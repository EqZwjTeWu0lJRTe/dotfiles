#!/usr/bin/env python3
"""
初始化一个新的自定义工具
使用方法: python init_tool.py <tool_name> [--language ts|py] [--location local|global]
"""

import sys
import os
import argparse
import json

def create_tool_template(tool_name, language='ts', location='local'):
    """创建工具模板文件"""
    
    # 确定工具目录位置
    if location == 'global':
        tool_dir = os.path.expanduser('~/.config/opencode/tool')
    else:
        tool_dir = './.opencode/tool'
    
    # 创建工具目录
    os.makedirs(tool_dir, exist_ok=True)
    
    if language == 'ts':
        # TypeScript 工具模板
        ts_content = f'''// .opencode/tool/{tool_name}.ts
import {{ tool }} from "@opencode-ai/plugin"

export default tool({{
  description: "{tool_name} - 描述工具功能",
  args: {{
    // 添加参数定义
    // param: tool.schema.string().describe("参数描述"),
  }},
  async execute(args) {{
    // 实现工具逻辑
    return "工具 {tool_name} 已创建";
  }},
}})
'''
        
        tool_path = os.path.join(tool_dir, f'{tool_name}.ts')
        with open(tool_path, 'w') as f:
            f.write(ts_content)
            
        print(f"✅ 创建 TypeScript 工具: {tool_path}")
        
    elif language == 'py':
        # Python 脚本模板
        py_content = f'''#!/usr/bin/env python3
# .opencode/tool/{tool_name}.py
import sys

def main():
    # 处理参数
    if len(sys.argv) < 2:
        print("Usage: {tool_name}.py <arg1> [arg2...]")
        sys.exit(1)
    
    args = sys.argv[1:]
    print(f"Python 工具 {tool_name} 接收到参数: {{args}}")
    # 在这里添加你的逻辑
    return f"Python 工具 {tool_name} 执行成功"

if __name__ == "__main__":
    result = main()
    print(result)
'''
        
        script_path = os.path.join(tool_dir, f'{tool_name}.py')
        with open(script_path, 'w') as f:
            f.write(py_content)
        
        # 创建对应的 TypeScript 包装器
        ts_wrapper = f'''// .opencode/tool/{tool_name}-wrapper.ts
import {{ tool }} from "@opencode-ai/plugin"

export default tool({{
  description: "{tool_name} - Python 工具包装器",
  args: {{
    arg1: tool.schema.string().describe("第一个参数"),
    arg2: tool.schema.string().optional().describe("可选的第二个参数"),
  }},
  async execute(args) {{
    const result = await Bun.$`python3 .opencode/tool/{tool_name}.py ${{args.arg1}} ${{args.arg2 || ''}}`.text()
    return result.trim()
  }},
}})
'''
        
        wrapper_path = os.path.join(tool_dir, f'{tool_name}-wrapper.ts')
        with open(wrapper_path, 'w') as f:
            f.write(ts_wrapper)
            
        print(f"✅ 创建 Python 工具: {script_path}")
        print(f"✅ 创建 TypeScript 包装器: {wrapper_path}")

def main():
    parser = argparse.ArgumentParser(description='初始化新的自定义工具')
    parser.add_argument('tool_name', help='工具名称')
    parser.add_argument('--language', choices=['ts', 'py'], default='ts',
                       help='工具语言 (ts=TypeScript, py=Python)')
    parser.add_argument('--location', choices=['local', 'global'], default='local',
                       help='工具位置 (local=.opencode/tool, global=~/.config/opencode/tool)')
    
    args = parser.parse_args()
    
    try:
        create_tool_template(args.tool_name, args.language, args.location)
        print("\n🚀 工具创建完成！")
        print(f"使用方法：在 opencode 中调用 '{args.tool_name}' 工具")
        
    except Exception as e:
        print(f"❌ 创建工具时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()