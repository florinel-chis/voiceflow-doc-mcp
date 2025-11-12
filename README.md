# Multi-Source Documentation MCP Server

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that enables AI assistants like Claude to search and query documentation from multiple sources. Currently supports **Voiceflow** and **Claude Code** documentation.

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd voiceflow-docs-mcp

# Install dependencies
uv sync
```

### Running the Server

```bash
# Run directly
uv run voiceflow-docs-mcp

# Or as a Python module
python -m voiceflow_docs_mcp.server
```

## 🔧 Configuration

### Claude Desktop Integration

Add this configuration to your Claude Desktop config file:

**MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "voiceflow-docs": {
      "command": "uv",
      "args": ["run", "voiceflow-docs-mcp"],
      "cwd": "/absolute/path/to/voiceflow-docs-mcp"
    }
  }
}
```

After adding the configuration, restart Claude Desktop.

## 📚 Available Tools

The server provides 6 specialized tools for documentation access:

| Tool | Description |
|------|-------------|
| `search_documentation` | Full-text search across all documentation sources with relevance ranking |
| `get_document` | Retrieve a specific document by its exact path or identifier |
| `search_code_examples` | Search for code snippets and examples across documentation |
| `list_categories` | List available documentation categories and topics |
| `get_integration_docs` | Get integration-specific documentation and guides |
| `find_step_documentation` | Find step-by-step tutorials and walkthroughs |

## 📁 Project Structure

```
voiceflow-docs-mcp/
├── voiceflow_docs_mcp/          # Main MCP server package
│   ├── __init__.py              # Package initialization
│   ├── server.py                # MCP server implementation (6 tools)
│   ├── db_manager.py            # SQLite database operations
│   ├── config.py                # Configuration and environment handling
│   └── parser.py                # Markdown documentation parser
│
├── data/                        # Documentation content (1.3 MB)
│   ├── voiceflow_docs/          # 182 Voiceflow documentation files
│   └── claude_code_docs/        # 12 Claude Code documentation files
│
├── .claude/                     # Claude Code configuration
│   ├── QUICK_START.md           # Quick start guide
│   ├── README.md                # Claude-specific readme
│   └── settings.local.json      # Local settings (gitignored)
│
├── .gitignore                   # Git ignore rules
├── .python-version              # Python version specification (3.10+)
├── pyproject.toml               # Project metadata and dependencies
├── uv.lock                      # Locked dependency versions
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## 🛠️ Technical Details

### Documentation Database

- **Storage**: SQLite database with full-text search (FTS5)
- **Sources**: Multi-source support (Voiceflow, Claude Code, extensible)
- **Indexing**: Automatic on first run, incremental updates supported
- **Search**: Full-text search with BM25 relevance ranking

### Dependencies

| Package | Purpose |
|---------|---------|
| `fastmcp` | MCP server framework |
| `beautifulsoup4` | HTML parsing and cleaning |
| `httpx` | Async HTTP client for fetching docs |
| `markdownify` | HTML to Markdown conversion |
| `playwright` | Web scraping for documentation |
| `python-frontmatter` | Parse YAML frontmatter in Markdown |
| `pyyaml` | YAML processing |

### Data Sources

**Voiceflow Documentation** (182 files)
- Complete Voiceflow platform documentation
- API references, guides, tutorials
- Integration documentation

**Claude Code Documentation** (12 files)
- Claude Code feature documentation
- Setup and configuration guides
- Best practices and troubleshooting

## 🔍 Usage Examples

### Searching Documentation

```python
# When connected to Claude Desktop, you can ask:
"Search the Voiceflow docs for information about API blocks"
"Find code examples for integrating with external APIs"
"What are the available Voiceflow integrations?"
"Show me step-by-step guides for setting up a voice assistant"
```

### Querying Specific Documents

```python
# Ask Claude to retrieve specific documentation:
"Get the document about Voiceflow agent variables"
"Show me the integration docs for Zapier"
"Find the documentation on condition blocks"
```

## 🧪 Development

### Project Status

- ✅ Multi-source documentation support
- ✅ Full-text search with relevance ranking
- ✅ 6 specialized MCP tools
- ✅ SQLite database with FTS5
- ✅ Automatic documentation indexing
- ✅ Claude Desktop integration

### Adding New Documentation Sources

The server is designed to support multiple documentation sources. To add a new source:

1. Add documentation files to `data/your-source-name/`
2. Update configuration in `voiceflow_docs_mcp/config.py`
3. The server will automatically index new files on restart

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

```bash
# Clone and install
git clone <your-repo-url>
cd voiceflow-docs-mcp
uv sync

# Run in development mode
uv run python -m voiceflow_docs_mcp.server
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp) - A Python framework for MCP servers
- Documentation sourced from [Voiceflow](https://www.voiceflow.com/) and [Claude Code](https://claude.ai/code)
- Designed for use with [Claude Desktop](https://claude.ai/download)

## 📞 Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Note**: This is an unofficial community project and is not affiliated with Anthropic or Voiceflow.
