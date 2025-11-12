"""
Markdown documentation parser with frontmatter support
"""

import frontmatter
from pathlib import Path
from typing import Dict, List
import re


class VoiceflowDocsParser:
    """Parse Voiceflow markdown documentation with YAML frontmatter"""

    def parse_file(self, file_path: Path) -> Dict:
        """
        Parse a single markdown file with frontmatter

        Args:
            file_path: Path to markdown file

        Returns:
            Dictionary with parsed content and metadata
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        return {
            'path': str(file_path),
            'title': post.get('title', file_path.stem),
            'category': post.get('category', 'general'),
            'subcategory': post.get('subcategory', ''),
            'url': post.get('url', ''),
            'tags': post.get('tags', []),
            'content': post.content,
            'code_blocks': self.extract_code_blocks(post.content),
            'headings': self.extract_headings(post.content),
        }

    def extract_code_blocks(self, content: str) -> List[Dict]:
        """
        Extract code blocks with language tags

        Args:
            content: Markdown content

        Returns:
            List of dicts with 'language' and 'code' keys
        """
        pattern = r'```(\w+)?\n(.*?)```'
        matches = re.findall(pattern, content, re.DOTALL)

        return [
            {
                'language': lang or 'text',
                'code': code.strip()
            }
            for lang, code in matches
        ]

    def extract_headings(self, content: str) -> List[str]:
        """
        Extract all headings for better search indexing

        Args:
            content: Markdown content

        Returns:
            List of heading texts
        """
        pattern = r'^#+\s+(.+)$'
        return re.findall(pattern, content, re.MULTILINE)

    def parse_directory(self, docs_path: Path) -> List[Dict]:
        """
        Parse all markdown files in directory recursively

        Args:
            docs_path: Path to documentation directory

        Returns:
            List of parsed documents
        """
        documents = []

        for md_file in docs_path.rglob('*.md'):
            if md_file.name in ['README.md', 'CLAUDE.md', 'SCRAPING_REPORT.md']:
                continue

            try:
                doc = self.parse_file(md_file)
                documents.append(doc)
            except Exception as e:
                print(f"Warning: Error parsing {md_file}: {e}")

        return documents
