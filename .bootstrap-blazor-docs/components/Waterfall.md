# Waterfall (瀑布流)

## 概述

`Waterfall` 组件用于**创建瀑布流布局**，常用于图片墙、商品列表等场景，元素按列排列，高度不一。

**主要特性**：
- 自适应列数
- 支持响应式布局
- 可设置列间距
- 支持无限滚动加载
- 可自定义 item 模板

**在线演示**: https://www.blazor.zone/waterfall

---

## 使用场景

### 1. 基础用法（简单瀑布流）

`Waterfall` 组件可以通过 `Items` 参数绑定数据源。

```razor
<!-- 基础瀑布流 -->
<Waterfall Items="WaterfallItems">
    <ItemTemplate>
        <div class="waterfall-item">
            <img src="@context.ImageUrl" alt="@context.Title" />
            <p>@context.Title</p>
        </div>
    </ItemTemplate>
</Waterfall>

@code {
    private List<WaterfallItem> WaterfallItems { get; set; } = new List<WaterfallItem>
    {
        new WaterfallItem("图片1", "https://via.placeholder.com/300x200"),
        new WaterfallItem("图片2", "https://via.placeholder.com/300x300"),
        new WaterfallItem("图片3", "https://via.placeholder.com/300x250"),
        new WaterfallItem("图片4", "https://via.placeholder.com/300x350"),
        new WaterfallItem("图片5", "https://via.placeholder.com/300x280")
    };

    public class WaterfallItem
    {
        public string Title { get; set; }
        public string ImageUrl { get; set; }
        
        public WaterfallItem(string title, string imageUrl)
        {
            Title = title;
            ImageUrl = imageUrl;
        }
    }
}
```

---

### 2. 设置列数（Columns）

通过 `Columns` 参数设置瀑布流列数。

```razor
<!-- 3 列瀑布流 -->
<Waterfall Items="WaterfallItems" Columns="3">
    <ItemTemplate>
        <div class="waterfall-item">
            <img src="@context.ImageUrl" alt="@context.Title" />
        </div>
    </ItemTemplate>
</Waterfall>

@code {
    private List<WaterfallItem> WaterfallItems { get; set; } = new List<WaterfallItem>
    {
        new WaterfallItem("图片1", "https://via.placeholder.com/300x200"),
        new WaterfallItem("图片2", "https://via.placeholder.com/300x300")
    };
}
```

---

### 3. 设置列间距（Gap）

通过 `Gap` 参数设置列间距（像素）。

```razor
<!-- 间距 20px -->
<Waterfall Items="WaterfallItems" Gap="20">
    <ItemTemplate>
        <div class="waterfall-item">
            <img src="@context.ImageUrl" alt="@context.Title" />
        </div>
    </ItemTemplate>
</Waterfall>

@code {
    private List<WaterfallItem> WaterfallItems { get; set; } = new List<WaterfallItem>
    {
        new WaterfallItem("图片1", "https://via.placeholder.com/300x200")
    };
}
```

---

### 4. 响应式布局（Breakpoints）

通过 `Breakpoints` 参数设置响应式断点。

```razor
<!-- 响应式瀑布流 -->
<Waterfall Items="WaterfallItems" Breakpoints="@Breakpoints">
    <ItemTemplate>
        <div class="waterfall-item">
            <img src="@context.ImageUrl" alt="@context.Title" />
        </div>
    </ItemTemplate>
</Waterfall>

@code {
    private List<WaterfallItem> WaterfallItems { get; set; } = new List<WaterfallItem>
    {
        new WaterfallItem("图片1", "https://via.placeholder.com/300x200")
    };

    private Dictionary<string, int> Breakpoints { get; set; } = new Dictionary<string, int>
    {
        { "640px", 2 },
        { "768px", 3 },
        { "1024px", 4 }
    };
}
```

**说明**：以上断点表示：
- 屏幕宽度 < 640px：2 列
- 640px ≤ 屏幕宽度 < 768px：3 列
- 768px ≤ 屏幕宽度 < 1024px：4 列
- 屏幕宽度 ≥ 1024px：使用 `Columns` 参数的值

---

### 5. 无限滚动加载（OnLoadMore）

通过 `OnLoadMore` 事件实现无限滚动加载。

```razor
<!-- 无限滚动瀑布流 -->
<Waterfall Items="WaterfallItems" OnLoadMore="LoadMoreItems" HasMore="HasMore">
    <ItemTemplate>
        <div class="waterfall-item">
            <img src="@context.ImageUrl" alt="@context.Title" />
            <p>@context.Title</p>
        </div>
    </ItemTemplate>
</Waterfall>

@code {
    private List<WaterfallItem> WaterfallItems { get; set; } = new List<WaterfallItem>();
    private bool HasMore { get; set; } = true;
    private int PageIndex { get; set; } = 1;

    private async Task LoadMoreItems()
    {
        // 模拟加载数据
        await Task.Delay(1000);
        
        var newItems = Enumerable.Range(PageIndex * 5, 5)
            .Select(i => new WaterfallItem($"图片{i}", $"https://via.placeholder.com/300x{200 + i % 100}"))
            .ToList();
        
        WaterfallItems.AddRange(newItems);
        PageIndex++;
        
        // 假设加载 5 页后没有更多数据
        if (PageIndex > 5)
        {
            HasMore = false;
        }
    }

    public class WaterfallItem
    {
        public string Title { get; set; }
        public string ImageUrl { get; set; }
        
        public WaterfallItem(string title, string imageUrl)
        {
            Title = title;
            ImageUrl = imageUrl;
        }
    }
}
```

---

## 参数 (Parameters)

### Waterfall 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<T>?` | `null` | 获得/设置数据源 |
| `Columns` | `int` | `4` | 获得/设置列数 |
| `Gap` | `int` | `16` | 获得/设置列间距（像素） |
| `Breakpoints` | `Dictionary<string, int>?` | `null` | 获得/设置响应式断点 |
| `HasMore` | `bool` | `false` | 获得/设置是否还有更多数据 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnLoadMore` | `Func<Task>?` | 加载更多数据回调 |

---

## 最佳实践

1. **使用 Items 绑定数据**：推荐通过 `Items` 参数绑定数据，而不是在 Razor 中手动编写 item
2. **合理设置 Columns**：根据内容宽度设置列数，避免列数过多导致内容过窄
3. **使用响应式断点**：通过 `Breakpoints` 参数实现响应式布局，适配不同屏幕尺寸
4. **处理 OnLoadMore 事件**：对于需要无限滚动的场景，处理 `OnLoadMore` 事件加载更多数据
5. **设置 HasMore 控制加载**：通过 `HasMore` 参数控制是否还有更多数据，避免无效加载
6. **优化图片加载**：瀑布流中图片较多，考虑使用懒加载（lazy loading）优化性能
7. **与 Grid 布局的区别**：`Waterfall` 是瀑布流布局（高度不一），`Grid` 是网格布局（高度统一）
