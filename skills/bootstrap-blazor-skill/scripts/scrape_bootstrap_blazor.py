#!/usr/bin/env python3
"""
Bootstrap Blazor 组件文档自动抓取脚本
使用 Playwright 抓取官方文档页面，提取组件参数表格和代码示例
不带任何参数则将抓取所有组件，或指定参数则抓取指定组件
"""

import asyncio
import json
import sys
from pathlib import Path
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

# 组件名称到 URL 的映射
# 组件名称使用 PascalCase（如 DateTimePicker），URL 使用 kebab-case（如 date-time-picker）
# 数据来源：component-url-mapping.md
COMPONENT_MAPPING = {
    "Affix": "affix",
    "Alert": "alert",
    "Anchor": "anchor",
    "AnchorLink": "anchor-link",
    "AutoComplete": "auto-complete",
    "AutoFill": "auto-fill",
    "Avatar": "avatar",
    "AvatarUpload":"upload-avatar",
    "Badge": "badge",
    "Breadcrumb": "breadcrumb",
    "Button": "button",
    "ButtonUpload":"upload-button",
    "Calendar": "calendar",
    "Camera": "camera",
    "Captcha": "captcha",
    "Card": "card",
    "CardUpload":"upload-card",
    "Carousel": "carousel",
    "Cascader": "cascader",
    "Checkbox": "checkbox",
    "CheckboxList":"checkbox-list",
    "Circle": "circle",
    "ClockPicker": "clock-picker",
    "Collapse": "collapse",
    "ColorPicker": "color-picker",
    "Console": "console",
    "ContextMenu": "context-menu",
    "CountUp": "count-up",
    "DateTimePicker": "datetime-picker",
    "DateTimeRange": "datetime-range",
    "Dialog": "dialog",
    "Display": "display",
    "Divider": "divider",
    "DragDrap": "drag-drap",
    "Drawer": "drawer",
    "Dropdown": "dropdown",
    "DropdownWidget": "dropdown-widget",
    "Editor": "editor",
    "EditorForm": "editor-form",
    "Empty": "empty",
    "ExportPdfButton":"export-pdf-button",
    "FileIcon": "file-icon",
    "Filters": "filters",
    "FlipClock": "flip-clock",
    "FloatingLabel":"floating-label",
    "Footer": "footer",
    "FullScreen": "fullscreen",
    "Gantt": "gantt",
    "GoTop": "go-top",
    "GroupBox": "group-box",
    "Handwritten": "handwritten",
    "HtmlTag": "html-tag",
    "Icon": "icon",
    "IFrame": "iframe",
    "ImageCropper": "image-cropper",
    "ImageViewer": "image-viewer",
    "Input": "input",
    "InputNumber": "input-number",
    "InputGroup": "input-group",
    "IpAddress": "ip",
    "JitViewer": "jit-viewer",
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
    "MindMap": "mind-map",
    "Mermaid": "mermaid",
    "ModalDialog": "modal",
    "MultiSelect": "multi-select",
    "Nav": "nav",
    "Navbar": "navbar",
    "NetworkMonitor": "network-monitor",
    "OfficeViewer": "office-viewer",
    "Pagination": "pagination",
    "PdfReader": "pdf-reader",
    "PdfViewer":"pdf-viewer",
    "Player":"player",
    "PopConfirm": "pop-confirm",
    "Popover": "popover",
    "Print": "print",
    "Progress": "progress",
    "PulseButton":"pulse-button",
    "QRCode": "qr-code",
    "QueryBuilder": "query-builder",
    "Radio": "radio",
    "Rate": "rate",
    "Reconnector": "reconnector",
    "Repeater": "repeater",
    "RibbonTab": "ribbon-tab",
    "Row": "row",
    "Scroll": "scroll",
    "Search": "search",
    "SearchDialog": "search-dialog",
    "SearchForm": "search-form",
    "Segmented": "segmented",
    "Select": "select",
    "SelectObject": "select-object",
    "SelectTable": "select-table",
    "SelectTree": "select-tree",
    "SignaturePad": "signature-pad",
    "Skeleton": "skeleton",
    "Slider": "slider",
    "Speech": "speech",
    "Spinner": "spinner",
    "Split": "split",
    "Stack": "stack",
    "Step": "step",
    "SweetAlert": "sweet-alert",
    "Switch": "switch",
    "SwitchButton": "switch-button",
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
    "UniverSheet":"univer-sheet",
    "ValidateForm": "validate-form",
    "VideoPlayer": "video-player",
    "Waterfall": "waterfall",
    "Watermark": "watermark",
}

