# PowerShell 批量重命名组件文件为 PascalCase
# 运行: powershell -ExecutionPolicy Bypass -File rename_remaining.ps1

$dir = "d:\WorkSpace\DotnetProject\ai-skills\skills\bootstrap-blazor-skill\references\components"

Write-Host "扫描目录: $dir"
$files = Get-ChildItem -Path $dir -Filter "*.md"

$renamed = 0
$skipped = 0

foreach ($file in $files) {
    $name = $file.Name
    
    # 检查是否需要重命名（小写开头 或 包含 -）
    if ($name[0] -cmatch "[a-z]" -or $name -match "-") {
        # 转换为 PascalCase: 按 - 分割，每个部分首字母大写，移除 -
        $nameNoExt = $name -replace "\.md$", ""
        $parts = $nameNoExt -split "-"
        $newNameNoExt = ""
        foreach ($part in $parts) {
            if ($part.Length -gt 0) {
                $newNameNoExt += $part.Substring(0,1).ToUpper() + $part.Substring(1)
            }
        }
        $newName = $newNameNoExt + ".md"
        $newPath = Join-Path $dir $newName
        
        # 检查目标是否存在
        if (Test-Path $newPath) {
            Write-Host "  跳过（目标存在）: $name -> $newName"
            $skipped++
        } else {
            # 重命名
            Move-Item -Path $file.FullName -Destination $newPath -Force
            Write-Host "  OK: $name -> $newName"
            $renamed++
        }
    } else {
        # 已是大写开头且无 -，跳过
        # Write-Host "  跳过（已是大写）: $name"
        $skipped++
    }
}

Write-Host "`n完成! 重命名: $renamed, 跳过: $skipped"
