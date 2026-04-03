---
description: 创建新的自定义命令
agent: build
model: opencode/minimax-m2.5-free
---

创建 OpenCode 自定义命令：名称根据用户需求自定义



**创建命令文件：**
在 `~/.config/opencode/commands/***.md` 中创建文件

**模板内容：**
```markdown
---
description: $2
agent: build
model: opencode/minimax-m2.5-free
---


```

请根据我的需求，生成完整的自定义命令模板，包含：
1. 适当的 YAML frontmatter
2. 清晰的功能描述
3. 使用示例
4. 参数说明
5. 相关的最佳实践建议
```

**使用方式：**
```bash
/create-command <命令名称> "<描述>" "<功能用途>" "<使用场景>"
```

**示例：**
```bash
/create-command code-review "代码审查" "对当前文件进行代码审查和优化建议" "在编写完代码后需要检查代码质量和潜在问题"
```

这个命令模板会创建一个通用的命令创建器，你可以通过参数指定新命令的各种属性，然后让 OpenCode 自动生成对应的命令文件。