# 组件名称列表（PascalCase）
COMPONENTS = list(COMPONENT_MAPPING.keys())

BASE_URL = "https://www.blazor.zone"
SCRIPT_DIR = Path(__file__).parent
# 抓取结果保存到项目根目录的 .temp/scraped/（临时文件，不提交到 git）
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent  # ai-skills/
OUTPUT_DIR = PROJECT_ROOT / ".temp" / "scraped"  # 抓取结果保存目录


async def scrape_component(page, component_name: str, max_retries: int = 2) -> dict:
    """抓取单个组件的文档内容（带重试）"""
    # 使用 URL 映射构造请求 URL
    url_name = COMPONENT_MAPPING.get(component_name, component_name)
    url = f"{BASE_URL}/{url_name}"
    print(f"  [抓取] {component_name} (URL: {url_name})")
    
    for attempt in range(max_retries + 1):
        try:
            # 导航到页面并等待加载
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            
            # 等待网络空闲（Blazor 通过 WebSocket 加载数据）
            try:
                await page.wait_for_load_state("networkidle", timeout=10000)
            except:
                pass  # 超时也继续
            
            # 额外等待 2 秒确保 Blazor 完全渲染
            await asyncio.sleep(2)
            
            # 提取页面文本内容（尝试多种选择器获取主要内容）
            text_content = await page.evaluate("""() => {
                const selectors = ['main', 'article', '.content', '#content', 'body'];
                for (const sel of selectors) {
                    const el = document.querySelector(sel);
                    if (el && el.innerText && el.innerText.trim().length > 100) {
                        return el.innerText;
                    }
                }
                return document.body.innerText;
            }""")
            
            # 提取页面 HTML
            html_content = await page.content()
            
            print(f"    ✓ 文本: {len(text_content)} 字符, HTML: {len(html_content)} 字符")
            
            return {
                "component": component_name,
                "url": url,
                "text": text_content,
                "html": html_content,
                "success": True
            }
            
        except PlaywrightTimeout as e:
            if attempt < max_retries:
                print(f"    ⚠️ 超时（尝试 {attempt+1}/{max_retries+1}），重试...")
                await asyncio.sleep(2)
                continue
            print(f"    ✗ 超时: {e}")
            return {"component": component_name, "url": url, "error": str(e), "success": False}
        except Exception as e:
            error_msg = str(e)
            # 如果是 "Execution context was destroyed"，可能是页面导航导致，重试
            if "Execution context was destroyed" in error_msg and attempt < max_retries:
                print(f"    ⚠️ 执行上下文销毁（尝试 {attempt+1}/{max_retries+1}），重试...")
                await asyncio.sleep(2)
                continue
            if attempt < max_retries:
                print(f"    ⚠️ 错误: {type(e).__name__}: {e}（尝试 {attempt+1}/{max_retries+1}），重试...")
                await asyncio.sleep(2)
                continue
            print(f"    ✗ 错误: {type(e).__name__}: {e}")
            return {"component": component_name, "url": url, "error": str(e), "success": False}


