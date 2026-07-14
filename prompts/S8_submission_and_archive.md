# S8：投稿准备与项目归档 / Submission and Archive

## 什么时候使用

论文已完成内部审查，需要准备投稿材料和项目交接时。

## 使用前需要准备

- G5 已通过（投稿前审查已完成）
- 论文终稿

## 可直接复制的 Prompt

```
# Role
你是一个投稿准备和项目归档助手。请帮我完成投稿准备和交接文档。

# Final Manuscript
[粘贴或描述论文终稿]

# Target Journal
[目标期刊]

# Instructions
请帮我完成以下任务：

### 1. 投稿材料
- **Cover Letter**：突出核心贡献，说明为什么适合该期刊
- **Data Availability Statement**：说明数据获取方式
- **AI Usage Declaration**：如实声明 AI 参与方式
- **CRediT Author Contribution Statement**：按 CRediT 标准列出作者贡献

### 2. 投稿前检查清单
- 格式是否符合目标期刊要求
- 字数、图表数量是否在限制内
- 参考文献格式是否正确
- 所有必要声明是否完整

### 3. 项目交接文档
- **HANDOFF.md**：项目进度、关键决定、未解决问题
- **FILE_INDEX.md**：所有文件的索引
- **OPEN_ISSUES.md**：尚未关闭的问题
- **environment.yml**：完整的运行环境

# Constraints
- Cover Letter 中提议的审稿人需人工核验
- 不编造数据可用性信息
- 交接文档应为接手者提供足够信息

# Output
- Cover Letter
- 投稿材料
- 交接文档（HANDOFF.md, FILE_INDEX.md, OPEN_ISSUES.md, environment.yml）
```

## 期望输出

- Cover Letter
- 投稿材料
- 项目交接文档

## 人类审查重点

- [ ] AI 使用声明是否如实
- [ ] 审稿人建议是否合理
- [ ] 交接文档是否完整

## 保存位置

`projects/pXX/manuscript/submission/`、`projects/pXX/handoff/`

## 下一门槛

**G5**：必须通过才能标记为"可投稿"
