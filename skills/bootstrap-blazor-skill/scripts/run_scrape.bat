@echo off
chcp 65001 >nul
echo [Bootstrap Blazor Skill] 组件文档抓取脚本
echo ========================================
echo.

:: 切换到脚本所在目录（支持路径中有空格）
cd /d "%~dp0"

:: 激活 conda 环境
call conda activate py310
if errorlevel 1 (
    echo [错误] 无法激活 conda 环境 py310
    pause
    exit /b 1
)

echo.
echo [环境] Python 版本：
python --version
echo [环境] Playwright 版本：
pip list | findstr playwright

echo.
echo ========================================
echo [开始] 正在抓取组件文档...
echo.

:: 运行抓取脚本
python scrape_bootstrap_blazor.py

echo.
echo ========================================
echo [完成] 按任意键退出...
pause
