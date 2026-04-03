# Context 上下文参考

## 可用的上下文信息
工具的 `execute` 函数可以接收 `context` 参数，包含以下信息：

```typescript
interface Context {
  agent: string;           // 当前使用的 agent 名称
  sessionID: string;       // 当前会话 ID
  messageID: string;       // 当前消息 ID
  workingDirectory: string; // 当前工作目录
  config: Record<string, any>; // opencode 配置
}
```

## 使用示例
```typescript
async execute(args, context) {
  const { agent, sessionID, workingDirectory } = context;
  
  console.log(`Agent: ${agent}`);
  console.log(`Session: ${sessionID}`);
  console.log(`Working directory: ${workingDirectory}`);
  
  // 根据工作目录执行不同操作
  if (workingDirectory.includes('project')) {
    return "在项目目录中执行";
  }
  
  return "在其他目录中执行";
}
```

## 实际应用场景
- **路径处理**：使用 `workingDirectory` 构建相对路径
- **会话跟踪**：使用 `sessionID` 记录日志或状态
- **代理识别**：根据 `agent` 提供不同的功能实现
- **配置访问**：从 `config` 中读取用户设置