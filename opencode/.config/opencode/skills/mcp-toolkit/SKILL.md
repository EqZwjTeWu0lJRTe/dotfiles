---
name: mcp-toolkit
description: A skill for orchestrating and utilizing MCP (Model Context Protocol) tools including filesystem operations, Obsidian note management, web automation with Playwright, and other available MCP resources.
---

# MCP Toolkit Skill

This skill enables Claude to effectively utilize the available MCP (Model Context Protocol) tools for various tasks including file management, Obsidian note operations, web automation, and more.

## When to Use This Skill

Use this skill when you need to:
- Read, write, or organize files and directories
- Manage Obsidian notes (search, read, create, update)
- Automate web interactions (navigation, screenshots, form filling)
- Fetch web content or convert markdown to mindmaps
- Perform any operation supported by the configured MCP tools

## Available MCP Tools

### 1. Filesystem Tools (`mcp__filesystem__*`)
- **List directories**: `mcp__filesystem__list_directory`, `mcp__filesystem__list_allowed_directories`
- **Read files**: `mcp__filesystem__read_text_file`, `mcp__filesystem__read_multiple_files`
- **Write/edit files**: `mcp__filesystem__write_file`, `mcp__filesystem__edit_file`
- **Search/explore**: `mcp__filesystem__search_files`, `mcp__filesystem__directory_tree`
- **File operations**: `mcp__filesystem__move_file`, `mcp__filesystem__get_file_info`, `mcp__filesystem__create_directory`

**Allowed directories**: `/home/lyna`

### 2. Obsidian Tools (Two MCP Servers)

#### Server 1: `mcp__obsidian-mcp__*`
- **List notes**: `mcp__obsidian-mcp__list_notes`
- **Read notes**: `mcp__obsidian-mcp__read_note`, `mcp__obsidian-mcp__read_multiple_notes`
- **Create/update notes**: `mcp__obsidian-mcp__create_note`, `mcp__obsidian-mcp__update_note`
- **Search**: `mcp__obsidian-mcp__search_vault`
- **Manage folders**: `mcp__obsidian-mcp__manage_folder`

#### Server 2: `mcp__mcp-obsidian-ek__*` (Extended features)
- **Vault navigation**: `obsidian_list_files_in_vault`, `obsidian_list_files_in_dir`
- **Read content**: `obsidian_get_file_contents`, `obsidian_batch_get_file_contents`
- **Search**: `obsidian_simple_search`, `obsidian_complex_search`, `obsidian_dataview_query`
- **Edit notes**: `obsidian_patch_content`, `obsidian_append_content`, `obsidian_put_content`
- **Periodic notes**: `obsidian_get_periodic_note`, `obsidian_get_recent_periodic_notes`
- **UI integration**: `obsidian_open_file`, `obsidian_get_active`, `obsidian_execute_command`

### 3. Playwright Browser Automation (`mcp__playwright__*`)
- **Navigation**: `browser_navigate`, `browser_navigate_back`
- **Interaction**: `browser_click`, `browser_type`, `browser_fill_form`, `browser_select_option`
- **Screenshots**: `browser_take_screenshot`, `browser_snapshot`
- **Evaluation**: `browser_evaluate`, `browser_run_code`
- **Tab management**: `browser_tabs`
- **Network/console**: `browser_network_requests`, `browser_console_messages`
- **Wait/dialogs**: `browser_wait_for`, `browser_handle_dialog`

**Protocol restriction**: Only `http:`, `https:`, `about:`, `data:` protocols allowed. `file://` URLs are blocked.

### 4. Fetch Tool (`mcp__fetch__fetch`)
- Fetch web content with optional markdown conversion
- Supports URLs with automatic HTTPS upgrade
- Includes 15-minute cache for repeated requests

### 5. Mindmap Tool (`mcp__mindmap__convert_markdown_to_mindmap`)
- Convert markdown content to interactive mindmaps
- Returns HTML with D3.js visualization

## Instructions for Using MCP Tools

