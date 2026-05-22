---
name: pr-auto-review-skill
description: 自动拉取 GitHub PR 或 GitLab MR 到本地临时分支，进行代码差异对比和 Code Review。当用户提到"PR Review"、"代码审查"、"Review PR"、"拉取PR"、"对比PR变更"时触发此 Skill。使用纯 git 命令，不依赖 gh/glab CLI。支持提供 PR/MR URL 自动完成：解析URL→git fetch拉取→本地创建临时分支→git diff获取变更→AI 代码审查→输出 Markdown 格式 Review 报告。
---

# PR Auto Review Skill

## 功能概述

此 Skill 使用纯 git 命令完成所有操作，不依赖 gh/glab CLI。

工作流程：

1. **解析 PR/MR URL** - 从用户提供的 URL 中提取平台、仓库、PR 编号
2. **验证 git remote** - 确保本地仓库的 remote 配置正确
3. **git fetch 拉取 PR** - 使用 git fetch 拉取远程 PR/MR 分支到本地
4. **创建临时分支** - 创建本地临时分支（如 pr/xxx）
5. **git diff 获取变更** - 获取所有变更的文件和内容
6. **AI Code Review** - 以资深后端架构师身份进行代码审查
7. **输出 Markdown 报告** - 生成结构化的 Review 报告

## 使用场景

- 同事提交了 PR，需要在合并前进行本地代码审查
- 需要对比 PR 的具体变更内容
- 希望在本地运行和测试 PR 的代码

## 核心设计原则

- **纯 git 命令**：不依赖 gh/glab 等额外 CLI 工具
- **通用兼容**：同时支持 GitHub 和 GitLab 的 PR/MR 格式
- **最小依赖**：只需要 git 和网络访问仓库

## 执行流程

### 步骤 1：解析 PR URL

从用户提供的 URL 中提取以下信息：

| 平台 | URL 示例 | 提取信息 |
|------|----------|----------|
| GitHub | `https://github.com/owner/repo/pull/123` | owner/repo, pr-number: 123 |
| GitHub | `https://github.com/owner/repo/-/merge_requests/123` | owner/repo, pr-number: 123 |
| GitLab | `https://gitlab.com/owner/repo/-/merge_requests/456` | owner/repo, mr-number: 456 |
| GitLab | `https://repo.rfnetech.com/group/project/-/merge_requests/308/` | owner/repo, mr-number: 308 |

正则表达式：

- GitHub PR: `github\.com/([^/]+)/([^/]+)/(?:pull|/merge_requests/)(\d+)`
- GitLab MR: `gitlab[^/]*/([^/]+)/([^/]+)/-/(?:merge_)?requests/(\d+)`

注意：内网 GitLab（如 `repo.rfnetech.com`）的 URL 格式可能包含 `/`- prefix.

### 步骤 2：克隆仓库到临时目录

对于每个 PR Review，使用临时目录避免污染现有仓库：

```bash
# 创建临时目录
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

# 克隆仓库（使用 deep clone 加速）
git clone --depth 1 <仓库URL> .
```

### 步骤 3：查找 MR 的源分支

找到 MR 对应的源分支是正确 diff 的关键：

```bash
# 方法1：查看 MR 分支包含的 commits
git branch -a --contains mr/<number>

# 方法2：查找包含特定 issue 编号的 commits
git log --oneline --all --grep="#<issue-number>"

# 方法3：直接对比 MR 的源分支与目标分支
# 在 GitLab MR 页面可以看到 source branch 和 target branch
# 例如：source: 400-wrongstatus -> target: main
# 则对比：git diff main..origin/400-wrongstatus
```

**常见源分支模式**：
- `issue-<number>-<description>`
- `fix-<number>-<description>`
- `feature-<number>-<description>`
- `sprint-<version>`

### 步骤 4：获取正确的 diff

**关键**：不要直接用 `main..HEAD` 或 `mr/XXX..main`，因为 MR 可能包含大量历史 commits。

正确的对比方式：

```bash
# 方法1：对比 MR 分支与目标分支（推荐）
git diff <target-branch>..origin/<source-branch>

# 方法2：如果知道 MR 的 base commit（从 MR 页面获取）
git diff <base-commit>..mr/<number>

# 方法3：先找到 MR 真正开始的 commit
git log --oneline mr/<number> | tail -1  # 找到最旧的 commit
```

验证文件数量：
```bash
git diff <target>..<source> --stat
# 应该只有 10-50 个文件才算正确
```

### 步骤 5：获取差异文件

**必须使用 `-w` 参数忽略空白变化！**

```bash
# ❌ 错误：包含大量空白变化，导致 diff 很大
git diff <base-branch>...HEAD

# ✅ 正确：忽略空白变化，只显示实际代码变更（推荐）
git diff -w <base-branch>...HEAD

# 获取忽略空白变化的文件统计（用于确认实际变更范围）
git diff -w <base-branch>..HEAD --stat
```

**为什么必须用 `-w`？**
- 空白变化（空格、Tab、换行符）会导致 diff 虚假地变大
- 大量文件可能只是格式调整，没有实际代码逻辑变更
- 使用 `-w` 才能精准识别真正的代码变更

**验证实际变更范围**：
```bash
# 对比包含空白 vs 忽略空白的文件数
git diff <base-branch>..HEAD --stat           # 包含空白
git diff -w <base-branch>..HEAD --stat         # 忽略空白
# 两者差异很大时，说明有大量格式调整
```

### 步骤 6：编译检查（重要！）

**在 Code Review 之前，必须先验证代码能否编译通过！**

