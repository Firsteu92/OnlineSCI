# AI Usage and Logging — AI 使用与日志规范

## 基本原则

- **透明记录**：所有关键 AI 交互必须保存日志
- **人类核验**：AI 输出必须经人工审查后方可使用
- **不编造**：AI 不得编造文献、数据、实验结果
- **完全披露**：投稿时在 Methods 或 Acknowledgements 中如实披露 AI 参与方式

## AI 交互日志格式

每次关键 AI 交互记录在 `logs/` 目录，文件名格式：`YYYY-MM-DD_S#_task.md`

```markdown
# AI Interaction Log

- Date: 2026-07-14
- Stage: S1
- Model: Claude Opus 4
- Task: 文献检索——海洋涡旋识别方法
- Duration: ~30 min

## Prompt Summary
[简述给 AI 的指令]

## Key Output
[AI 输出的关键结果摘要]

## Human Assessment
[人类对 AI 输出质量的简要评价：哪些可用、哪些需要修改、哪些被拒绝]
```

## AI 使用披露模板（投稿用）

```
The authors used [AI Model/Tool Name] for [specific tasks, e.g., literature
search, code generation, figure design, language polishing]. All AI-generated
content was reviewed and verified by the human authors, who bear full
responsibility for the scientific accuracy and integrity of this work.
```

## 质量红线

- **文献幻觉零容忍**：AI 生成的每一条参考文献，必须通过 Google Scholar / Crossref 进行人工核验
- **结果验证**：AI 给出的任何数值结果，必须由领域专家进行合理性检查
- **代码可复现**：AI 生成的所有代码必须能在标准环境中复现
