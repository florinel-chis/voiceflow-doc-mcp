"""
Multi-Source Documentation MCP Server

Provides 6 specialized tools for searching Voiceflow and Claude Code documentation.
"""

from fastmcp import FastMCP
from pathlib import Path
import sys

from .parser import VoiceflowDocsParser
from .db_manager import VoiceflowDocsDB
from .config import Config


# Initialize MCP server
mcp = FastMCP("Multi-Source Documentation")

# Global instances (initialized on startup)
config = None
db = None
parser = None


def initialize_server():
    """Initialize database with documentation from all sources"""
    global config, db, parser

    print("🚀 Initializing Multi-Source Documentation MCP Server...")

    # Load configuration
    try:
        config = Config.from_env()
        config.validate()
        print(f"   Documentation sources: {', '.join(config.docs_paths.keys())}")
        for source, path in config.docs_paths.items():
            print(f"      - {source}: {path}")
        print(f"   Database path: {config.db_path}")
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        sys.exit(1)

    # Initialize database
    db = VoiceflowDocsDB(config.db_path)
    parser = VoiceflowDocsParser()

    # Check if database needs indexing
    stats = db.get_stats()
    if stats['total_documents'] == 0:
        print("   Database is empty, indexing documentation...")

        all_documents = []

        # Parse all documentation sources
        for source, docs_path in config.docs_paths.items():
            print(f"   Parsing {source} documentation from {docs_path}...")
            documents = parser.parse_directory(docs_path)
            # Ensure source is set
            for doc in documents:
                doc['source'] = source
            print(f"      Found {len(documents)} {source} documents")
            all_documents.extend(documents)

        # Index in database
        print(f"   Indexing {len(all_documents)} total documents in database...")
        indexed = db.index_documents(all_documents)
        print(f"   Indexed {indexed} documents")

        # Show stats by source
        stats = db.get_stats()
        if 'by_source' in stats:
            print(f"   Documents by source:")
            for source, count in stats['by_source'].items():
                print(f"      - {source}: {count} docs")
    else:
        print(f"   Database already indexed: {stats['total_documents']} documents, {stats['total_code_examples']} code examples")
        if 'by_source' in stats:
            print(f"   Documents by source:")
            for source, count in stats['by_source'].items():
                print(f"      - {source}: {count} docs")

    print("✅ Server ready!")


@mcp.tool()
def search_documentation(query: str, source: str = "all", category: str = None, limit: int = 5) -> dict:
    """
    Search Voiceflow and Claude Code documentation with full-text search.

    Use this tool to find documentation pages about features, integrations, or concepts.

    Args:
        query: Search query (e.g., "MCP integration", "KB search step", "custom actions")
        source: Documentation source filter - "voiceflow", "claude-code", or "all" (default: "all")
        category: Optional category filter
        limit: Maximum number of results to return (default: 5)

    Returns:
        Dictionary with search results including title, URL, snippet, source, and document ID

    Example:
        search_documentation("how to use MCP tool")
        search_documentation("API step configuration", source="voiceflow", limit=3)
        search_documentation("Claude Code setup", source="claude-code")
    """
    if not db:
        return {"error": "Database not initialized"}

    try:
        results = db.search(query, source=source, category=category, limit=limit)

        return {
            "query": query,
            "source_filter": source,
            "count": len(results),
            "results": results
        }
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_document(doc_id: int) -> dict:
    """
    Retrieve complete document content by ID.

    Use this tool to get the full documentation content after finding a document with search_documentation.

    Args:
        doc_id: Document ID from search results

    Returns:
        Full document with title, content, URL, code examples, and metadata

    Example:
        get_document(42)
    """
    if not db:
        return {"error": "Database not initialized"}

    try:
        doc = db.get_document(doc_id)

        if not doc:
            return {"error": f"Document ID {doc_id} not found"}

        return doc
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def search_code_examples(query: str, language: str = None, limit: int = 5) -> dict:
    """
    Search for code examples in Voiceflow documentation.

    Use this tool to find code snippets and implementation examples.

    Args:
        query: What kind of code to find (e.g., "MCP tool definition", "API request", "webhook")
        language: Optional language filter (e.g., "javascript", "python", "json", "typescript")
        limit: Maximum number of code examples to return (default: 5)

    Returns:
        Dictionary with code examples, their language, source document, and URL

    Example:
        search_code_examples("MCP tool configuration")
        search_code_examples("API request", language="json")
    """
    if not db:
        return {"error": "Database not initialized"}

    try:
        examples = db.search_code_examples(query, language=language, limit=limit)

        return {
            "query": query,
            "language": language,
            "count": len(examples),
            "examples": examples
        }
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def list_categories(source: str = "all") -> dict:
    """
    List all documentation categories with document counts by source.

    Use this tool to see what documentation categories are available.

    Args:
        source: Documentation source filter - "voiceflow", "claude-code", or "all" (default: "all")

    Returns:
        Dictionary with category list organized by source and total document count

    Example:
        list_categories()
        list_categories(source="voiceflow")
        list_categories(source="claude-code")
    """
    if not db:
        return {"error": "Database not initialized"}

    try:
        categories = db.list_categories(source=source)
        stats = db.get_stats()

        return {
            "source_filter": source,
            "categories": categories,
            "total_docs": stats['total_documents'],
            "total_code_examples": stats['total_code_examples'],
            "by_source": stats.get('by_source', {})
        }
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_integration_docs(integration: str) -> dict:
    """
    Get documentation for a specific Voiceflow integration.

    Use this tool to find docs about integrations like MCP, Zapier, Make, Airtable, etc.

    Args:
        integration: Integration name (e.g., "mcp", "zapier", "make", "hubspot", "salesforce")

    Returns:
        Main documentation and related docs for the integration

    Example:
        get_integration_docs("mcp")
        get_integration_docs("zapier")
    """
    if not db:
        return {"error": "Database not initialized"}

    try:
        # Search for integration
        results = db.search(f"{integration} integration tool", limit=3)

        if not results:
            return {"error": f"No documentation found for '{integration}' integration"}

        # Get full content for first result
        main_doc = db.get_document(results[0]['id'])

        return {
            "integration": integration,
            "main_doc": main_doc,
            "related_docs": results[1:] if len(results) > 1 else []
        }
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def find_step_documentation(step_name: str) -> dict:
    """
    Find documentation for a specific Voiceflow step.

    Use this tool to get docs about Voiceflow steps like API, Prompt, KB Search, Function, etc.

    Args:
        step_name: Step name (e.g., "API", "Prompt", "KB Search", "Function", "Custom Action", "Agent")

    Returns:
        Main documentation for the step and related pages

    Example:
        find_step_documentation("API")
        find_step_documentation("KB Search")
        find_step_documentation("Prompt")
    """
    if not db:
        return {"error": "Database not initialized"}

    try:
        # Search for step documentation
        results = db.search(f"{step_name} step", limit=3)

        if not results:
            return {"error": f"No documentation found for '{step_name}' step"}

        # Get full content for first result
        main_doc = db.get_document(results[0]['id'])

        return {
            "step_name": step_name,
            "documentation": main_doc,
            "related": results[1:] if len(results) > 1 else []
        }
    except Exception as e:
        return {"error": str(e)}


def main():
    """Main entry point for MCP server"""
    # Initialize on startup
    initialize_server()

    # Run MCP server
    mcp.run()


if __name__ == "__main__":
    main()
