#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BootstrapBlazor Skill - 文档更新脚本
从本地 BootstrapBlazor 源码 + 抓取的官方文档 生成/更新组件文档到 references/components/ 目录。

用法:
    conda activate py310
    python scripts/update_docs.py              # 更新所有组件
    python scripts/update_docs.py label button  # 只更新 label 和 button 组件

要求:
    - 指定本地 BootstrapBlazor 源代码仓库位置 REPO_ROOT 变量
    - Python 3.10+
    - 已运行 scrape_bootstrap_blazor_v2.py 抓取官方文档到 .temp/scraped/
"""

import json
import os
import re
import sys
import glob
import textwrap
from pathlib import Path
from typing import Optional, List, Dict

# 路径配置
REPO_ROOT = Path(r"D:\WorkSpace\DotnetProject\BootstrapBlazor")
SRC_DIR = REPO_ROOT / "src" / "BootstrapBlazor"
COMPONENTS_DIR = SRC_DIR / "Components"
SERVER_DIR = REPO_ROOT / "src" / "BootstrapBlazor.Server"
SAMPLES_DIR = SERVER_DIR / "Components" / "Samples"
DOCS_JSON = SERVER_DIR / "docs.json"
XML_DOC_PATH = SRC_DIR / "BootstrapBlazor.xml"

# 抓取数据目录（由 scrape_bootstrap_blazor_v2.py 生成）
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent  # ai-skills/
SCRAPED_DIR = PROJECT_ROOT / ".temp" / "scraped"

OUTPUT_DIR = SCRIPT_DIR.parent / "references" / "components"

# 组件分类
CATEGORIES = {
    "Alert": "基础组件", "Badge": "基础组件", "Button": "基础组件", "Card": "基础组件",
    "Divider": "基础组件", "Icon": "基础组件", "Tag": "基础组件", "Title": "基础组件",
    "Block": "基础组件", "GroupBox": "基础组件", "Label": "基础组件",
    "Layout": "布局", "Row": "布局", "Stack": "布局", "Affix": "布局",
    "Anchor": "布局", "AnchorLink": "布局", "GoTop": "布局", "Footer": "布局",
    "Responsive": "布局", "Split": "布局", "Transition": "布局",
    "AutoComplete": "表单输入", "AutoFill": "表单输入", "Cascader": "表单输入",
    "Checkbox": "表单输入", "ClockPicker": "表单输入", "ColorPicker": "表单输入",
    "DateTimePicker": "表单输入", "DateTimeRange": "表单输入", "EditorForm": "表单输入",
    "Input": "表单输入", "InputNumber": "表单输入", "IpAddress": "表单输入",
    "Radio": "表单输入", "Rate": "表单输入", "Select": "表单输入",
    "Segmented": "表单输入", "Slider": "表单输入", "Switch": "表单输入",
    "Textarea": "表单输入", "TimePicker": "表单输入", "Toggle": "表单输入",
    "Transfer": "表单输入", "Upload": "表单输入",
    "Validate": "表单验证", "ValidateForm": "表单验证",
    "Breadcrumb": "导航", "Menu": "导航", "Nav": "导航", "Navbar": "导航",
    "Pagination": "导航", "RibbonTab": "导航", "Step": "导航", "Tab": "导航",
    "Toolbar": "导航",
    "Avatar": "数据展示", "Calendar": "数据展示", "Carousel": "数据展示",
    "Circle": "数据展示", "CountUp": "数据展示", "Display": "数据展示",
    "Empty": "数据展示", "FlipClock": "数据展示", "ImageViewer": "数据展示",
    "Light": "数据展示", "ListView": "数据展示", "Marquee": "数据展示",
    "Progress": "数据展示", "Skeleton": "数据展示", "Spinner": "数据展示",
    "Table": "数据展示", "Timeline": "数据展示", "Timer": "数据展示",
    "Tree": "数据展示", "TreeView": "数据展示", "Typed": "数据展示",
    "Watermark": "数据展示",
    "Console": "反馈", "Dialog": "反馈", "Drawer": "反馈", "Dropdown": "反馈",
    "DropdownWidget": "反馈", "Message": "反馈", "Modal": "反馈",
    "Notification": "反馈", "Popover": "反馈", "SweetAlert": "反馈",
    "Toast": "反馈", "Tooltip": "反馈",
}


def get_category(component_name: str) -> str:
    """获取组件分类"""
    return CATEGORIES.get(component_name, "其他")


def load_scraped_data(component_name: str) -> dict:
    """加载抓取的官方文档数据"""
    # component_name 是 PascalCase，需要转为 kebab-case
    kebab_name = re.sub(r'(?<!^)(?=[A-Z])', '-', component_name).lower()
    
    txt_file = SCRAPED_DIR / f"{kebab_name}.txt"
    html_file = SCRAPED_DIR / f"{kebab_name}.html"
    
    result = {"text": "", "html": "", "success": False}
    
    if txt_file.exists():
        result["text"] = txt_file.read_text(encoding="utf-8")
        result["success"] = True
    
    if html_file.exists():
        result["html"] = html_file.read_text(encoding="utf-8")
    
    return result


def parse_scraped_text(text: str) -> dict:
    """解析抓取的文本内容，提取关键信息"""
    result = {
        "overview": "",
        "usage_scenarios": [],
        "best_practices": [],
    }
    
    if not text:
        return result
    
    lines = text.split("\n")
    
    # 提取概述（找"组件标签"后面的段落）
    overview_lines = []
    for i, line in enumerate(lines):
        if "组件标签" in line:
            # 从下一行开始收集，直到遇到空行或"小提示"
            for j in range(i+1, min(i+20, len(lines))):
                next_line = lines[j].strip()
                if not next_line or "小提示" in next_line or "##" in next_line:
                    break
                if next_line and len(next_line) > 10:
                    overview_lines.append(next_line)
            break
    
    if overview_lines:
        result["overview"] = " ".join(overview_lines)
    
    # 提取小提示/注意事项（"小提示"段落）
    tips_lines = []
    for i, line in enumerate(lines):
        if "小提示" in line:
            # 收集小提示内容
            for j in range(i+1, min(i+30, len(lines))):
                next_line = lines[j].strip()
                if not next_line or "##" in next_line or "使用" in next_line:
                    break
                if next_line and len(next_line) > 5:
                    tips_lines.append(next_line)
            break
    
    result["best_practices"] = tips_lines[:5]
    
    # 提取使用场景（"单独使用"、"EditorForm 中使用"等段落）
    scenarios = []
    in_scenario = False
    scenario_lines = []
    scenario_title = ""
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        
        # 检测场景标题（以"使用"、"在"开头，或包含"中使用"）
        if line_stripped and ("使用" in line_stripped or "在" in line_stripped) and len(line_stripped) < 50:
            if in_scenario and scenario_lines:
                scenarios.append({
                    "title": scenario_title,
                    "content": "\n".join(scenario_lines)
                })
            in_scenario = True
            scenario_title = line_stripped
            scenario_lines = []
        elif in_scenario and line_stripped:
            scenario_lines.append(line_stripped)
    
    # 最后一个场景
    if in_scenario and scenario_lines:
        scenarios.append({
            "title": scenario_title,
            "content": "\n".join(scenario_lines)
        })
    
    result["usage_scenarios"] = scenarios[:5]  # 最多5个场景
    
    return result


def load_docs_json() -> dict:
    """加载 docs.json 获取组件示例映射"""
    if DOCS_JSON.exists():
        with open(DOCS_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("src", {})
    return {}


def parse_razor_cs(filepath: Path) -> dict:
    """
    解析 .razor.cs 文件，提取:
    - 组件描述 (class XML doc)
    - 参数列表 ([Parameter] 标记的属性)
    - 事件回调 (EventCallback 类型)
    """
    if not filepath.exists():
        return {"description": "", "parameters": [], "events": []}
    
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")
    
    result = {
        "description": "",
        "description_en": "",
        "parameters": [],
        "events": [],
    }
    
    # 正则模式
    param_pattern = re.compile(r'\[Parameter\]')
    event_type_pattern = re.compile(r'EventCallback<')
    property_pattern = re.compile(r'public\s+(?:new\s+)?(\S+(?:<[^>]+>)?)\s+(\w+)\s*\{')
    xml_pattern = re.compile(r'///\s*<summary>\s*$')
    xml_lang_pattern = re.compile(r'///\s*<para\s+lang="(\w+)"\s*>\s*(.*?)\s*</para>', re.IGNORECASE)
    xml_line_pattern = re.compile(r'///\s*(.*)')
    xml_end_pattern = re.compile(r'///\s*</summary>')
    
    # 解析类级别的 XML doc
    in_class_doc = False
    class_doc_lines = []
    for i, line in enumerate(lines):
        if line.strip().startswith("public partial class ") and i > 0:
            # 检查上面几行是否有 XML doc
            for j in range(i - 1, max(i - 20, 0), -1):
                if '</summary>' in lines[j]:
                    # 收集 XML doc 内容
                    for k in range(j - 1, max(j - 30, -1), -1):
                        if '<summary>' in lines[k] or '<summary' in lines[k]:
                            doc_text = "\n".join(lines[k:j]).strip()
                            # 提取中英文描述
                            for m in re.finditer(xml_lang_pattern, doc_text):
                                lang = m.group(1)
                                text = m.group(2).strip()
                                if lang == "zh":
                                    result["description"] = text
                                elif lang == "en":
                                    result["description_en"] = text
                            break
                    break
    
    # 解析 [Parameter] 属性
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if param_pattern.match(line):
            # 找到 [Parameter]，往上找 XML doc
            doc_zh = ""
            doc_en = ""
            for j in range(i - 1, max(i - 20, 0), -1):
                prev_line = lines[j].strip()
                if prev_line.startswith("///"):
                    if '</summary>' in prev_line:
                        # 收集这个 XML doc block
                        for k in range(j, max(j - 30, -1), -1):
                            doc_line = lines[k].strip()
                            if '<summary>' in doc_line or '<summary' in doc_line:
                                for x in range(k, j + 1):
                                    dx = lines[x].strip()
                                    m = re.match(xml_lang_pattern, dx)
                                    if m:
                                        if m.group(1) == "zh":
                                            doc_zh = m.group(2).strip()
                                        elif m.group(1) == "en":
                                            doc_en = m.group(2).strip()
                                    elif not dx.startswith("/// <") and not dx.startswith("///</"):
                                        text = dx.replace("///", "").strip()
                                        if text and not doc_zh:
                                            doc_zh = text
                                break
                    break
            
            # 往下找属性声明（1-5行内）
            for j in range(i + 1, min(i + 8, len(lines))):
                p_match = re.match(r'public\s+(?:new\s+)?(\S+(?:<[^>]+>)?)\s+(\w+)\s*(\{.*?\})?\s*', lines[j].strip())
                if p_match:
                    prop_type = p_match.group(1)
                    prop_name = p_match.group(2)
                    is_event = "EventCallback" in prop_type
                    
                    # 提取默认值
                    default_val = ""
                    default_match = re.search(r'=\s*([^;]+?)\s*;', lines[j])
                    if default_match:
                        default_val = default_match.group(1).strip()
                    else:
                        # 检查 setter 中的默认值
                        setter_match = re.search(r'set;\s*(\S+)', lines[j].strip())
                        if setter_match:
                            default_val = setter_match.group(1).strip()
                    
                    item = {
                        "name": prop_name,
                        "type": prop_type,
                        "description": doc_zh,
                        "description_en": doc_en,
                        "is_event": is_event,
                        "default": default_val,
                    }
                    
                    if is_event:
                        result["events"].append(item)
                    else:
                        result["parameters"].append(item)
                    break
        i += 1
    
    return result


def find_base_params(filepath: Path, visited: set = None) -> list:
    """递归查找基类中的 [Parameter] 属性"""
    if visited is None:
        visited = set()
    
    if not filepath.exists():
        return []
    
    content = filepath.read_text(encoding="utf-8")
    params = []
    
    # 查找继承声明
    inherit_match = re.search(r':\s*(?:public\s+)?(\w+Base|\w+)\b(?!\s*\{)', content)
    if inherit_match:
        base_name = inherit_match.group(1)
        if base_name not in visited:
            visited.add(base_name)
            # 在 Components 目录中搜索基类
            for root, dirs, files in os.walk(COMPONENTS_DIR):
                for f in files:
                    if f == f"{base_name}.cs" or f == f"{base_name}.razor.cs":
                        base_path = Path(root) / f
                        result = parse_razor_cs(base_path)
                        params.extend(result["parameters"])
                        params.extend(find_base_params(base_path, visited))
                        break
    
    return params


def extract_sample_code(sample_file: Path, component_name: str) -> list:
    """从示例页面中提取关键代码示例"""
    if not sample_file.exists():
        return []
    
    content = sample_file.read_text(encoding="utf-8")
    examples = []
    
    # 提取 DemoBlock 中的代码
    demo_blocks = re.finditer(
        r'<DemoBlock[^>]*>(.*?)</DemoBlock>',
        content, re.DOTALL
    )
    
    for match in demo_blocks:
        block_content = match.group(1)
        # 提取组件标签
        tag_pattern = re.compile(
            rf'<{component_name}\b[^>]*>.*?</{component_name}>',
            re.DOTALL
        )
        tags = tag_pattern.findall(block_content)
        if tags and len(tags) <= 3:
            examples.append({
                "name": "基本用法",
                "code": tags[0].strip() if len(tags) == 1 else "\n".join(t.strip() for t in tags),
            })
    
    return examples


def generate_markdown(
    component_name: str,
    doc_info: dict,
    base_params: list,
    samples: list,
    docs_mapping: dict,
    scraped_info: dict,
) -> str:
    """生成组件的完整 Markdown 文档"""
    desc = doc_info["description"] or f"{component_name} 组件"
    desc_en = doc_info["description_en"] or f"{component_name} component"
    all_params = doc_info["parameters"] + base_params
    all_events = doc_info["events"]
    category = get_category(component_name)
    
    # 去重参数（按名称）
    seen_names = set()
    unique_params = []
    for p in all_params:
        if p["name"] not in seen_names:
            seen_names.add(p["name"])
            unique_params.append(p)
    
    # 查找对应的 docs.json key
    doc_key = ""
    for k, v in docs_mapping.items():
        # 规范化比较
        k_normalized = k.replace("-", "").lower()
        cn_normalized = component_name.lower()
        if k_normalized == cn_normalized or k_normalized.replace("-", "") == cn_normalized:
            doc_key = k
            break
    
    demo_url = f"https://www.blazor.zone/{doc_key}" if doc_key else ""
    
    # 从抓取的数据中提取更多信息
    scraped_text = scraped_info.get("text", "")
    scraped_overview = scraped_info.get("overview", "")
    scraped_tips = scraped_info.get("best_practices", [])
    
    lines = []
    
    # 标题
    lines.append(f"# {component_name}\n")
    
    # 概述
    overview_text = scraped_overview or desc
    if overview_text:
        lines.append(f"## 概述\n\n{overview_text}\n")
        if desc_en and desc_en != overview_text:
            lines.append(f"> {desc_en}\n")
    
    # 分类和在线演示
    lines.append(f"**分类**: {category}")
    if demo_url:
        lines.append(f"**在线演示**: [{demo_url}]({demo_url})")
    lines.append("")
    
    # 使用场景（从抓取的数据中提取）
    usage_scenarios = scraped_info.get("usage_scenarios", [])
    if usage_scenarios:
        lines.append("## 使用场景\n")
        for scenario in usage_scenarios[:5]:  # 最多5个场景
            lines.append(f"### {scenario['title']}\n")
            lines.append(scenario["content"])
            lines.append("")
    
    # 最佳实践/注意事项（从抓取的数据中提取）
    if scraped_tips:
        lines.append("## 最佳实践\n")
        for tip in scraped_tips[:5]:
            lines.append(f"- {tip}")
        lines.append("")
    
    # 参数表
    if unique_params:
        lines.append("## 参数 (Parameters)\n")
        lines.append("| 参数名 | 类型 | 默认值 | 说明 |")
        lines.append("|--------|------|--------|------|")
        for p in unique_params:
            desc_text = p["description"] or p["description_en"] or "-"
            default_text = p["default"] or "null"
            lines.append(f"| `{p['name']}` | `{p['type']}` | `{default_text}` | {desc_text} |")
        lines.append("")
    
    # 事件回调
    if all_events:
        lines.append("## 事件回调 (EventCallbacks)\n")
        lines.append("| 事件名 | 类型 | 说明 |")
        lines.append("|--------|------|------|")
        for e in all_events:
            desc_text = e["description"] or e["description_en"] or "-"
            lines.append(f"| `{e['name']}` | `{e['type']}` | {desc_text} |")
        lines.append("")
    
    # 代码示例
    if samples:
        lines.append("## 代码示例\n")
        for i, sample in enumerate(samples[:5]):  # 最多 5 个示例
            lines.append(f"### {sample.get('name', f'示例 {i+1}')}\n")
            lines.append("```razor")
            lines.append(sample["code"])
            lines.append("```\n")
    
    return "\n".join(lines)


def find_component_source(component_name: str) -> Optional[Path]:
    """查找组件源码目录"""
    comp_dir = COMPONENTS_DIR / component_name
    if comp_dir.exists() and comp_dir.is_dir():
        return comp_dir
    # 尝试大小写不敏感
    for d in COMPONENTS_DIR.iterdir():
        if d.is_dir() and d.name.lower() == component_name.lower():
            return d
    return None


def find_sample_file(component_name: str, docs_mapping: dict) -> Optional[Path]:
    """查找示例文件"""
    # 通过 docs.json 查找
    for k, v in docs_mapping.items():
        # v 是类似 "Alerts", "Buttons", "Table\\Tables" 的格式
        sample_name = v.split("\\")[-1]  # 取最后一部分
        k_normalized = k.replace("-", "").lower()
        cn = component_name.lower()
        
        if k_normalized == cn or k_normalized == cn.replace("-", ""):
            sample_path = SAMPLES_DIR / f"{sample_name}.razor"
            if sample_path.exists():
                return sample_path
    
    # 直接构造
    sample_path = SAMPLES_DIR / f"{component_name}s.razor"
    if sample_path.exists():
        return sample_path
    
    return None


def process_component(component_name: str, docs_mapping: dict) -> bool:
    """处理单个组件，返回是否成功"""
    print(f"  🔍 处理: {component_name}...", end=" ")
    
    # 1. 查找组件源码
    comp_dir = find_component_source(component_name)
    if not comp_dir:
        print("⚠️  无源码目录，跳过")
        return False
    
    # 2. 查找 .razor.cs 文件
    razor_cs_files = list(comp_dir.glob(f"{component_name}.razor.cs"))
    if not razor_cs_files:
        razor_cs_files = list(comp_dir.glob("*.razor.cs"))
    
    if not razor_cs_files:
        print("⚠️  无 .razor.cs 文件，跳过")
        return False
    
    # 3. 解析参数（从源码）
    doc_info = parse_razor_cs(razor_cs_files[0])
    base_params = find_base_params(razor_cs_files[0])
    
    # 4. 加载抓取的官方文档
    scraped_info = load_scraped_data(component_name)
    if not scraped_info["success"]:
        print("⚠️  无抓取数据，使用源码信息", end=" ")
    
    # 5. 查找示例
    sample_file = find_sample_file(component_name, docs_mapping)
    samples = []
    if sample_file:
        samples = extract_sample_code(sample_file, component_name)
    
    # 6. 生成 Markdown
    md_content = generate_markdown(
        component_name, doc_info, base_params, samples, docs_mapping, scraped_info
    )
    
    # 7. 写入文件（使用 kebab-case）
    file_name = re.sub(r'(?<!^)(?=[A-Z])', '-', component_name).lower() + ".md"
    output_path = OUTPUT_DIR / file_name
    output_path.write_text(md_content, encoding="utf-8")
    
    print(f"✅ ({len(doc_info['parameters'])} 参数, {len(samples)} 示例)")
    return True


def main():
    print("=" * 60)
    print("BootstrapBlazor Skill - 文档更新器")
    print("=" * 60)
    
    # 检查抓取数据目录
    if not SCRAPED_DIR.exists():
        print(f"❌ 错误: 抓取数据目录不存在: {SCRAPED_DIR}")
        print(f"请先运行: python scripts/scrape_bootstrap_blazor_v2.py")
        sys.exit(1)
    
    docs_mapping = load_docs_json()
    print(f"📋 从 docs.json 加载了 {len(docs_mapping)} 个文档路由")
    
    # 获取所有组件目录
    component_dirs = sorted(
        [d for d in COMPONENTS_DIR.iterdir() if d.is_dir()],
        key=lambda x: x.name.lower()
    )
    
    # 排除非组件目录
    exclude = {"BaseComponents", "BootstrapBlazorRootOutlet", "SelectGeneric"}
    component_dirs = [d for d in component_dirs if d.name not in exclude]
    
    print(f"📦 找到 {len(component_dirs)} 个组件目录")
    
    # 支持命令行参数：指定要更新的组件
    args = sys.argv[1:]
    if args:
        # 过滤出有效的组件名
        valid_components = [d.name for d in component_dirs if d.name in args]
        if not valid_components:
            print(f"❌ 错误: 指定的组件名无效: {args}")
            print(f"有效组件名示例: {[d.name for d in component_dirs[:5]]}...")
            sys.exit(1)
        component_dirs = [d for d in component_dirs if d.name in valid_components]
        print(f"📋 命令行参数: 只更新 {len(component_dirs)} 个组件: {[d.name for d in component_dirs]}")
    
    # 确保输出目录存在
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    skip_count = 0
    
    for comp_dir in component_dirs:
        component_name = comp_dir.name
        try:
            if process_component(component_name, docs_mapping):
                success_count += 1
            else:
                skip_count += 1
        except Exception as e:
            print(f"❌ 错误: {e}")
            skip_count += 1
    
    print(f"\n{'=' * 60}")
    print(f"✅ 完成! 成功: {success_count}, 跳过: {skip_count}")
    print(f"📂 文档输出目录: {OUTPUT_DIR}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ 脚本执行失败: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
