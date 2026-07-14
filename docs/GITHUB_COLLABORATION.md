# GitHub Collaboration — GitHub 协作规范

## GitHub 的角色

在 OnlineSCI 中，GitHub 主要承担以下职责：

- 发布和分发 OnlineSCI 工具包
- 保存项目结构和轻量产出
- 记录修改历史
- 通过 Issue 讨论科学问题
- 通过 Pull Request 进行审查
- 支持多人协作
- 归档投稿版本和返修过程

## 不宜提交的内容

以下内容**不得**提交到 GitHub 仓库：

- 密钥、Token、密码
- 涉密或受限数据
- 未匿名化个人数据
- 大型原始数据文件
- 违反许可的数据
- Agent 私密凭证
- 未确认可公开的论文稿件

## Commit 规范

格式：`[P##] S#: 简要描述`

```
[P01] S0: 初始化项目卡
[P01] S1: 文献综述和参考文献核验
[P01] S4: 正式实验运行记录
...
```

## Branch 规范

- 主分支：`main`
- 每个项目使用独立分支：`p01/main`、`p02/main`
- 功能分支：`p01/feature/<description>`

## Issue 规范

- 标题格式：`[P##] 简要描述`
- 使用 Label 标记项目编号和阶段（`P01`、`S0` 等）
- 关键科学决策必须有 Issue 记录

## PR 规范

- 每个阶段完成后可提交 PR
- PR 描述中列出本阶段的关键产出和变更
- PR 模板包含 G 门槛检查和 AI 使用声明
- PR 合并需要至少 1 位参与者的 Review
