#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BootstrapBlazor Skill - 组件文档生成脚本（AI 驱动）
读取源码和抓取的官方文档，调用 AI API 生成高质量的 component.md 文件。

用法:
    conda activate py310
    python scripts/generate_components.py              # 生成所有组件
    python scripts/generate_components.py Alert Button  # 只生成 Alert 和 Button 组件

要求:
    - 指定本地 BootstrapBlazor 源代码仓库位置 REPO_ROOT 变量
    - Python 3.10+
    - 已运行 scrape_bootstrap_blazor_v2.py 抓取官方文档到 .temp/scraped/
    - 已配置 AI_API_KEY 环境变量 或修改脚本中的 AI_API_KEY 变量
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import List, Dict

# ========== 配置区域 ==========
# AI API 配置（硅基流动，OpenAI 兼容）
AI_API_BASE = "https://api.siliconflow.cn/v1"  # 硅基流动 API 地址
AI_MODEL = "Qwen/Qwen2.5-72B-Instruct"  # 使用的模型（免费额度）
AI_API_KEY = os.getenv("AI_API_KEY", "")  # 从环境变量读取，或在这里填写你的 API Key

# 路径配置
REPO_ROOT = Path(r"D:\WorkSpace\DotnetProject\BootstrapBlazor")
SRC_DIR = REPO_ROOT / "src" / "BootstrapBlazor"
COMPONENTS_DIR = SRC_DIR / "Components"
SCRAPED_DIR = Path(__file__).resolve().parent.parent.parent / ".temp" / "scraped"  # ai-skills/.temp/scraped/
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "references" / "components"
# ===============================


def read_source_code(component_name: str) -> Dict:
    """读取组件源码，提取关键信息"""
    result = {"description": "", "parameters": [], "events": []}
    
    comp_dir = COMPONENTS_DIR / component_name
    if not comp_dir.exists():
        return result
    
    # 查找 .razor.cs 文件
    razor_cs_files = list(comp_dir.glob("*.razor.cs"))
    if not razor_cs_files:
        return result
    
    # 读取文件内容
    content = razor_cs_files[0].read_text(encoding="utf-8")
    
    # 提取 [Parameter] 属性（参数和事件）
    param_pattern = re.compile(r'\[Parameter\]')
    lines = content.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if param_pattern.search(line):
            # 往上找 XML 文档注释
            desc_zh = ""
            desc_en = ""
            for j in range(i - 1, max(0, i - 15), -1):
                if "///" in lines[j]:
                    comment_block = "\n".join(lines[j:i])
                    zh_m = re.search(r'lang="zh">(.*?)</para>', comment_block, re.DOTALL)
                    en_m = re.search(r'lang="en">(.*?)</para>', comment_block, re.DOTALL)
                    if zh_m:
                        desc_zh = zh_m.group(1).strip()
                    if en_m:
                        desc_en = en_m.group(1).strip()
                    break
            
            # 往下找属性声明
            for j in range(i + 1, min(i + 5, len(lines))):
                prop_match = re.match(
                    r'public\s+(\S+)\s+(\w+)\s*[;{]',
                    lines[j].strip()
                )
                if prop_match:
                    prop_type = prop_match.group(1)
                    prop_name = prop_match.group(2)
                    is_event = "EventCallback" in prop_type
                    
                    # 提取默认值
                    default_val = ""
                    default_m = re.search(r'=\s*([^;]+?)\s*;', lines[j])
                    if default_m:
                        default_val = default_m.group(1).strip()
                    
                    item = {
                        "name": prop_name,
                        "type": prop_type,
                        "default": default_val,
                        "description": desc_zh or desc_en,
                    }
                    
                    if is_event:
                        result["events"].append(item)
                    else:
                        result["parameters"].append(item)
                    break
        i += 1
    
    return result


def read_scraped_data(component_name: str) -> str:
    """读取抓取的官方文档"""
    kebab_name = re.sub(r'(?<!^)(?=[A-Z])', '-', component_name).lower()
    txt_file = SCRAPED_DIR / f"{kebab_name}.txt"
    if txt_file.exists():
        return txt_file.read_text(encoding="utf-8")
    return ""


def generate_prompt(component_name: str, source_info: Dict, scraped_text: str) -> str:
    """生成给 AI 的 prompt"""
    prompt = f"""你是 Bootstrap Blazor 组件文档专家。请根据以下信息，为 `{component_name}` 组件生成一份完整的 `component.md` 文档。

## 目标
生成的文档将用于 **Bootstrap Blazor Skill**，让 AI 能够准确理解和使用该组件。
文档应包含：
1. 完整的概述
2. 使用场景（带示例代码）
3. 参数说明（完整的参数表格）
4. 最佳实践/注意事项

## 输入数据

### 1. 组件源码信息（从 .razor.cs 提取）
```json
{json.dumps(source_info, ensure_ascii=False, indent=2)}
```

### 2. 抓取的官方文档（从官网抓取）
```
{scraped_text[:3000]}  # 只取前 3000 字符
```

## 输出要求

请生成 Markdown 格式的文档，包含以下章节：

1. **# 标题**（组件名称）
2. **## 概述**（组件用途、功能说明）
3. **## 使用场景**（多个场景，每个场景带示例代码）
4. **## 参数 (Parameters)**（完整表格：参数名 | 类型 | 默认值 | 说明）
5. **## 事件回调 (EventCallbacks)**（如有）
6. **## 最佳实践**（注意事项、使用技巧）

**重要**：
- 参数表格中的 **默认值** 必须准确（不要写 `}`）
- 示例代码必须是 **可运行的 Razor 代码**
- 使用场景要 **实用**、**贴近实际开发**
- 最佳实践要 **简洁**、**有价值**

请直接输出 Markdown 内容，不要加 ```markdown 包裹。
"""
    return prompt


