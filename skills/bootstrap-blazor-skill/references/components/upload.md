# Upload

## 概述

头像上传组件

> Avatar Upload Component

**分类**: 表单输入

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Width` | `int` | `100` | 获得/设置 文件预览框宽度 |
| `Height` | `int` | `100` | 获得/设置 文件预览框高度 |
| `IsCircle` | `bool` | `}` | 获得/设置 是否圆形图片框，Avatar 模式时生效，默认为 false |
| `BorderRadius` | `string?` | `}` | 获得/设置 边框圆角，默认为 null |
| `AllowExtensions` | `List<string>?` | `}` | 获得/设置 允许的文件扩展名集合，".png" |
| `DeleteIcon` | `string?` | `}` | 获得/设置 删除图标 |
| `LoadingIcon` | `string?` | `}` | 获得/设置 加载中图标 |
| `AddIcon` | `string?` | `}` | 获得/设置 新增图标 |
| `ValidStatusIcon` | `string?` | `}` | 获得/设置 上传成功状态图标 |
| `InvalidStatusIcon` | `string?` | `}` | 获得/设置 上传失败状态图标 |
| `IsUploadButtonAtFirst` | `bool` | `}` | 获得/设置 继续上传按钮是否在列表前，默认 false |
| `bool` | `Func<UploadFile,` | `}` | 获得/设置 是否允许预览的回调方法，默认 null |
