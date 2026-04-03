#!/usr/bin/env python3
"""
验证 tool-creator 技能结构是否符合规范
"""

import os
import sys

def validate_skill_structure():
    """验证技能结构"""
    
    # 检查 SKILL.md 文件
    skill_md = 'SKILL.md'
    if not os.path.exists(skill_md):
        print(f"❌ 缺少 {skill_md} 文件")
        return False
    
    # 检查 YAML frontmatter
    with open(skill_md, 'r') as f:
        content = f.read()
        if not content.startswith('---'):
            print(f"❌ {skill_md} 缺少 YAML frontmatter")
            return False
    
    # 检查必要目录
    required_dirs = ['scripts', 'references', 'assets']
    for directory in required_dirs:
        if not os.path.exists(directory):
            print(f"⚠️  目录 {directory}/ 不存在（可选）")
    
    # 检查 scripts 目录内容
    if os.path.exists('scripts'):
        scripts = [f for f in os.listdir('scripts') if f.endswith('.py')]
        if not scripts:
            print(f"⚠️  scripts/ 目录为空（建议添加初始化脚本）")
    
    # 检查 references 目录内容
    if os.path.exists('references'):
        refs = [f for f in os.listdir('references') if f.endswith('.md')]
        if not refs:
            print(f"⚠️  references/ 目录为空（建议添加参考文档）")
    
    # 检查 assets 目录内容
    if os.path.exists('assets'):
        assets = [f for f in os.listdir('assets') if f.endswith(('.ts', '.py'))]
        if not assets:
            print(f"⚠️  assets/ 目录为空（建议添加模板文件）")
    
    print("✅ 技能结构验证完成")
    return True

if __name__ == "__main__":
    success = validate_skill_structure()
    sys.exit(0 if success else 1)