# Tool Schema 参考指南

## Zod 类型系统
工具参数使用 Zod 类型系统进行定义。Zod 是一个 TypeScript 的运行时类型检查库。

### 基本类型
```typescript
// 字符串
tool.schema.string().describe("描述")

// 数字
tool.schema.number().describe("描述")

// 布尔值
tool.schema.boolean().describe("描述")

// 日期
tool.schema.date().describe("描述")
```

### 验证约束
```typescript
// 最小值/最大值
tool.schema.number().min(1).max(100).describe("1-100之间的数字")

// 字符串长度
tool.schema.string().min(3).max(50).describe("3-50个字符")

// 枚举值
tool.schema.enum(['option1', 'option2', 'option3']).describe("选项列表")

// 可选参数
tool.schema.string().optional().describe("可选参数")

// 默认值
tool.schema.number().default(10).describe("默认值为10")
```

### 复杂类型
```typescript
// 对象
tool.schema.object({
  name: tool.schema.string(),
  age: tool.schema.number()
}).describe("用户对象")

// 数组
tool.schema.array(tool.schema.string()).describe("字符串数组")

// 联合类型
tool.schema.union([
  tool.schema.string(),
  tool.schema.number()
]).describe("字符串或数字")
```

## 参数命名最佳实践
- 使用有意义的名称（如 `query`, `timeout`, `verbose`）
- 避免缩写，除非是广泛认可的（如 `id`, `url`）
- 保持一致性（同一项目中相似功能使用相同参数名）

## 错误处理
```typescript
async execute(args) {
  try {
    // 工具逻辑
    return result;
  } catch (error) {
    // 返回用户友好的错误信息
    return `工具执行出错: ${error.message}`;
  }
}
```