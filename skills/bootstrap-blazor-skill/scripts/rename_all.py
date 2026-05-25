#!/usr/bin/env python3
"""
批量重命名 components/ 目录中所有小写的 .md 文件为 PascalCase
输出日志到 rename_log.txt
"""

import os
import sys
from pathlib import Path

COMP_DIR = Path(r"d:\WorkSpace\DotnetProject\ai-skills\skills\bootstrap-blazor-skill\references\components")

def log(msg):
    print(msg, flush=True)
    with open("rename_log.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def to_pascal(name_no_ext):
    """kebab-case 或 lowercase 转 PascalCase"""
    parts = name_no_ext.split("-")
    result = "".join(p.capitalize() for p in parts)
    return result

def main():
    log(f"开始扫描: {COMP_DIR}")
    all_files = list(COMP_DIR.glob("*.md"))
    log(f"总文件数: {len(all_files)}")
    
    lower_files = [f for f in all_files if f.name[0].islower() or "-" in f.name]
    log(f"需要重命名: {len(lower_files)} 个")
    
    renamed = 0
    skipped = 0
    
    for f in lower_files:
        old_name = f.name  # e.g. "input-number.md"
        name_no_ext = old_name[:-3]  # remove .md
        new_name = to_pascal(name_no_ext) + ".md"
        new_path = COMP_DIR / new_name
        
        if new_path.exists():
            log(f"  跳过（目标存在）: {old_name} -> {new_name}")
            skipped += 1
            continue
        
        try:
            f.rename(new_path)
            log(f"  ✓ {old_name} -> {new_name}")
            renamed += 1
        except Exception as e:
            log(f"  ✗ 错误: {old_name} -> {new_name} ({e})")
    
    log(f"\n完成! 重命名: {renamed}, 跳过: {skipped}")

if __name__ == "__main__":
    main()
