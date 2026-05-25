#!/usr/bin/env python3
"""检查小写文件 - 版本2"""
import os
import sys
from pathlib import Path

DIR = Path(r"d:\WorkSpace\DotnetProject\ai-skills\skills\bootstrap-blazor-skill\references\components")

print("开始检查...", flush=True)
all_files = list(DIR.glob("*.md"))
print(f"目录中总共有 {len(all_files)} 个 .md 文件", flush=True)

lower_files = [f.name for f in all_files if f.name[0].islower()]
print(f"其中小写开头的文件有 {len(lower_files)} 个:", flush=True)
for f in sorted(lower_files):
    print(f"  {f}", flush=True)
