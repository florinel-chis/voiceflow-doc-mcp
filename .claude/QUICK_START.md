# 🚀 Quick Start - Multi-Source Documentation MCP

## What's Configured

✅ **Project-Level MCP Server** is now active for this project!

When you work in this project directory, you automatically have access to:
- 🔍 Search across **194 documentation pages**
- 📚 **Voiceflow** (182 docs) + **Claude Code** (12 docs)
- 💻 **517 code examples** searchable
- 🏷️ **8 categories** for organized browsing

---

## How to Use

### Option 1: Natural Questions
Just ask Claude naturally:

```
"How do I use MCP in Voiceflow?"
"Show me the API step documentation"
"Find code examples for integrations"
"What are the Claude Code setup steps?"
```

### Option 2: Specific Tool Calls
Ask Claude to use specific tools:

```
"Use search_documentation to find MCP integration docs"
"List all documentation categories"
"Search for code examples about webhooks"
```

---

## Available Tools

| Tool | Purpose | Example |
|------|---------|---------|
| `search_documentation` | Search all docs | "Find MCP integration info" |
| `get_document` | Get full content | "Show me document 42" |
| `search_code_examples` | Find code | "Find JSON examples" |
| `list_categories` | Browse categories | "What categories exist?" |
| `get_integration_docs` | Integration-specific | "Get Zapier integration docs" |
| `find_step_documentation` | Voiceflow steps | "Find API step docs" |

---

## Testing

### Quick Test
Ask Claude:
```
"Search the documentation for 'MCP integration'"
```

Expected result: Claude uses the `multi-docs` MCP server and returns results from both Voiceflow and Claude Code documentation.

### Verify Server
Check that MCP server is loaded:
```
"What MCP tools do you have access to?"
```

You should see 6 tools from the `multi-docs` server listed.

---

## Examples by Use Case

### Learning Voiceflow
```
"How do I create a Knowledge Base step?"
"What's the difference between API step and Function step?"
"Show me examples of custom actions"
```

### Learning Claude Code
```
"How do I set up Claude Code?"
"What are the CLI commands available?"
"How do I configure MCP servers in Claude Code?"
```

### Comparing Both
```
"Compare MCP integration in Voiceflow vs Claude Code"
"How do both platforms handle webhooks?"
"Show me all MCP-related documentation"
```

### Finding Code
```
"Find code examples for API calls"
"Show me JSON configuration examples"
"Find TypeScript examples in the docs"
```

---

## Configuration Files

### Project-Level (This Project)
**File:** `.claude/settings.local.json`
**Scope:** Only when working in this directory
**Status:** ✅ Configured

### Global-Level (Optional)
**File:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Scope:** All projects and conversations
**Status:** ✅ Also configured (optional)

---

## Troubleshooting

### MCP Server Not Working?

1. **Verify configuration exists:**
   ```bash
   cat .claude/settings.local.json
   ```

2. **Test server manually:**
   ```bash
   DOCS_PATH="$(pwd)" uv run python -m voiceflow_docs_mcp.server
   ```

3. **Check database:**
   ```bash
   ls -lh ~/.mcp/multi-docs/database.db
   ```

4. **Restart Claude Code:**
   Close and reopen the project

### No Results Found?

1. **Check database is indexed:**
   ```bash
   uv run python scripts/test_mcp_direct.py
   ```

2. **Verify sources:**
   ```bash
   ls data/voiceflow_docs/ | wc -l  # Should show 182
   ls data/claude_code_docs/ | wc -l  # Should show 12
   ```

---

## What's Different from Global Config?

| Aspect | Project-Level (.claude) | Global-Level |
|--------|------------------------|--------------|
| **Active when** | Working in this project | Always |
| **Best for** | Project-specific work | Universal access |
| **Configuration** | ✅ Set up now | ✅ Also set up |
| **Recommended** | ✅ Yes for this project | Optional |

---

## Next Steps

1. ✅ Configuration complete!
2. Open this project in Claude Code
3. Ask a documentation question
4. Verify results come from MCP server

**You're ready to go!** 🎉

---

## Resources

- **Full Guide:** `MCP_CONFIGURATION_GUIDE.md`
- **Test Reports:** `LOCAL_TEST_REPORT.md`
- **Implementation Details:** `MULTI_SOURCE_COMPLETION.md`
- **User Guide:** `README_VOICEFLOW_MCP.md`

---

**Project:** Multi-Source Documentation MCP
**Status:** ✅ Ready for Use
**Sources:** Voiceflow (182) + Claude Code (12) = 194 docs
**Code Examples:** 517
**Categories:** 8
