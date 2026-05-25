#!/usr/bin/env python3
"""测试 Playwright 是否可用"""
import sys

try:
    import playwright
    print(f"✅ Playwright 已安装，版本: {playwright.__version__}")
except ImportError:
    print("❌ Playwright 未安装")
    sys.exit(1)

# 测试能否启动浏览器
async def test_browser():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.blazor.zone/label", wait_until="networkidle", timeout=30000)
        title = await page.title()
        print(f"✅ 浏览器启动成功，页面标题: {title}")
        await browser.close()

import asyncio
asyncio.run(test_browser())