```bash
# 根据项目类型选择编译命令：
# .NET/C# 项目
dotnet build

# Java 项目
mvn compile  # 或 gradle build

# Node.js 项目
npm run build

# Go 项目
go build ./...
```

**编译检查的意义**：
- 如果编译失败，说明 PR 存在明显问题（缺少文件、类型错误、语法错误等）
- 编译失败时，Review 报告中必须标注，并给出 ❌ 暂不合并 的建议
- 编译通过后再进行代码逻辑审查

**编译失败时的处理**：
- 记录编译错误信息
- 在 Review 报告中标注编译状态为"失败"
- 给出具体的错误信息

### 步骤 7：AI Code Review

以 **资深后端架构师** 身份进行深度 Code Review。不仅仅是找 Bug，还要发现代码改进机会。

#### 审查策略 - 如何让 AI 有效发现问题

**1. 代码审查是「找问题」不是「写好评」**
- 不要只写"代码很好"，要具体指出哪里可以改进
- 即使没有严重 Bug，也应该找到代码优化点
- 每一行修改的代码都值得仔细审视

**2. 审查维度（实用版）**

请从以下角度逐个检查修改的代码：

| 维度 | 审查要点 | 问题示例 |
|------|----------|----------|
| **逻辑正确性** | 边界条件、空值处理、异常分支 | 是否处理了 null？循环是否会死循环？ |
| **资源管理** | 连接关闭、内存释放、异常时资源释放 | finally 块是否正确释放资源？ |
| **并发安全** | 共享变量、静态字段、线程安全 | 多线程访问是否有锁保护？ |
| **安全风险** | 敏感信息、日志输出、参数校验 | 密码是否明文？日志是否泄露 PII？ |
| **代码质量** | 重复代码、魔法值、方法过长 | 是否有 copy-paste？常量是否提取？ |
| **业务逻辑** | 业务流程、状态转换、权限控制 | 逻辑是否符合需求？是否漏了分支？ |

**3. 审查时的关键问题**

对每个修改的文件，逐条检查：
- 这段代码在什么场景下会出错？
- 如果输入是 null/空/边界值会怎样？
- 异常情况下是否正确处理？
- 是否有资源泄露风险？
- 变量命名是否清晰易懂？

**4. 输出格式**

不要只输出"无"。即使代码质量不错，也应该：
- 指出代码亮点
- 提出改进建议（即使是 minor 级别）
- 给出具体的代码示例

### 步骤 8：评分与合并建议逻辑（关键！）

**评估规则**：合并建议必须与问题级别对应，不能自相矛盾！

| 问题级别 | 数量 | 合并建议 |
|----------|------|----------|
| 严重问题(必须修复) | ≥1 | ❌ 需要大幅修改 |
| 严重问题(必须修复) | 1-2 个 | ⚠️ 建议修改后合并 |
| 严重问题(必须修复) | 0 且 改进建议 > 5 | ⚠️ 建议修改后合并 |
| 无严重问题 | 0-3 个改进建议 | ✅ 可以合并 |
| 无严重问题 | 0 个改进建议 | ✅ 建议合并 |

**评分标准**：
- 严重问题(Must Fix)：会导致功能错误、数据丢失、安全漏洞、运行时崩溃的问题
- 改进建议(Should Fix)：代码质量、可维护性、性能优化等问题
- 亮点(Good)：值得肯定的优秀实现

### 步骤 9：输出 Review 报告

使用以下实用格式输出：

```markdown
# Code Review 报告

**MR #<编号>** | **<owner>/<repo>** | **<source> → <target>**

## 编译状态
✅ 编译通过 / ❌ 编译失败

## 变更概述
- 文件变更：<n> 个文件 (+<add> / -<del> 行)

## 审查结果

### 🔴 严重问题（Must Fix - 必须修复，阻止合并）
- **[问题标题]** (<文件>:<行号>)
  - 问题描述：<具体描述>
  - 影响：<会导致什么问题>
  - 建议：<修复方案>

### 🟡 改进建议（Should Fix - 推荐处理）
- **[改进标题]** (<文件>:<行号>)
  - 问题描述：<具体描述>
  - 建议：<改进方案>

### 🟢 代码亮点
- <亮点描述>

## 总结
- 严重问题数量：<n> 个
- 改进建议数量：<n> 个
- 合并建议：⚠️ 建议修改后合并 / ✅ 可以合并 / ❌ 需要大幅修改
```

**重要**：
- 编译状态必须放在第一位！编译失败时直接给出 ❌ 暂不合并 的建议
- 严重问题数量 ≥1 时，结论必须是"⚠️ 建议修改后合并"或"❌ 需要大幅修改"
- 结论必须与问题数量对应，不能自相矛盾！
- 问题描述要说明"影响什么"，不只是"是什么"

**重要**：
- 即使没有严重问题，也要输出改进建议和代码亮点
- 不要输出"无"就结束，要让审查报告有内容
- 每个问题都要有文件路径和行号
- 建议要有具体的代码示例

注意：
- 每个问题必须明确标注文件路径和行号
- 必须引用 SonarQube 规则编号（如 java:S2259）
- 修复建议必须提供具体的代码片段
- 没有问题的模块直接写"无"，不要编造问题

## 错误处理

| 错误类型 | 处理方式 |
|----------|----------|
| PR 不存在 | 提示检查 PR 编号是否正确 |
| 权限不足 | 提示需要仓库的读取权限 |
| 网络错误 | 提示检查网络连接 |

## 依赖工具

- Git