### General Guidelines
1. **Check availability**: Use `ListMcpResourcesTool` to see available MCP resources
2. **Choose appropriate tool**: Select the most specific tool for the task
3. **Handle errors gracefully**: MCP tools may return errors for invalid paths, permissions, etc.
4. **Respect boundaries**: Only access allowed directories and follow protocol restrictions

### Filesystem Operations
```text
When user needs to read a file:
1. Check if file is in allowed directory (/home/lyna)
2. Use mcp__filesystem__read_text_file with path parameter
3. For large files, use head/tail parameters to limit reading

When user needs to list directory contents:
1. Use mcp__filesystem__list_directory with path parameter
2. For detailed info, use mcp__filesystem__list_directory_with_sizes
3. For tree view, use mcp__filesystem__directory_tree
```

### Obsidian Note Management
```text
When user needs to read an Obsidian note:
1. Use mcp__obsidian-mcp__read_note for simple reading
2. Use obsidian_get_file_contents for the other server
3. Check note path format (relative to vault root)

When user needs to search notes:
1. Use obsidian_simple_search for text search
2. Use obsidian_dataview_query for structured queries (if Dataview plugin available)
3. Use mcp__obsidian-mcp__search_vault for basic search
```

### Web Automation with Playwright
```text
When user needs to interact with a webpage:
1. Use browser_navigate to go to URL (must be http/https)
2. Use browser_snapshot to see page structure
3. Use browser_click, browser_type for interactions
4. Use browser_take_screenshot for visual capture
5. Always close browser with browser_close when done
```

### Web Content Fetching
```text
When user needs to fetch web content:
1. Use mcp__fetch__fetch with URL and optional prompt
2. Content is converted to markdown when possible
3. Use max_length parameter for large pages
```

## Examples

### Example 1: Read Today's Obsidian Diary
```text
1. Determine today's date in format YYYY-MM-DD
2. Construct path: "日记/2025年/冬季/2026-01-20.md" (adjust year/season)
3. Use mcp__obsidian-mcp__read_note or obsidian_get_file_contents
4. Extract and summarize content for user
```

### Example 2: Take Website Screenshot
```text
1. Use browser_navigate to go to https://example.com
2. Use browser_take_screenshot with filename parameter
3. Save screenshot to allowed directory
4. Close browser with browser_close
```

### Example 3: Search Obsidian for Specific Content
```text
1. Use obsidian_simple_search with query term
2. Parse results to show matching files and context
3. Optionally read full notes for top matches
```

### Example 4: Create Markdown Mindmap
```text
1. Prepare markdown content with hierarchical structure
2. Use mcp__mindmap__convert_markdown_to_mindmap
3. Save resulting HTML to file or return to user
```

## Best Practices

1. **Resource cleanup**: Always close Playwright browser sessions when done
2. **Path validation**: Ensure file paths are within allowed directories
3. **Error handling**: Check for common errors (file not found, permission denied, invalid URL)
4. **Performance**: Use batch operations when processing multiple files/notes
5. **User feedback**: Provide clear status updates when operations take time

## Common Errors and Solutions

- **"Access to 'file:' URL is blocked"**: Use HTTP server or online test page for Playwright
- **"File not found"**: Verify path is relative to vault root for Obsidian, absolute for filesystem
- **"Permission denied"**: Check if path is within allowed directories (`/home/lyna`)
- **"Invalid tool call"**: Verify tool name and parameters match available MCP tools

## Testing the Skill

To verify MCP tools are working:
1. List available MCP resources with `ListMcpResourcesTool`
2. Test filesystem access with `mcp__filesystem__list_allowed_directories`
3. Test Obsidian with `mcp__obsidian-mcp__list_notes` (should return 300+ files)
4. Test Playwright with `browser_navigate` to `https://httpbin.org/html`
5. Test fetch with `mcp__fetch__fetch` to `https://httpbin.org/get`

---

**Note**: This skill provides guidance for using MCP tools that are already configured in the environment. The actual availability of tools depends on the MCP server configuration.