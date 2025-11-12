# Voiceflow Documentation MCP Server

A Model Context Protocol (MCP) server that provides search and query capabilities for Voiceflow documentation.

## Project Structure

```
voiceflow-docs-mcp/
├── voiceflow_docs_mcp/     # Main MCP server package
│   ├── __init__.py         # Package initialization
│   ├── server.py           # MCP server implementation
│   ├── db_manager.py       # Database operations
│   ├── config.py           # Configuration management
│   └── parser.py           # Documentation parser
├── data/                   # Documentation database and content
├── docs/                   # Project documentation and guides
├── archive/                # Test scripts and development artifacts
├── pyproject.toml          # Python project configuration
├── uv.lock                 # Dependency lock file
└── README.md               # This file
```

## Installation

1. Ensure Python 3.10+ is installed
2. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Usage

Run the MCP server:
```bash
uv run voiceflow-docs-mcp
```

Or use as a module:
```bash
python -m voiceflow_docs_mcp.server
```

## Configuration

Configure the server in your MCP client (e.g., Claude Desktop) by adding to the configuration file:

```json
{
  "mcpServers": {
    "voiceflow-docs": {
      "command": "uv",
      "args": ["run", "voiceflow-docs-mcp"],
      "cwd": "/path/to/voiceflow-docs-mcp"
    }
  }
}
```

## Features

- Search Voiceflow documentation
- Query agent variables
- Query function documentation
- Query function paths and interfaces
- Full-text search with relevance ranking

## Development

See `docs/` folder for:
- Setup guides
- Configuration instructions
- Development notes
- Test reports

## Dependencies

- `fastmcp` - MCP server framework
- `beautifulsoup4` - HTML parsing
- `httpx` - HTTP client
- `markdownify` - HTML to Markdown conversion
- `playwright` - Web scraping
- `python-frontmatter` - Markdown frontmatter parsing
- `pyyaml` - YAML processing

## License

[Add license information here]
