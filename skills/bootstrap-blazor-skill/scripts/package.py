#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""打包 bootstrap-blazor skill"""
import zipfile
import os
from pathlib import Path

base = Path(r"d:/WorkSpace/DotnetProject/bootstrap-blazor-skill")
output = base.parent / "bootstrap-blazor.skill"

exclude = {".codebuddy", ".playwright-cli", ".git"}

with zipfile.ZipFile(str(output), "w", zipfile.ZIP_DEFLATED) as zf:
    count = 0
    for root, dirs, files in os.walk(str(base)):
        rel = os.path.relpath(root, str(base))
        parts = set(rel.split(os.sep))
        if parts & exclude:
            continue
        for f in files:
            if f.endswith((".yaml", ".yml")):
                continue
            fp = Path(root) / f
            an = str(Path(rel) / f) if rel != "." else f
            zf.write(str(fp), an)
            count += 1

size_mb = output.stat().st_size / 1024 / 1024
print(f"Packaged: {output}")
print(f"Size: {size_mb:.2f} MB, Files: {count}")
