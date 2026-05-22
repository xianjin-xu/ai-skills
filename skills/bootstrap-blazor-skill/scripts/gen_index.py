#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 references/index.md 组件索引文件"""

import os
import re
from pathlib import Path

OUTPUT_DIR = Path(r"d:\WorkSpace\DotnetProject\bootstrap-blazor-skill\references\components")

CATEGORIES = {
    "基础组件": ["Alert", "Badge", "Button", "Card", "Divider", "Icon", "Tag", "Title", "Block", "GroupBox", "Label"],
    "布局": ["Layout", "Row", "Stack", "Affix", "Anchor", "AnchorLink", "GoTop", "Footer", "Responsive", "Split", "Transition"],
    "表单输入": ["AutoComplete", "AutoFill", "Cascader", "Checkbox", "ClockPicker", "ColorPicker", "DateTimePicker", "DateTimeRange", "EditorForm", "Input", "InputNumber", "IpAddress", "Radio", "Rate", "Select", "Segmented", "Slider", "Switch", "Textarea", "TimePicker", "Toggle", "Transfer", "Upload"],
    "表单验证": ["Validate", "ValidateForm"],
    "导航": ["Breadcrumb", "Menu", "Nav", "Navbar", "Pagination", "RibbonTab", "Step", "Tab", "Toolbar"],
    "数据展示": ["Avatar", "Calendar", "Carousel", "Circle", "CountUp", "Display", "Empty", "FlipClock", "ImageViewer", "Light", "ListView", "Marquee", "Progress", "Skeleton", "Spinner", "Table", "Timeline", "Timer", "Tree", "TreeView", "Typed", "Watermark"],
    "反馈": ["Console", "Dialog", "Drawer", "Dropdown", "DropdownWidget", "Message", "Modal", "Notification", "Popover", "SweetAlert", "Toast", "Tooltip"],
    "媒体": ["Camera", "Handwritten", "IFrame", "ImagePreviewer", "Speech", "WebSpeech"],
    "工具": ["Ajax", "AutoRedirect", "Captcha", "Clipboard", "Collapse", "ConnectionHub", "ContextMenu", "Download", "DragDrap", "ErrorLogger", "FileIcon", "Filters", "FullScreen", "Geolocation", "HtmlTag", "IPLocator", "LazyLoad", "ListGroup", "Logout", "Mask", "NetworkMonitor", "Print", "QueryBuilder", "Reconnector", "Redirect", "Repeater", "Scroll", "Search", "SearchForm", "SortableList", "ThemeProvider", "Waterfall"],
}


def to_hyphen(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()


def main():
    # 获取所有已生成的 md 文件
    existing = set()
    for f in OUTPUT_DIR.glob("*.md"):
        existing.add(f.stem)

    lines = []
    lines.append("# BootstrapBlazor 组件索引\n")
    lines.append("> 本文档基于 BootstrapBlazor 本地源码自动生成，共收录 112 个组件的详细 API 文档和代码示例。\n")
    lines.append("> 在线演示站点: [https://www.blazor.zone](https://www.blazor.zone)\n")

    total = 0
    for cat, components in CATEGORIES.items():
        lines.append(f"## {cat}\n")
        lines.append("| 组件 | 说明 | 在线演示 |")
        lines.append("|------|------|----------|")
        cat_count = 0
        for comp in components:
            hyphen = to_hyphen(comp)
            if hyphen in existing:
                doc_link = f"[{comp}](./components/{hyphen}.md)"
                demo_link = f"[演示](https://www.blazor.zone/{hyphen})"
                # 读取文档获取描述
                doc_path = OUTPUT_DIR / f"{hyphen}.md"
                desc = ""
                try:
                    content = doc_path.read_text(encoding="utf-8")
                    # 提取概述
                    m = re.search(r'## 概述\n\n(.+?)(?:\n|$)', content)
                    if m:
                        desc = m.group(1).strip()
                except:
                    pass
                lines.append(f"| {doc_link} | {desc} | {demo_link} |")
                cat_count += 1
        total += cat_count
        lines.append(f"\n> 共 {cat_count} 个组件\n")

    lines.insert(2, f"> **总计 {total} 个组件**\n")

    index_path = Path(r"d:\WorkSpace\DotnetProject\bootstrap-blazor-skill\references\index.md")
    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ 生成索引: {index_path}")
    print(f"   收录 {total} 个组件，{len(CATEGORIES)} 个分类")


if __name__ == "__main__":
    main()
