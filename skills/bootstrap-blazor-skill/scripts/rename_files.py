#!/usr/bin/env python3
"""
重命名文件脚本：将 .temp/scraped/ 和 references/components/ 中的文件从 URL 名称重命名为组件名称
"""
import sys
from pathlib import Path

# 组件名称到 URL 的映射（从 scrape_bootstrap_blazor_v2.py 复制）
COMPONENT_MAPPING = {
    "Affix": "affix",
    "Alert": "alert",
    "Anchor": "anchor",
    "AnchorLink": "anchor-link",
    "AutoComplete": "auto-complete",
    "AutoFill": "auto-fill",
    "Avatar": "avatar",
    "Badge": "badge",
    "Breadcrumb": "breadcrumb",
    "Button": "button",
    "Calendar": "calendar",
    "Camera": "camera",
    "Captcha": "captcha",
    "Card": "card",
    "Carousel": "carousel",
    "Cascader": "cascader",
    "Checkbox": "checkbox",
    "Circle": "circle",
    "ClockPicker": "clock-picker",
    "Collapse": "collapse",
    "ColorPicker": "color-picker",
    "Console": "console",
    "ContextMenu": "context-menu",
    "CountUp": "count-up",
    "DateTimePicker": "datetime-picker",
    "DateTimeRange": "date-time-range",
    "Dialog": "dialog",
    "Display": "display",
    "Divider": "divider",
    "DragDrap": "drag-drap",
    "Drawer": "drawer",
    "Dropdown": "dropdown",
    "DropdownWidget": "dropdown-widget",
    "EditorForm": "editor-form",
    "Empty": "empty",
    "FileIcon": "file-icon",
    "Filters": "filters",
    "FlipClock": "flip-clock",
    "Footer": "footer",
    "FullScreen": "fullscreen",
    "GoTop": "go-top",
    "GroupBox": "group-box",
    "Handwritten": "handwritten",
    "HtmlTag": "html-tag",
    "Icon": "icon",
    "IFrame": "i-frame",
    "ImagePreviewer": "image-previewer",
    "ImageViewer": "image-viewer",
    "Input": "input",
    "InputNumber": "input-number",
    "IpAddress": "ip-address",
    "Label": "label",
    "Layout": "layout",
    "Light": "light",
    "ListGroup": "list-group",
    "ListView": "list-view",
    "Logout": "logout",
    "Marquee": "marquee",
    "Mask": "mask",
    "Menu": "menu",
    "Message": "message",
    "Modal": "modal",
    "Nav": "nav",
    "Navbar": "navbar",
    "NetworkMonitor": "network-monitor",
    "Pagination": "pagination",
    "Popover": "popover",
    "Print": "print",
    "Progress": "progress",
    "QueryBuilder": "query-builder",
    "Radio": "radio",
    "Rate": "rate",
    "Reconnector": "reconnector",
    "Repeater": "repeater",
    "RibbonTab": "ribbon-tab",
    "Row": "row",
    "Scroll": "scroll",
    "Search": "search",
    "SearchForm": "search-form",
    "Segmented": "segmented",
    "Select": "select",
    "Skeleton": "skeleton",
    "Slider": "slider",
    "Speech": "speech",
    "Spinner": "spinner",
    "Split": "split",
    "Stack": "stack",
    "Step": "step",
    "SweetAlert": "sweet-alert",
    "Switch": "switch",
    "Tab": "tab",
    "Table": "table",
    "Tag": "tag",
    "Textarea": "textarea",
    "ThemeProvider": "theme-provider",
    "Timeline": "timeline",
    "TimePicker": "time-picker",
    "Timer": "timer",
    "Toast": "toast",
    "Toggle": "toggle",
    "Toolbar": "toolbar",
    "Tooltip": "tooltip",
    "Transfer": "transfer",
    "Transition": "transition",
    "Tree": "tree",
    "TreeView": "tree-view",
    "Typed": "typed",
    "Upload": "upload",
    "ValidateForm": "validate-form",
    "Waterfall": "waterfall",
    "Watermark": "watermark",
}

def rename_scraped_files():
    """重命名 .temp/scraped/ 目录中的文件"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent.parent
    scraped_dir = project_root / ".temp" / "scraped"
    
    if not scraped_dir.exists():
        print(f"❌ 目录不存在: {scraped_dir}")
        return
    
    print(f"📁 处理目录: {scraped_dir}")
    
    renamed_count = 0
    for component_name, url_name in COMPONENT_MAPPING.items():
        # 检查旧文件（URL 名称）是否存在
        old_txt = scraped_dir / f"{url_name}.txt"
        old_html = scraped_dir / f"{url_name}.html"
        
        # 新文件名称（组件名称）
        new_txt = scraped_dir / f"{component_name}.txt"
        new_html = scraped_dir / f"{component_name}.html"
        
        # 重命名 .txt 文件
        if old_txt.exists() and not new_txt.exists():
            old_txt.rename(new_txt)
            print(f"  ✓ {url_name}.txt -> {component_name}.txt")
            renamed_count += 1
        elif old_txt.exists() and new_txt.exists():
            print(f"  ⚠️ 目标文件已存在，跳过: {component_name}.txt")
        
        # 重命名 .html 文件
        if old_html.exists() and not new_html.exists():
            old_html.rename(new_html)
            print(f"  ✓ {url_name}.html -> {component_name}.html")
            renamed_count += 1
        elif old_html.exists() and new_html.exists():
            print(f"  ⚠️ 目标文件已存在，跳过: {component_name}.html")
    
    print(f"\n✅ 完成！重命名 {renamed_count} 个文件")

def rename_components_docs():
    """重命名 references/components/ 目录中的文件"""
    script_dir = Path(__file__).parent
    components_dir = script_dir.parent / "references" / "components"
    
    if not components_dir.exists():
        print(f"❌ 目录不存在: {components_dir}")
        return
    
    print(f"📁 处理目录: {components_dir}")
    
    # 获取当前目录中的所有 .md 文件
    current_files = list(components_dir.glob("*.md"))
    
    renamed_count = 0
    for component_name in COMPONENT_MAPPING.keys():
        # 尝试找到对应的当前文件（可能是 URL 名称或错误的组件名称）
        found = False
        
        # 尝试几种可能的当前文件名
        possible_names = [
            f"{COMPONENT_MAPPING[component_name]}.md",  # URL 名称
            f"{component_name.lower()}.md",  # 小写组件名
            f"{component_name}.md",  # 正确名称（可能已存在）
        ]
        
        for possible_name in possible_names:
            current_file = components_dir / possible_name
            if current_file.exists():
                # 重命名为正确的组件名称
                new_file = components_dir / f"{component_name}.md"
                if current_file != new_file and not new_file.exists():
                    current_file.rename(new_file)
                    print(f"  ✓ {possible_name} -> {component_name}.md")
                    renamed_count += 1
                    found = True
                    break
                elif current_file == new_file:
                    # 文件名已经正确
                    found = True
                    break
        
        if not found:
            print(f"  ❌ 未找到文件: {component_name}.md (可能的名称: {possible_names})")
    
    print(f"\n✅ 完成！重命名 {renamed_count} 个文件")

if __name__ == "__main__":
    print("=" * 70)
    print("重命名文件脚本")
    print("=" * 70)
    
    print("\n1. 重命名 .temp/scraped/ 目录中的文件...")
    rename_scraped_files()
    
    print("\n2. 重命名 references/components/ 目录中的文件...")
    rename_components_docs()
    
    print("\n🎉 全部完成！")