async def main():
    """主函数"""
    print("=" * 70)
    print("Bootstrap Blazor 组件文档抓取脚本")
    print(f"目标: {len(COMPONENTS)} 个组件")
    print("=" * 70)
    
    # 创建输出目录
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n[目录] 数据将保存到: {OUTPUT_DIR}\n")
    
    # 使用 asyncio.wait_for 设置总体超时（每个组件最多 60 秒）
    async def scrape_with_timeout(page, comp):
        try:
            return await asyncio.wait_for(scrape_component(page, comp), timeout=60.0)
        except asyncio.TimeoutError:
            print(f"    ✗ 总体超时（60秒）")
            # 使用 URL 映射构造正确的 URL
            url_name = COMPONENT_MAPPING.get(comp, comp)
            return {"component": comp, "url": f"{BASE_URL}/{url_name}", "error": "总体超时", "success": False}
    
    results = []
    
    async with async_playwright() as p:
        # 启动浏览器 - 优先使用系统 Edge
        print("[浏览器] 启动中...")
        browser = None
        
        edge_paths = [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        ]
        for edge_path in edge_paths:
            if Path(edge_path).exists():
                print(f"[浏览器] 使用 Edge: {edge_path}")
                browser = await p.chromium.launch(
                    executable_path=edge_path,
                    headless=True,
                    args=['--no-sandbox', '--disable-setuid-sandbox']
                )
                break
        
        if browser is None:
            print("[浏览器] Edge 未找到，使用 Chromium...")
            browser = await p.chromium.launch(
                headless=True,
                args=['--no-sandbox', '--disable-setuid-sandbox']
            )
        
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        
        page = await context.new_page()
        
        # 抓取所有组件
        for i, comp in enumerate(COMPONENTS):
            print(f"\n[{i+1:3d}/{len(COMPONENTS)}] ", end="")
            result = await scrape_with_timeout(page, comp)
            results.append(result)
            
            # 保存文本文件（使用组件名称命名）
            text_file = OUTPUT_DIR / f"{comp}.txt"
            with open(text_file, 'w', encoding='utf-8') as f:
                f.write(result.get("text", result.get("error", "NO DATA")))
            
            # 保存 HTML 文件（使用组件名称命名）
            if result.get("success"):
                html_file = OUTPUT_DIR / f"{comp}.html"
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(result.get("html", ""))
            
            # 避免请求过快
            if i < len(COMPONENTS) - 1:
                await asyncio.sleep(1)  # 增加到 1 秒，避免导航中断
        
        # 关闭浏览器（添加超时保护，避免卡死）
        print(f"\n\n{'='*70}")
        print("[完成] 正在关闭浏览器...")
        try:
            # 使用 asyncio.wait_for 设置 10 秒超时
            await asyncio.wait_for(browser.close(), timeout=10.0)
            print("[完成] 浏览器已关闭")
        except asyncio.TimeoutError:
            print("[警告] 浏览器关闭超时，强制终止进程...")
            # 强制终止浏览器进程
            for proc in browser.contexts:
                for page in proc.pages:
                    try:
                        await page.close()
                    except:
                        pass
            try:
                await browser.close()
            except:
                pass
            print("[完成] 浏览器已强制关闭")
        except Exception as e:
            print(f"[警告] 关闭浏览器时出错: {e}")
    
    # 保存结果摘要（放到抓取数据目录中，不放在 scripts/ 源码目录）
    summary_file = OUTPUT_DIR / "scrape_summary.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    # 统计
    success_count = sum(1 for r in results if r.get("success"))
    print(f"\n✅ 完成！成功: {success_count}/{len(COMPONENTS)}")
    print(f"📁 数据目录: {OUTPUT_DIR}")
    print(f"📊 摘要文件: {summary_file}")
    print("\n正在退出...")
    sys.exit(0)


if __name__ == "__main__":
    try:
        # 支持命令行参数：指定要抓取的组件（不指定则抓取全部）
        # 用法：
        #   python scrape_bootstrap_blazor_v2.py              # 抓取所有组件
        #   python scrape_bootstrap_blazor_v2.py DateTimePicker Button  # 只抓取 DateTimePicker 和 Button（组件名）
        #   python scrape_bootstrap_blazor_v2.py datetime-picker button  # 只抓取 DateTimePicker 和 Button（URL名）
        args = sys.argv[1:]
        if args:
            # 创建反向映射：URL名 -> 组件名
            url_to_component = {v: k for k, v in COMPONENT_MAPPING.items()}
            
            valid_components = []
            for arg in args:
                # 先检查是否是组件名（PascalCase）
                if arg in COMPONENT_MAPPING:
                    valid_components.append(arg)
                # 再检查是否是 URL 名（kebab-case）
                elif arg in url_to_component:
                    valid_components.append(url_to_component[arg])
                else:
                    print(f"❌ 错误：无效的组件名或 URL 名：{arg}")
                    print(f"有效组件名示例：{list(COMPONENT_MAPPING.keys())[:5]}...")
                    print(f"有效 URL 名示例：{list(COMPONENT_MAPPING.values())[:5]}...")
                    sys.exit(1)
            
            print(f"📋 命令行参数：只抓取 {len(valid_components)} 个组件：{valid_components}")
            # 临时修改 COMPONENTS（仅用于本次运行）
            original_components = COMPONENTS.copy()
            COMPONENTS = valid_components
        
        asyncio.run(main())
        
        # 恢复 COMPONENTS（如果有修改）
        if args:
            COMPONENTS = original_components
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ 脚本执行失败: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
