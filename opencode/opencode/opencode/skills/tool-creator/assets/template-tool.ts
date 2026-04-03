// .opencode/tool/[tool-name].ts
import { tool } from "@opencode-ai/plugin"

export default tool({
  description: "[工具描述]",
  args: {
    // 参数定义示例：
    // param1: tool.schema.string().describe("参数1描述"),
    // param2: tool.schema.number().min(1).max(100).default(10).describe("参数2描述"),
    // verbose: tool.schema.boolean().default(false).describe("是否显示详细输出"),
  },
  async execute(args, context) {
    try {
      // 工具实现逻辑
      // 可以使用 context 访问会话信息
      // const { workingDirectory } = context;
      
      return "工具执行结果";
    } catch (error) {
      return `错误: ${error.message}`;
    }
  },
})