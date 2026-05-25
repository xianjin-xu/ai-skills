#!/usr/bin/env python3
"""
批量重命名 references/components/ 目录中的组件文件为 PascalCase
将 component-name.md 重命名为 ComponentName.md
"""

import os
import re
from pathlib import Path

# 组件目录
COMPONENTS_DIR = Path(__file__).parent.parent / "references" / "components"

def to_pascal_case(name: str) -> str:
    """将 kebab-case 或 lowercase 转换为 PascalCase"""
    # 先按 - 分割
    parts = name.replace('.md', '').split('-')
    # 每个部分首字母大写
    result = ''.join(part.capitalize() for part in parts)
    return result + '.md'

def main():
    print(f"扫描目录: {COMPONENTS_DIR}")
    
    # 获取所有 .md 文件
    md_files = list(COMPONENTS_DIR.glob("*.md"))
    print(f"找到 {len(md_files)} 个 .md 文件")
    
    renamed_count = 0
    skipped_count = 0
    
    for file_path in md_files:
        file_name = file_path.name
        
        # 跳过已经是 PascalCase 的文件 (检查是否有小写字母后跟大写字母)
        if file_name[0].isupper() and '-' not in file_name:
            print(f"  跳过 (已是大写): {file_name}")
            skipped_count += 1
            continue
        
        # 转换为 PascalCase
        new_name = to_pascal_case(file_name)
        new_path = COMPONENTS_DIR / new_name
        
        # 检查目标文件是否已存在
        if new_path.exists():
            print(f"  跳过 (目标已存在): {file_name} -> {new_name}")
            skipped_count += 1
            continue
        
        # 重命名
        try:
            file_path.rename(new_path)
            print(f"  ✓ 重命名: {file_name} -> {new_name}")
            renamed_count += 1
        except Exception as e:
            print(f"  ✗ 错误: {file_name} -> {new_name} ({e})")
    
    print(f"\n完成! 重命名: {renamed_count}, 跳过: {skipped_count}")

if __name__ == "__main__":
    main()
