# 重命名组件文档文件脚本
# 将 references/components/ 中的文件从各种命名方式统一为组件名称（PascalCase）

# 组件名称到 URL 的映射
$ComponentMapping = @{
    "Affix" = "affix"
    "Alert" = "alert"
    "Anchor" = "anchor"
    "AnchorLink" = "anchor-link"
    "AutoComplete" = "auto-complete"
    "AutoFill" = "auto-fill"
    "Avatar" = "avatar"
    "Badge" = "badge"
    "Breadcrumb" = "breadcrumb"
    "Button" = "button"
    "Calendar" = "calendar"
    "Camera" = "camera"
    "Captcha" = "captcha"
    "Card" = "card"
    "Carousel" = "carousel"
    "Cascader" = "cascader"
    "Checkbox" = "checkbox"
    "Circle" = "circle"
    "ClockPicker" = "clock-picker"
    "Collapse" = "collapse"
    "ColorPicker" = "color-picker"
    "Console" = "console"
    "ContextMenu" = "context-menu"
    "CountUp" = "count-up"
    "DateTimePicker" = "datetime-picker"
    "DateTimeRange" = "date-time-range"
    "Dialog" = "dialog"
    "Display" = "display"
    "Divider" = "divider"
    "DragDrap" = "drag-drap"
    "Drawer" = "drawer"
    "Dropdown" = "dropdown"
    "DropdownWidget" = "dropdown-widget"
    "EditorForm" = "editor-form"
    "Empty" = "empty"
    "FileIcon" = "file-icon"
    "Filters" = "filters"
    "FlipClock" = "flip-clock"
    "Footer" = "footer"
    "FullScreen" = "fullscreen"
    "GoTop" = "go-top"
    "GroupBox" = "group-box"
    "Handwritten" = "handwritten"
    "HtmlTag" = "html-tag"
    "Icon" = "icon"
    "IFrame" = "i-frame"
    "ImagePreviewer" = "image-previewer"
    "ImageViewer" = "image-viewer"
    "Input" = "input"
    "InputNumber" = "input-number"
    "IpAddress" = "ip-address"
    "Label" = "label"
    "Layout" = "layout"
    "Light" = "light"
    "ListGroup" = "list-group"
    "ListView" = "list-view"
    "Logout" = "logout"
    "Marquee" = "marquee"
    "Mask" = "mask"
    "Menu" = "menu"
    "Message" = "message"
    "Modal" = "modal"
    "Nav" = "nav"
    "Navbar" = "navbar"
    "NetworkMonitor" = "network-monitor"
    "Pagination" = "pagination"
    "Popover" = "popover"
    "Print" = "print"
    "Progress" = "progress"
    "QueryBuilder" = "query-builder"
    "Radio" = "radio"
    "Rate" = "rate"
    "Reconnector" = "reconnector"
    "Repeater" = "repeater"
    "RibbonTab" = "ribbon-tab"
    "Row" = "row"
    "Scroll" = "scroll"
    "Search" = "search"
    "SearchForm" = "search-form"
    "Segmented" = "segmented"
    "Select" = "select"
    "Skeleton" = "skeleton"
    "Slider" = "slider"
    "Speech" = "speech"
    "Spinner" = "spinner"
    "Split" = "split"
    "Stack" = "stack"
    "Step" = "step"
    "SweetAlert" = "sweet-alert"
    "Switch" = "switch"
    "Tab" = "tab"
    "Table" = "table"
    "Tag" = "tag"
    "Textarea" = "textarea"
    "ThemeProvider" = "theme-provider"
    "Timeline" = "timeline"
    "TimePicker" = "time-picker"
    "Timer" = "timer"
    "Toast" = "toast"
    "Toggle" = "toggle"
    "Toolbar" = "toolbar"
    "Tooltip" = "tooltip"
    "Transfer" = "transfer"
    "Transition" = "transition"
    "Tree" = "tree"
    "TreeView" = "tree-view"
    "Typed" = "typed"
    "Upload" = "upload"
    "ValidateForm" = "validate-form"
    "Waterfall" = "waterfall"
    "Watermark" = "watermark"
}

# 获取脚本目录和项目根目录
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path (Split-Path (Split-Path $ScriptDir -Parent) -Parent) -Parent
$ComponentsDir = Join-Path $ProjectRoot "skills\bootstrap-blazor-skill\references\components"

Write-Host "=" * 70
Write-Host "重命名组件文档文件脚本"
Write-Host "=" * 70
Write-Host ""
Write-Host "📁 处理目录: $ComponentsDir"
Write-Host ""

$RenamedCount = 0
$SkippedCount = 0
$ErrorCount = 0

foreach ($ComponentName in $ComponentMapping.Keys) {
    $UrlName = $ComponentMapping[$ComponentName]
    
    # 尝试找到当前文件（可能是多种命名方式）
    $PossibleFileNames = @(
        "$UrlName.md"                    # URL 名称 (kebab-case)
        "$($ComponentName.ToLower()).md"  # 小写组件名
        "$ComponentName.md"               # 正确名称 (PascalCase)
        "$($UrlName.Replace('-', '')).md"  # 无连字符的小写名
    )
    
    $CurrentFile = $null
    foreach ($FileName in $PossibleFileNames) {
        $FilePath = Join-Path $ComponentsDir $FileName
        if (Test-Path $FilePath) {
            $CurrentFile = Get-Item $FilePath
            break
        }
    }
    
    if ($CurrentFile -eq $null) {
        Write-Host "  ❌ 未找到文件: $ComponentName.md (尝试的名称: $($PossibleFileNames -join ', '))"
        $ErrorCount++
        continue
    }
    
    # 目标文件名
    $TargetFileName = "$ComponentName.md"
    $TargetFilePath = Join-Path $ComponentsDir $TargetFileName
    
    # 如果当前文件名已经是正确的，跳过
    if ($CurrentFile.Name -eq $TargetFileName) {
        Write-Host "  ✓ 已正确: $TargetFileName"
        $SkippedCount++
        continue
    }
    
    # 如果目标文件已存在，跳过（避免覆盖）
    if (Test-Path $TargetFilePath) {
        Write-Host "  ⚠️ 目标文件已存在，跳过: $TargetFileName (当前: $($CurrentFile.Name))"
        $ErrorCount++
        continue
    }
    
    # 重命名文件
    try {
        Rename-Item -Path $CurrentFile.FullName -NewName $TargetFileName -ErrorAction Stop
        Write-Host "  ✓ $($CurrentFile.Name) -> $TargetFileName"
        $RenamedCount++
    }
    catch {
        Write-Host "  ❌ 重命名失败: $($CurrentFile.Name) -> $TargetFileName (错误: $_)"
        $ErrorCount++
    }
}

Write-Host ""
Write-Host "=" * 70
Write-Host "✅ 完成！"
Write-Host "   重命名: $RenamedCount 个文件"
Write-Host "   跳过: $SkippedCount 个文件 (已正确命名)"
Write-Host "   错误: $ErrorCount 个文件"
Write-Host "=" * 70
