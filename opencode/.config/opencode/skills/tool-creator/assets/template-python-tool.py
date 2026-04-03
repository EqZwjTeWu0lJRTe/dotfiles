#!/usr/bin/env python3
# .opencode/tool/[tool-name].py
import sys
import json

def main():
    """主函数 - 处理参数并执行业务逻辑"""
    
    # 解析参数
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "需要至少一个参数",
            "usage": "python [tool-name].py <arg1> [arg2...]"
        }))
        sys.exit(1)
    
    args = sys.argv[1:]
    
    try:
        # 在这里添加你的业务逻辑
        result = {
            "status": "success",
            "message": f"Python 工具执行成功，收到 {len(args)} 个参数",
            "arguments": args,
            "timestamp": str(int(time.time()))
        }
        
        print(json.dumps(result))
        
    except Exception as e:
        print(json.dumps({
            "error": str(e),
            "status": "failed"
        }))
        sys.exit(1)

if __name__ == "__main__":
    import time
    main()