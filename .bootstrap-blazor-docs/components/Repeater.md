# Repeater (重复器)

## 概述

`Repeater` 组件用于**重复渲染一组数据**，类似 `foreach` 循环，但提供更好的模板化和事件支持。

**主要特性**：
- 支持数据绑定
- 支持空数据模板
- 支持分隔符模板
- 支持事件回调

**在线演示**: https://www.blazor.zone/repeater

---

## 使用场景

### 1. 基础用法（简单重复）

`Repeater` 组件通过 `Items` 参数绑定数据源，`ChildContent` 定义每项模板。

```razor
<!-- 基础重复器 -->
<Repeater Items="Items">
    <ChildContent>
        <div class="p-2 border-bottom">@context</div>
    </ChildContent>
</Repeater>

@code {
    private List<string> Items { get; set; } = new List<string> { "项目 1", "项目 2", "项目 3" };
}
```

---

### 2. 空数据模板（EmptyTemplate）

通过 `EmptyTemplate` 参数设置数据为空时的显示内容。

```razor
<!-- 空数据提示 -->
<Repeater Items="EmptyItems">
    <ChildContent>
        <div class="p-2">@context.Name</div>
    </ChildContent>
    <EmptyTemplate>
        <div class="text-muted">暂无数据</div>
    </EmptyTemplate>
</Repeater>

@code {
    private List<Item> EmptyItems { get; set; } = new List<Item>();
    
    public class Item
    {
        public string Name { get; set; } = "";
    }
}
```

---

### 3. 分隔符模板（SeparatorTemplate）

通过 `SeparatorTemplate` 参数设置项之间的分隔符。

```razor
<!-- 带分隔符的重复器 -->
<Repeater Items="Items">
    <ChildContent>
        <span class="badge bg-primary">@context</span>
    </ChildContent>
    <SeparatorTemplate>
        <span class="mx-1">,</span>
    </SeparatorTemplate>
</Repeater>

@code {
    private List<string> Items { get; set; } = new List<string> { "苹果", "香蕉", "橙子" };
}
```

---

### 4. 复杂对象（Complex Object）

`Repeater` 可以绑定复杂对象列表，通过 `context` 访问对象属性。

```razor
<!-- 复杂对象重复器 -->
<Repeater Items="Users">
    <ChildContent>
        <div class="d-flex justify-content-between align-items-center p-2 border-bottom">
            <div>
                <strong>@context.Name</strong>
                <small class="text-muted">@context.Email</small>
            </div>
            <span class="badge bg-@(context.IsActive ? "success" : "secondary")">
                @(context.IsActive ? "活跃" : "停用")
            </span>
        </div>
    </ChildContent>
</Repeater>

@code {
    private List<User> Users { get; set; } = new List<User>
    {
        new User { Name = "张三", Email = "zhangsan@example.com", IsActive = true },
        new User { Name = "李四", Email = "lisi@example.com", IsActive = false }
    };
    
    public class User
    {
        public string Name { get; set; } = "";
        public string Email { get; set; } = "";
        public bool IsActive { get; set; }
    }
}
```

---

### 5. 与 foreach 对比（Comparison）

`Repeater` 相比 `foreach` 的优势：

```razor
<!-- 使用 foreach -->
@foreach (var item in Items)
{
    <div class="p-2">@item</div>
}

<!-- 使用 Repeater -->
<Repeater Items="Items">
    <ChildContent>
        <div class="p-2">@context</div>
    </ChildContent>
    <EmptyTemplate>
        <div class="text-muted">暂无数据</div>
    </EmptyTemplate>
</Repeater>
```

**Repeater 优势**：
- 支持 `EmptyTemplate`（空数据提示）
- 支持 `SeparatorTemplate`（分隔符）
- 更好的模板化支持
- 更符合组件化思维

---

## 参数 (Parameters)

### Repeater 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<T>?` | `null` | 获得/设置数据源 |
| `ChildContent` | `RenderFragment<T>?` | `null` | 获得/设置项模板 |
| `EmptyTemplate` | `RenderFragment?` | `null` | 获得/设置空数据模板 |
| `SeparatorTemplate` | `RenderFragment?` | `null` | 获得/设置分隔符模板 |

---

## 最佳实践

1. **与 foreach 的选择**：简单循环用 `foreach`，需要空数据提示或分隔符时用 `Repeater`
2. **合理使用 EmptyTemplate**：数据可能为空时，使用 `EmptyTemplate` 提供友好提示
3. **避免过度嵌套**：`Repeater` 内避免嵌套过多复杂组件，影响性能
4. **与 Table 的区别**：`Repeater` 是通用重复器，`Table` 是表格数据展示（带排序、分页等）
5. **性能优化**：大数据集考虑虚拟滚动（`Virtualize` 组件）而非 `Repeater`
6. **类型安全**：使用泛型 `Repeater<T>` 获得类型安全，避免 `object` 转换
