// .opencode/tool/example-tool.ts
import { tool } from "@opencode-ai/plugin"

export default tool({
  description: "示例自定义工具 - 演示基本用法",
  args: {
    message: tool.schema.string().describe("要返回的消息"),
    count: tool.schema.number().int().min(1).max(100).default(1).describe("重复次数")
  },
  async execute(args) {
    // 简单的业务逻辑
    const result = Array(args.count).fill(args.message).join("\n");
    return result;
  },
})