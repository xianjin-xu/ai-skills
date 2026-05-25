#!/bin/bash
# 批量重命名组件文件为 PascalCase
# 使用方法: bash rename_components.sh

COMP_DIR="d:/WorkSpace/DotnetProject/ai-skills/skills/bootstrap-blazor-skill/references/components"

cd "$COMP_DIR" || exit 1

echo "开始扫描小写文件..."
count=0

for file in *.md; do
    # 跳过已经是 PascalCase 的（首字母大写且无 -）
    if [[ "$file" =~ ^[A-Z] && "$file" != *-* ]]; then
        # echo "跳过: $file"
        continue
    fi
    
    # 获取文件名（无 .md）
    name="${file%.md}"
    
    # 转换为 PascalCase: 按 - 分割，每个部分首字母大写
    IFS='-'
    read -ra parts <<< "$name"
    new_name=""
    for part in "${parts[@]}"; do
        # 首字母大写
        part="$(echo "${part:0:1}" | tr 'a-z' 'A-Z')${part:1}"
        new_name="${new_name}${part}"
    done
    
    new_file="${new_name}.md"
    
    # 检查目标是否已存在
    if [[ -f "$new_file" ]]; then
        echo "跳过（目标已存在）: $file -> $new_file"
        continue
    fi
    
    # 重命名
    mv "$file" "$new_file" 2>/dev/null && echo "重命名: $file -> $new_file" || echo "失败: $file"
    ((count++))
done

echo "完成！共处理 $count 个文件"
