# S0：项目建立 / Project Setup

## 什么时候使用

当你需要一个正式的项目结构来启动新研究方向时。

## 使用前需要准备

- 选择一个空白项目位（P01–P10）
- 准备核心研究问题的初步描述

## 可直接复制的 Prompt

```
# Role
你是一个科研项目规划助手。请帮助我建立一个新的研究项目。

# Research Question
我的研究问题是：[在此输入 1-2 句话描述核心研究问题]

# Instructions
请帮我完成以下任务：

1. **项目卡**：基于我的研究问题，生成一份项目卡（PROJECT.md），包含：
   - 研究问题
   - 核心假设
   - 预期方法路线
   - 所需资源
   - 已知限制

2. **状态初始化**：生成初始 STATUS.md，包含：
   - 当前阶段：S0
   - G0-G5 全部标记为 not_checked
   - 各组件状态（data、code、protocol、evidence、manuscript）

3. **项目 YAML**：生成 project.yml，包含必要字段

# Constraints
- 不要编造文献、数据或实验结果
- 不要写入无法确认的研究假设
- 输出格式使用 Markdown，方便保存到项目目录

# Output
请输出以下三个文件的内容：
1. PROJECT.md
2. STATUS.md
3. project.yml

告诉我把它们保存到 projects/pXX/ 目录下。
```

## 期望输出

- 三个完整的项目初始化文件
- 项目卡包含清晰的研究方向和边界

## 人类审查重点

- 研究问题是否准确反映你的意图
- 假设是否合理
- 项目范围是否可控

## 保存位置

保存到 `projects/pXX/PROJECT.md`、`projects/pXX/STATUS.md`、`projects/pXX/project.yml`

## 下一门槛

G0：使用 [G0_project_card.md](../checklists/G0_project_card.md) 检查后进入 S1
