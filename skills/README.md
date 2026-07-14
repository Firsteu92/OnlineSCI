# Skills — Agent 任务规范

本目录包含 12 个核心 Skills，每个 Skill 定义了 Agent 在执行科研任务时必须遵守的完整规范。

## 使用方式

1. 在 [SKILL_INDEX.md](../SKILL_INDEX.md) 中找到你的任务对应的 Skill
2. 阅读对应 `skills/<skill-name>/SKILL.md`
3. 了解该 Skill 的输入、步骤、禁止事项和产出
4. 用对应的 Prompt（在 `prompts/` 目录）指导 Agent 执行

## Skill 列表

| Skill | 用途 | 对应阶段 |
|-------|------|----------|
| [project-context](project-context/SKILL.md) | 项目上下文管理 | S0 |
| [deep-research](deep-research/SKILL.md) | 深度文献检索 | S1 |
| [idea-evaluator](idea-evaluator/SKILL.md) | 创新性评价 | S1 |
| [protocol-freezer](protocol-freezer/SKILL.md) | 实验协议冻结 | S2 |
| [experiment-auditor](experiment-auditor/SKILL.md) | 实验审计 | S3/S4/S5 |
| [evidence-ledger](evidence-ledger/SKILL.md) | 证据账本管理 | S5 |
| [paper-logic-builder](paper-logic-builder/SKILL.md) | 论文逻辑构建 | S6 |
| [scientific-figure-designer](scientific-figure-designer/SKILL.md) | 科学图件设计 | S6 |
| [paper-writer](paper-writer/SKILL.md) | 论文撰写 | S7 |
| [paper-polish](paper-polish/SKILL.md) | 论文润色 | S7 |
| [pre-submission-reviewer](pre-submission-reviewer/SKILL.md) | 投稿前审查 | S7/S8 |
| [project-handoff](project-handoff/SKILL.md) | 项目交接 | S8 |
