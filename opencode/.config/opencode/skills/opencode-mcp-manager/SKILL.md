---
name: opencode-mcp-manager
description: 专门用于管理和配置 OpenCode MCP 服务器的技能。当用户需要为 OpenCode 添加、配置或管理 MCP 服务器时使用此技能。它能够根据 OpenCode 特定的配置格式要求，将 Claude Desktop 格式转换为 OpenCode 格式，处理环境变量，并生成正确的配置文件。
---

# OpenCode MCP 管理器

## 技能概述

此技能专门用于管理 OpenCode 的 MCP（Model Context Protocol）服务器配置。它能够处理 OpenCode 与 Claude Desktop 之间的配置格式差异，确保所有 MCP 服务器配置符合 OpenCode 的要求。

## 何时使用此技能

- 需要为 OpenCode 添加新的 MCP 服务器
- 从 Claude Desktop 迁移 MCP 配置到 OpenCode
- 修复 OpenCode MCP 配置错误
- 验证 MCP 配置格式的正确性
- 处理环境变量在 OpenCode 中的配置

## OpenCode 配置格式要求

OpenCode 使用特定的 JSON 格式，与 Claude Desktop 有重要区别：

### 标准格式
```json
"server-name": {
  "type": "local",
  "command": ["command", "arg1", "arg2"],
  "enabled": true
}
```

### 关键区别
1. **必须添加** `"type": "local"` 属性
2. **command 使用数组格式**，包含命令和所有参数
3. **不支持 env 属性**，环境变量需通过 env 命令设置
4. **必须添加** `"enabled": true` 属性
5. **使用绝对路径**

## 环境变量处理方法

由于 OpenCode 不支持单独的 env 属性，使用以下方法：

### 方法1：使用 env 命令（推荐）
```json
"command": ["env", "VAR1=value1", "VAR2=value2", "actual-command", "arg1", "arg2"]
```

### 转换示例
Claude Desktop 格式：
```json
"obsidian-mcp": {
  "command": "npx",
  "args": ["@huangyihe/obsidian-mcp"],
  "env": {
    "OBSIDIAN_VAULT_PATH": "/path/to/vault",
    "OBSIDIAN_API_TOKEN": "token"
  }
}
```

OpenCode 格式：
```json
"obsidian-mcp": {
  "type": "local",
  "command": ["env", "OBSIDIAN_VAULT_PATH=/path/to/vault", "OBSIDIAN_API_TOKEN=token", "npx", "@huangyihe/obsidian-mcp"],
  "enabled": true
}
```

## 常见 MCP 服务器配置模板

### 文件系统服务器
```json
"filesystem": {
  "type": "local",
  "command": ["npx", "-y", "@modelcontextprotocol/server-filesystem", "/home/lyna/"],
  "enabled": true
}
```

### Fetch 服务器
```json
"fetch": {
  "type": "local",
  "command": ["uvx", "mcp-server-fetch"],
  "enabled": true
}
```

### Playwright 服务器
```json
"playwright": {
  "type": "local",
  "command": ["npx", "@playwright/mcp@latest"],
  "enabled": true
}
```

## 配置生成工作流程

### 步骤1：收集服务器信息
当用户需要添加新的 MCP 服务器时，收集以下信息：
- 服务器名称
- 主命令
- 参数列表
- 环境变量（如果有）
- 工作目录（可选）

### 步骤2：格式转换
将 Claude Desktop 格式转换为 OpenCode 格式：
1. 添加 `"type": "local"`
2. 合并 command 和 args 为 command 数组
3. 处理环境变量（使用 env 命令前缀）
4. 添加 `"enabled": true`
5. 确保使用绝对路径

### 步骤3：验证配置
检查生成的配置是否符合 OpenCode 要求：
- 是否包含必需的 type 属性
- command 是否为数组格式
- 是否包含 enabled 属性
- 环境变量是否正确处理
- 路径是否为绝对路径

## 故障排除指南

### 常见错误及解决方案

1. **配置验证失败**
   - 检查是否有不允许的属性（如 env）
   - 确保 JSON 格式正确

2. **服务器启动失败**
   - 检查命令路径和权限
   - 验证数组格式的 command 是否正确

3. **环境变量不生效**
   - 确保使用 env 命令正确设置
   - 检查环境变量格式是否为 KEY=VALUE

## 使用示例

### 用户输入模板
```
我需要为 OpenCode 添加一个新的 MCP 服务器配置。

服务器名称：[服务器名称]
命令：[主命令]
参数：[参数列表，用空格分隔]
环境变量：[变量名=值 对，用空格分隔]
工作目录：[可选，默认为系统路径]
```

### 处理流程示例
用户请求：
```
服务器名称：my-mcp-server
命令：python
参数：-m mcp_server --port 8080
环境变量：API_KEY=abc123 DEBUG=true
```

生成的 OpenCode 配置：
```json
"my-mcp-server": {
  "type": "local",
  "command": ["env", "API_KEY=abc123", "DEBUG=true", "python", "-m", "mcp_server", "--port", "8080"],
  "enabled": true
}
```

## 最佳实践

1. **始终使用绝对路径**：确保所有路径都是完整的绝对路径
2. **验证命令存在性**：确保配置中使用的命令在系统中可用
3. **环境变量安全**：避免在配置中硬编码敏感信息
4. **保持配置整洁**：移除不必要的属性和注释
5. **测试配置**：添加新配置后测试服务器是否能正常启动

## 文档参考

详细的配置对比和示例请参考：
- OpenCode MCP 配置技术说明与对比文档
- MCP 官方文档
- 各 MCP 服务器的具体配置要求