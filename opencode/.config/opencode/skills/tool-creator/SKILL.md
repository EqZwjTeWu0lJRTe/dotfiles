---
name: tool-creator
description: 创建 LLM 可以在 opencode 中调用的自定义工具
---

# tool-creator 技能

## 目的
创建自定义工具，扩展 opencode 的功能，使 LLM 能够调用用户定义的函数来执行特定任务

## 使用场景
- 创建新的自定义工具供 LLM 调用
- 为现有项目添加功能扩展
- 将外部脚本集成到 opencode 工作流中
- 创建多语言工具（TypeScript/JavaScript + Python/Shell 等）

## 技能内容

### 1. 工具位置
工具可以定义在：
- **本地**：`.opencode/tool/` 目录中（项目级）
- **全局**：`~/.config/opencode/tool/` 目录中（用户级）

### 2. 基本结构模板
```typescript
// .opencode/tool/[tool-name].ts
import { tool } from "@opencode-ai/plugin"

export default tool({
  description: "工具描述",
  args: {
    param1: tool.schema.string().describe("参数1描述"),
    param2: tool.schema.number().describe("参数2描述"),
  },
  async execute(args, context) {
    // 工具实现逻辑
    return "结果"
  },
})
```

### 3. 多工具导出模板
```typescript
// .opencode/tool/math.ts
import { tool } from "@opencode-ai/plugin"

export const add = tool({
  description: "两个数字相加",
  args: {
    a: tool.schema.number().describe("第一个数字"),
    b: tool.schema.number().describe("第二个数字"),
  },
  async execute(args) {
    return args.a + args.b
  },
})

export const multiply = tool({
  description: "两个数字相乘",
  args: {
    a: tool.schema.number().describe("第一个数字"),
    b: tool.schema.number().describe("第二个数字"),
  },
  async execute(args) {
    return args.a * args.b
  },
})
```

### 4. 多语言支持模板
#### Python 工具示例
```python
# .opencode/tool/add.py
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
print(a + b)
```

```typescript
// .opencode/tool/python-add.ts
import { tool } from "@opencode-ai/plugin"

export default tool({
  description: "使用 Python 将两个数字相加",
  args: {
    a: tool.schema.number().describe("第一个数字"),
    b: tool.schema.number().describe("第二个数字"),
  },
  async execute(args) {
    const result = await Bun.$`python3 .opencode/tool/add.py ${args.a} ${args.b}`.text()
    return result.trim()
  },
})
```

### 5. 参数定义指南
使用 Zod 类型系统定义参数：
```typescript
args: {
  query: tool.schema.string().describe("SQL 查询语句"),
  timeout: tool.schema.number().min(1).max(300).describe("超时时间（秒）"),
  verbose: tool.schema.boolean().describe("是否显示详细输出")
}
```

### 6. 上下文访问
```typescript
async execute(args, context) {
  const { agent, sessionID, messageID, workingDirectory } = context
  // 使用上下文信息
}
```

## 最佳实践
1. **命名规范**：工具文件名应反映功能，使用小写字母和连字符
2. **错误处理**：在 execute 函数中添加适当的错误处理
3. **安全性**：验证输入参数，避免命令注入
4. **文档化**：为每个参数提供清晰的描述
5. **测试**：创建简单的测试用例验证工具功能

## 示例：创建一个文件搜索工具
```typescript
// .opencode/tool/file-search.ts
import { tool } from "@opencode-ai/plugin"
import { execSync } from 'child_process'

export default tool({
  description: "在指定目录中搜索文件",
  args: {
    pattern: tool.schema.string().describe("文件名模式，如 *.js"),
    directory: tool.schema.string().default(".").describe("搜索目录，默认为当前目录")
  },
  async execute(args) {
    try {
      const command = `find ${args.directory} -name "${args.pattern}"`;
      const result = execSync(command, { encoding: 'utf8' });
      return result.trim() || "未找到匹配的文件";
    } catch (error) {
      return `搜索出错: ${error.message}`;
    }
  },
})
```

## 快速开始步骤
1. 使用脚本初始化工具：
   ```bash
   python ~/.config/opencode/skills/tool-creator/scripts/init_tool.py my-tool --language ts
   ```
2. 或手动创建工具文件：`.opencode/tool/[tool-name].ts`
3. 参考模板文件（位于 assets/ 目录）：
   - `assets/template-tool.ts` - TypeScript 工具模板
   - `assets/template-python-tool.py` - Python 工具模板
4. 查阅参考文档（位于 references/ 目录）：
   - `references/tool-schema-reference.md` - 参数类型和 Zod 验证参考
   - `references/context-reference.md` - 上下文信息和使用指南
5. 测试工具功能
6. 在 opencode 中使用新工具