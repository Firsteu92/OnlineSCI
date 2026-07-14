# OnlineSCI v1 系统概述

## 定位

OnlineSCI v1 是一套**从 GitHub 下载即可使用的标准化 AI 辅助科研工作流工具包**。它不是必须安装的自动 Agent 程序，也不是单纯的论文写作规范。

## 核心组成

1. **标准化 AI 科研工作流**（S0–S8）
2. **可复制的 AI Flow 提示词**（prompts/）
3. **Agent 任务规范**（skills/）
4. **质量门槛**（G0–G5）
5. **人工审查清单**（checklists/）
6. **空白项目模板**（projects/）
7. **GitHub 科研协作规范**（docs/）

## 典型使用方式

```text
下载或克隆 OnlineSCI
  → 选择 P01–P10 中一个空白项目
  → 在 AI_WORKFLOW_GUIDE.md 中判断当前阶段
  → 复制对应 Prompt
  → 在 ChatGPT、Claude、Codex、Cursor 等 Agent 中执行
  → 人工检查 Agent 输出
  → 按 G0–G5 判断是否允许进入下一阶段
  → 将结果保存到规定项目目录
  → 有协作需求时提交到 GitHub
```

## 设计原则

- **人类在环路中**（Human-in-the-Loop）：AI 负责执行，人类负责审核
- **不依赖特定 Agent 品牌**：Prompt 通用，可在任意 LLM 中使用
- **可复现**：每步的输入、输出、参数和决策都有记录
- **可追溯**：Git 记录完整变更历史
- **透明**：AI 使用方式完全披露

## 本次不做

- 不开发自动 Router 程序
- 不开发网页界面
- 不开发数据库
- 不包含具体学科领域包
- 不加入复杂 CI
- 不自动提交或推送 GitHub
