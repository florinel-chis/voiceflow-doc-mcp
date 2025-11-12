"""
SQLite database manager with FTS5 full-text search for multi-source documentation
Supports: Voiceflow, Claude Code, and other documentation sources
"""

import sqlite3
from pathlib import Path
from typing import List, Dict, Optional
import hashlib
import json


class VoiceflowDocsDB:
    """SQLite database with FTS5 for documentation search"""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(db_path))
        self.conn.row_factory = sqlite3.Row
        self._create_schema()

    def _create_schema(self):
        """Create database schema with FTS5 tables"""
        with self.conn:
            # Main documents table
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    id INTEGER PRIMARY KEY,
                    source TEXT NOT NULL,
                    path TEXT UNIQUE NOT NULL,
                    title TEXT NOT NULL,
                    category TEXT NOT NULL,
                    subcategory TEXT,
                    url TEXT,
                    content_hash TEXT NOT NULL,
                    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # FTS5 full-text search (standalone, no external content)
            self.conn.execute("""
                CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts
                USING fts5(
                    title,
                    content,
                    headings,
                    tags
                )
            """)

            # Code examples table
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS code_examples (
                    id INTEGER PRIMARY KEY,
                    document_id INTEGER NOT NULL,
                    language TEXT,
                    code TEXT NOT NULL,
                    FOREIGN KEY (document_id) REFERENCES documents(id)
                )
            """)

    def index_documents(self, documents: List[Dict]) -> int:
        """
        Index parsed documents into database

        Args:
            documents: List of parsed document dictionaries

        Returns:
            Number of documents indexed
        """
        indexed_count = 0

        with self.conn:
            for doc in documents:
                # Calculate content hash
                content_hash = hashlib.md5(
                    doc['content'].encode()
                ).hexdigest()

                # Check if document already exists with same hash
                existing = self.conn.execute(
                    "SELECT content_hash FROM documents WHERE path = ?",
                    (doc['path'],)
                ).fetchone()

                if existing and existing['content_hash'] == content_hash:
                    continue  # Skip unchanged documents

                # Insert or replace document
                cursor = self.conn.execute("""
                    INSERT OR REPLACE INTO documents
                    (source, path, title, category, subcategory, url, content_hash)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    doc.get('source', 'voiceflow'),
                    doc['path'],
                    doc['title'],
                    doc['category'],
                    doc.get('subcategory', ''),
                    doc.get('url', ''),
                    content_hash
                ))

                doc_id = cursor.lastrowid

                # Update FTS5 index
                self.conn.execute("""
                    INSERT OR REPLACE INTO documents_fts
                    (rowid, title, content, headings, tags)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    doc_id,
                    doc['title'],
                    doc['content'],
                    ' '.join(doc.get('headings', [])),
                    ' '.join(doc.get('tags', []))
                ))

                # Delete old code examples
                self.conn.execute(
                    "DELETE FROM code_examples WHERE document_id = ?",
                    (doc_id,)
                )

                # Index code blocks
                for code_block in doc.get('code_blocks', []):
                    self.conn.execute("""
                        INSERT INTO code_examples
                        (document_id, language, code)
                        VALUES (?, ?, ?)
                    """, (doc_id, code_block['language'], code_block['code']))

                indexed_count += 1

        return indexed_count

    def search(
        self,
        query: str,
        source: Optional[str] = None,
        category: Optional[str] = None,
        limit: int = 5
    ) -> List[Dict]:
        """
        Full-text search across documents

        Args:
            query: Search query
            source: Optional source filter ('voiceflow', 'claude-code', or None for all)
            category: Optional category filter
            limit: Maximum number of results

        Returns:
            List of matching documents with snippets
        """
        sql = """
            SELECT
                d.id, d.source, d.title, d.category, d.url, d.path,
                snippet(documents_fts, 1, '<mark>', '</mark>', '...', 30) as snippet,
                documents_fts.rank
            FROM documents_fts
            JOIN documents d ON d.id = documents_fts.rowid
            WHERE documents_fts MATCH ?
        """

        params = [query]

        if source and source != "all":
            sql += " AND d.source = ?"
            params.append(source)

        if category:
            sql += " AND d.category = ?"
            params.append(category)

        sql += " ORDER BY documents_fts.rank LIMIT ?"
        params.append(limit)

        cursor = self.conn.execute(sql, params)
        return [dict(row) for row in cursor.fetchall()]

    def get_document(self, doc_id: int) -> Optional[Dict]:
        """
        Get full document by ID

        Args:
            doc_id: Document ID

        Returns:
            Document dictionary or None
        """
        cursor = self.conn.execute("""
            SELECT * FROM documents WHERE id = ?
        """, (doc_id,))

        row = cursor.fetchone()
        if not row:
            return None

        doc = dict(row)

        # Read full content from file
        try:
            with open(doc['path'], 'r', encoding='utf-8') as f:
                import frontmatter
                post = frontmatter.load(f)
                doc['full_content'] = post.content
        except Exception as e:
            doc['full_content'] = f"Error reading file: {e}"

        # Get code examples
        cursor = self.conn.execute("""
            SELECT language, code FROM code_examples
            WHERE document_id = ?
        """, (doc_id,))

        doc['code_examples'] = [dict(row) for row in cursor.fetchall()]

        return doc

    def get_document_by_url(self, url: str) -> Optional[Dict]:
        """
        Get document by URL path

        Args:
            url: URL path (e.g., '/docs/mcp-tool')

        Returns:
            Document dictionary or None
        """
        cursor = self.conn.execute("""
            SELECT id FROM documents WHERE url = ?
        """, (url,))

        row = cursor.fetchone()
        if not row:
            return None

        return self.get_document(row['id'])

    def search_code_examples(
        self,
        query: str,
        language: Optional[str] = None,
        limit: int = 5
    ) -> List[Dict]:
        """
        Search for code examples

        Args:
            query: Search term
            language: Optional language filter
            limit: Maximum results

        Returns:
            List of code examples with context
        """
        # First find documents matching query
        docs = self.search(query, limit=limit * 2)

        examples = []
        seen_codes = set()

        for doc in docs:
            full_doc = self.get_document(doc['id'])
            if not full_doc:
                continue

            for example in full_doc.get('code_examples', []):
                if language and example['language'] != language:
                    continue

                # Avoid duplicates
                code_hash = hashlib.md5(example['code'].encode()).hexdigest()
                if code_hash in seen_codes:
                    continue

                seen_codes.add(code_hash)

                examples.append({
                    'code': example['code'],
                    'language': example['language'],
                    'source': doc['title'],
                    'url': doc['url'],
                    'doc_id': doc['id']
                })

                if len(examples) >= limit:
                    break

            if len(examples) >= limit:
                break

        return examples

    def list_categories(self, source: Optional[str] = None) -> List[Dict]:
        """
        Get all categories with document counts

        Args:
            source: Optional source filter ('voiceflow', 'claude-code', or None for all)

        Returns:
            List of category dictionaries
        """
        if source and source != "all":
            cursor = self.conn.execute("""
                SELECT source, category, COUNT(*) as count
                FROM documents
                WHERE source = ?
                GROUP BY source, category
                ORDER BY category
            """, (source,))
        else:
            cursor = self.conn.execute("""
                SELECT source, category, COUNT(*) as count
                FROM documents
                GROUP BY source, category
                ORDER BY source, category
            """)
        return [dict(row) for row in cursor.fetchall()]

    def get_stats(self) -> Dict:
        """
        Get database statistics

        Returns:
            Statistics dictionary
        """
        total_docs = self.conn.execute(
            "SELECT COUNT(*) as count FROM documents"
        ).fetchone()['count']

        total_code = self.conn.execute(
            "SELECT COUNT(*) as count FROM code_examples"
        ).fetchone()['count']

        # Get stats by source
        source_stats = self.conn.execute("""
            SELECT source, COUNT(*) as count
            FROM documents
            GROUP BY source
            ORDER BY source
        """)
        by_source = {row['source']: row['count'] for row in source_stats.fetchall()}

        return {
            'total_documents': total_docs,
            'total_code_examples': total_code,
            'by_source': by_source,
            'database_path': str(self.db_path),
            'database_size_kb': self.db_path.stat().st_size // 1024 if self.db_path.exists() else 0
        }

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
