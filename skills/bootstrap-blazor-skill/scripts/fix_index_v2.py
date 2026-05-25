#!/usr/bin/env python3
"""
修正 index.md 中的组件引用
1. 将所有文件名改为 PascalCase
2. 添加缺失的组件引用
3. 删除多余的引用 (SearchForm)
"""

import re
from pathlib import Path

# 配置路径
SCRIPT_DIR = Path(__file__).parent
COMPONENTS_DIR = SCRIPT_DIR.parent / "references" / "components"
INDEX_FILE = SCRIPT_DIR.parent / "references" / "index.md"

# 从 index.md 中提取所有组件引用
def extract_components_from_index(content):
    """提取 index.md 中的所有组件引用"""
    # 匹配格式: | [Name](./components/File.md) | Description | [Demo](url) |
    pattern = r'\| \[([^\]]+)\]\(\.\/components\/([^\)]+)\)'
    matches = re.findall(pattern, content)
    return matches

# 读取实际文件列表
def get_actual_files():
    """获取 components 目录中实际存在的 .md 文件"""
    files = [f.name for f in COMPONENTS_DIR.glob("*.md")]
    return sorted(files)

# 主函数
def main():
    print(f"组件目录: {COMPONENTS_DIR}")
    print(f"索引文件: {INDEX_FILE}")
    
    # 1. 读取 index.md 内容
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 2. 提取当前引用
    current_refs = extract_components_from_index(content)
    print(f"\n当前索引引用数: {len(current_refs)}")
    
    # 3. 获取实际文件列表
    actual_files = get_actual_files()
    print(f"实际文件数: {len(actual_files)}")
    
    # 4. 构建正确引用列表
    # 先处理当前引用：修正文件名大小写
    corrected_refs = []
    seen_files = set()
    
    for name, filename in current_refs:
        # 检查文件是否还存在
        if filename in actual_files:
            # 文件存在，使用正确的 PascalCase 文件名
            corrected_refs.append((name, filename))
            seen_files.add(filename)
        else:
            # 文件不存在，跳过（如 SearchForm.md）
            print(f"跳过不存在的文件: {filename}")
    
    # 5. 添加缺失的文件
    missing_files = set(actual_files) - seen_files
    print(f"\n缺失的文件数: {len(missing_files)}")
    for f in sorted(missing_files):
        # 从文件名推断组件名（去掉 .md）
        component_name = f[:-3]  # 去掉 .md
        corrected_refs.append((component_name, f))
        print(f"添加缺失文件: {f}")
    
    # 6. 重新组织 index.md 内容
    # 这里简化：只输出修正后的引用列表，让用户手动更新
    print(f"\n=== 修正后的引用列表 ===")
    print(f"总数: {len(corrected_refs)}")
    for name, filename in corrected_refs:
        print(f"| [{name}](./components/{filename}) | ... | ... |")
    
    print(f"\n=== 下一步 ===")
    print(f"由于 index.md 结构复杂，建议：")
    print(f"1. 备份当前 index.md")
    print(f"2. 手动更新 index.md 中的引用")
    print(f"3. 或者让我直接重写整个 index.md")

if __name__ == '__main__':
    main()
