# Claude Code Project Configuration

This directory contains project-specific settings for Claude Code.

## Files

### `settings.local.json`
Project-level MCP server configuration. This file configures the multi-source documentation MCP server to be available when working on this project.

**Configuration:**
- **Server Name:** `multi-docs`
- **Type:** Multi-source documentation search (Voiceflow + Claude Code)
- **Scope:** Project-level (only available when working in this project)

## MCP Server

The configured MCP server provides:
- 🔍 **search_documentation** - Search across Voiceflow and Claude Code docs
- 📄 **get_document** - Retrieve full document content
- 💻 **search_code_examples** - Find code examples
- 📚 **list_categories** - Browse documentation categories
- 🔌 **get_integration_docs** - Get integration-specific docs
- 🧩 **find_step_documentation** - Find Voiceflow step docs

## Usage

When you open this project in Claude Code, the MCP server will automatically be available. You can ask questions like:

- "How do I use MCP in Voiceflow?"
- "Show me the API step documentation"
- "Find code examples for MCP configuration"
- "What integrations are available in Voiceflow?"

## Sources

The server indexes documentation from:
- **Voiceflow** (182 documents) - Located in `data/voiceflow_docs/`
- **Claude Code** (12 documents) - Located in `data/claude_code_docs/`

## Database

- **Location:** `~/.mcp/multi-docs/database.db`
- **Size:** ~1.8 MB
- **Documents:** 194 total
- **Code Examples:** 517 total

## Updating Documentation

To refresh the documentation:

```bash
# Re-scrape Voiceflow docs
uv run python scripts/scrape_docs.py

# Re-scrape Claude Code docs
uv run python scripts/scrape_claude_code.py

# Delete old database to force re-indexing
rm -f ~/.mcp/multi-docs/database.db
```

The database will be automatically rebuilt on the next MCP server start.

## Testing

To test the MCP server:

```bash
# Test all functionality
uv run python scripts/test_mcp_direct.py

# Test with sample queries
uv run python scripts/test_server.py
```

## Notes

- This configuration is project-specific and only applies when working in this directory
- The MCP server runs in the background when Claude Code is active
- Changes to `settings.local.json` require restarting Claude Code to take effect

## See Also

- [MULTI_SOURCE_COMPLETION.md](../MULTI_SOURCE_COMPLETION.md) - Implementation details
- [LOCAL_TEST_REPORT.md](../LOCAL_TEST_REPORT.md) - Test results
- [README_VOICEFLOW_MCP.md](../README_VOICEFLOW_MCP.md) - User guide