def call_ai_api(prompt: str) -> str:
    """调用 AI API 生成文档"""
    try:
        from openai import OpenAI
        
        client = OpenAI(
            api_key=AI_API_KEY,
            base_url=AI_API_BASE,
        )
        
        response = client.chat.completions.create(
            model=AI_MODEL,
            messages=[
                {"role": "system", "content": "你是 Bootstrap Blazor 组件文档专家。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=4000,
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"    ❌ AI API 调用失败: {e}")
        return ""


def generate_component_md(component_name: str) -> str:
    """生成组件的 Markdown 文档"""
    print(f"  📝 生成文档: {component_name}")
    
    # 1. 读取源码
    source_info = read_source_code(component_name)
    print(f"    ✓ 源码: {len(source_info['parameters'])} 参数, {len(source_info['events'])} 事件")
    
    # 2. 读取抓取的数据
    scraped_text = read_scraped_data(component_name)
    if scraped_text:
        print(f"    ✓ 抓取数据: {len(scraped_text)} 字符")
    else:
        print(f"    ⚠️  无抓取数据")
    
    # 3. 生成 prompt
    prompt = generate_prompt(component_name, source_info, scraped_text)
    
    # 4. 调用 AI API
    print(f"    🤖 调用 AI API...")
    md_content = call_ai_api(prompt)
    
    if md_content:
        print(f"    ✅ AI 生成完成: {len(md_content)} 字符")
        return md_content
    else:
        print(f"    ❌ AI 生成失败")
        return ""


def find_all_components() -> List[Path]:
    """查找所有组件目录"""
    dirs = sorted(
        [d for d in COMPONENTS_DIR.iterdir() if d.is_dir()],
        key=lambda x: x.name.lower()
    )
    
    # 排除非组件目录
    exclude = {"BaseComponents", "BootstrapBlazorRootOutlet", "SelectGeneric"}
    dirs = [d for d in dirs if d.name not in exclude]
    
    return dirs


def main():
    print("=" * 60)
    print("Bootstrap Blazor Skill - 组件文档生成器（AI 驱动）")
    print("=" * 60)
    
    # 检查 AI API Key
    if not AI_API_KEY:
        print("❌ 错误: 未配置 AI_API_KEY")
        print("请设置环境变量 AI_API_KEY 或修改脚本中的 AI_API_KEY 变量")
        print("获取免费 API Key: https://siliconflow.cn/")
        sys.exit(1)
    
    # 检查抓取数据目录
    if not SCRAPED_DIR.exists():
        print(f"❌ 错误: 抓取数据目录不存在: {SCRAPED_DIR}")
        print(f"请先运行: python scripts/scrape_bootstrap_blazor_v2.py")
        sys.exit(1)
    
    # 支持命令行参数：指定要生成的组件
    args = sys.argv[1:]
    if args:
        all_dirs = find_all_components()
        valid_dirs = [d for d in all_dirs if d.name in args]
        if not valid_dirs:
            print(f"❌ 错误: 指定的组件名无效: {args}")
            print(f"有效组件名示例: {[d.name for d in all_dirs[:5]]}...")
            sys.exit(1)
        component_dirs = valid_dirs
        print(f"📋 命令行参数: 只生成 {len(component_dirs)} 个组件: {[d.name for d in component_dirs]}")
    else:
        component_dirs = find_all_components()
        print(f"📦 找到 {len(component_dirs)} 个组件目录")
    
    # 确保输出目录存在
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    skip_count = 0
    
    for i, comp_dir in enumerate(component_dirs):
        component_name = comp_dir.name
        print(f"\n[{i+1}/{len(component_dirs)}] 🔍 处理: {component_name}...")
        
        try:
            md_content = generate_component_md(component_name)
            if md_content:
                # 写入文件（使用 kebab-case）
                file_name = re.sub(r'(?<!^)(?=[A-Z])', '-', component_name).lower() + ".md"
                output_path = OUTPUT_DIR / file_name
                output_path.write_text(md_content, encoding="utf-8")
                print(f"    ✅ 已保存: {output_path}")
                success_count += 1
            else:
                skip_count += 1
        except Exception as e:
            print(f"    ❌ 错误: {e}")
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
