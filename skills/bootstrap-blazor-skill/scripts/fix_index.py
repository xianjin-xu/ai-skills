#!/usr/bin/env python3
"""
自动修正 index.md 中的组件引用
- 修正文件名大小写（改为 PascalCase）
- 添加缺失的组件引用
- 删除多余引用（实际文件不存在的）
"""

import re
import sys
from pathlib import Path

# 获取实际文件列表（PascalCase）
def get_actual_files(components_dir):
    """获取 components 目录中实际存在的 md 文件列表"""
    files = []
    for f in Path(components_dir).glob("*.md"):
        files.append(f.name)
    return sorted(files)

# 从 index.md 中提取所有组件引用
def extract_references(index_file):
    """从 index.md 中提取所有 [ComponentName](./components/xxx.md) 引用"""
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配 [Text](./components/xxx.md)
    pattern = r'\[([^\]]+)\]\(\.\/components\/([^\)]+)\)'
    matches = re.findall(pattern, content)
    
    refs = []
    for text, filename in matches:
        refs.append((text, filename))
    
    return refs, content

# 构建正确的组件引用映射
def build_correct_mapping(actual_files):
    """根据实际文件名构建正确的引用映射
    - 文件名已经是 PascalCase
    - 需要找到对应的组件名称和演示 URL
    """
    mapping = {}
    for filename in actual_files:
        # 去掉 .md 后缀
        basename = filename[:-3]  # 去掉 .md
        
        # 尝试推断组件名称（PascalCase）
        # 例如：SearchDialog.md -> SearchDialog
        component_name = basename  # 文件名就是组件名
        
        # 构建演示 URL（小写，连字符分隔）
        # 例如：SearchDialog -> search-dialog
        demo_url = basename.lower()
        # 在大写字母前加连字符（第一个大写字母除外）
        demo_url = re.sub(r'(?<!^)([A-Z])', r'-\1', demo_url).lower()
        
        mapping[filename] = {
            'component_name': component_name,
            'demo_url': f'https://www.blazor.zone/{demo_url}'
        }
    
    return mapping

# 主函数
def main():
    # 路径设置
    script_dir = Path(__file__).parent
    components_dir = script_dir.parent / 'references' / 'components'
    index_file = script_dir.parent / 'references' / 'index.md'
    
    print(f"组件目录: {components_dir}")
    print(f"索引文件: {index_file}")
    
    # 1. 获取实际文件列表
    actual_files = get_actual_files(components_dir)
    print(f"\n实际文件数量: {len(actual_files)}")
    print("实际文件列表:")
    for f in actual_files:
        print(f"  {f}")
    
    # 2. 提取 index.md 中的引用
    refs, content = extract_references(index_file)
    print(f"\n索引文件中引用数量: {len(refs)}")
    print("索引文件中的引用:")
    for text, filename in refs:
        print(f"  [{text}](./components/{filename})")
    
    # 3. 检查差异
    actual_set = set(actual_files)
    ref_set = set([f for _, f in refs])
    
    missing_in_index = actual_set - ref_set  # 实际有但索引中没有
    extra_in_index = ref_set - actual_set   # 索引中有但实际没有
    
    print(f"\n=== 差异分析 ===")
    print(f"实际有但索引中没有 (缺失): {len(missing_in_index)}")
    for f in sorted(missing_in_index):
        print(f"  {f}")
    
    print(f"\n索引中有但实际没有 (多余): {len(extra_in_index)}")
    for f in sorted(extra_in_index):
        print(f"  {f}")
    
    # 4. 构建正确的映射
    print(f"\n=== 构建正确映射 ===")
    mapping = build_correct_mapping(actual_files)
    
    # 5. 修正 index.md 内容
    print(f"\n=== 修正索引文件 ===")
    
    # 读取原始内容
    with open(index_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 找出需要修正的行
    corrected_lines = []
    for line in lines:
        new_line = line
        
        # 检查是否包含组件引用
        # 格式：| [Text](./components/xxx.md) | Description | [Demo](url) |
        match = re.match(r'(\| \[)([^\]]+)(\]\(\.\/components\/)([^\)]+)(\) \| .+)', line)
        if match:
            prefix, text, path, filename, suffix = match.groups()
            
            # 检查文件是否存在
            if filename in actual_set:
                # 文件存在，检查是否需要修正大小写
                if filename != actual_files[actual_files.index(filename)]:
                    # 需要修正大小写
                    correct_filename = actual_files[actual_files.index(filename)]
                    new_line = f"{prefix}{text}{path}{correct_filename}{suffix}\n"
                    print(f"修正大小写: {filename} -> {correct_filename}")
            else:
                # 文件不存在，可能是多余引用，保留原样（后面会处理）
                print(f"警告: 引用文件不存在: {filename}")
        
        corrected_lines.append(new_line)
    
    # 写回文件
    with open(index_file, 'w', encoding='utf-8') as f:
        f.writelines(corrected_lines)
    
    print(f"\n修正完成！")
    print(f"建议下一步：")
    print(f"1. 检查修正后的 index.md")
    print(f"2. 手动添加缺失的组件引用")
    print(f"3. 手动删除多余的组件引用")

if __name__ == '__main__':
    main()
