---
description: 同步 MCP 配置
agent: build
model: deepseek/deepseek-chat
---

同步 MCP (Model Context Protocol) 配置，使OpenCode、Claude Desktop 和 Obsidian Claude三者mcp一致,注意配置格式差异。
以mcp最多的为准
**支持的配置文件：**
1. OpenCode: `~/.config/opencode/opencode.json` (格式: `{mcp: {name: {type: "local", command: [...], enabled: true}}}`)
2. Claude Desktop MCP: `~/sync/文档/Obsidian/lyna-note/.claude/mcp.json` (格式: `{mcpServers: {name: {command: "...", args: [...]}}}`)
3. Claude Desktop 项目: `~/.claude.json` (格式: `{projects["/home/lyna"].mcpServers: {...}}`)

**典型使用场景：**
- 在 OpenCode、Claude Desktop 和 Obsidian Claude 之间同步 MCP 配置
- 迁移 MCP 服务器配置到不同环境
- 备份和恢复 MCP 配置
- 统一多个工具的 MCP 配置
- 处理不同客户端的配置格式差异



**格式转换规则：**
- OpenCode → Claude Desktop: `{type: "local", command: [...]}` → `{command: "...", args: [...]}`
- Claude Desktop → OpenCode: `{command: "...", args: [...]}` → `{type: "local", command: [...], enabled: true}`
- 特殊处理 `obsidian-mcp` 的环境变量配置

