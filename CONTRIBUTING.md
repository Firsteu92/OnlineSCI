# Contributing Guide — 参与指南

欢迎加入 OnlineSCI！本文档帮助你快速上手参与项目。

## 快速开始

### 1. Fork 与 Clone

```bash
# Fork 本仓库到你的 GitHub 账号（在 GitHub 页面点击 Fork 按钮）
# 然后 clone 你的 fork
git clone https://github.com/YOUR_USERNAME/OnlineSCI.git
cd OnlineSCI
git remote add upstream https://github.com/Firsteu92/OnlineSCI.git
```

### 2. 选择项目

浏览 [projects/DASHBOARD.md](projects/DASHBOARD.md) 了解当前所有项目的状态。

- 在感兴趣的项目 Issue 下留言表达参与意向
- 或直接提一个新的 Issue 提出你的研究想法

### 3. 创建分支

```bash
# 同步最新代码
git fetch upstream
git merge upstream/main

# 为你的工作创建分支
git checkout -b p01/feature/your-work-description
```

分支命名规范：`p##/feature/描述` 或 `p##/s#-stage-description`

### 4. 提交工作

```bash
# 添加你的修改
git add projects/p01/analysis/your_script.py
git add projects/p01/figures/fig01.png

# 提交（遵循 commit message 规范）
git commit -m "[P01] S1: add literature review"

# 推送到你的 fork
git push origin p01/feature/your-work-description
```

### 5. 提交 PR

在 GitHub 上从你的分支向 upstream/main 发起 Pull Request，按照 PR 模板填写描述。

## Commit Message 规范

格式：`[P##] S#: 简要描述`

```
[P01] S0: 初始化项目卡
[P01] S1: 文献综述和参考文献核验
[P01] S4: 正式实验运行记录
```

## 文件组织

每个项目目录是自包含的，详见 [projects/_template/](projects/_template/)。

## 几个关键规则

1. **不上传原始数据**：只提交数据链接和下载脚本
2. **不编造文献**：AI 生成的每条引用必须经人工核验
3. **写清环境依赖**：脚本开头注明依赖库
4. **图表可复现**：图表必须有对应的生成脚本

## 需要帮助？

- 在 GitHub Issue 中提问，标题格式：`[Help] 你的问题`

*详细的协作制度和署名规则见 [COLLABORATION.md](COLLABORATION.md)*
