# S7：内部审查 / Internal Review

## 什么时候使用

论文初稿或修改稿完成后，需要在投稿前进行全面内部审查时。

## 使用前需要准备

- 已完成论文初稿或修改稿
- 证据账本和实验记录

## 可直接复制的 Prompt

```
# Role
你是一个严格的学术审稿人。请对以下论文进行同行评议级别的审查。

# Manuscript
[粘贴论文全文]

# Evidence Ledger
[粘贴或引用证据账本]

# Target Journal
[目标期刊]

# Review Focus
[提交者希望审查者重点关注的方面]

# Instructions
请按以下维度进行审查：

1. **科学性**：
   - 研究问题是否清晰重要
   - 方法是否适合问题
   - 结论是否有数据充分支持
   - 逻辑链是否完整

2. **证据完整性**：
   - 每项主要声明是否有对应证据
   - 是否有无证据支持的结论
   - 冲突结果是否被讨论

3. **结构**：
   - 论文结构是否合理
   - 故事线是否清晰
   - 各部分之间衔接是否自然

4. **语言**：
   - 是否清晰准确
   - 是否有 AI 腔
   - 术语是否一致

5. **图表**：
   - 是否清晰易读
   - 标注是否完整
   - 是否准确反映结果

6. **格式与投稿材料**：
   - 是否符合目标期刊要求
   - 必要声明是否完整

# Issue Severity
问题分级：
- CRITICAL：必须修改，否则不能投稿
- MAJOR：建议修改，否则降低发表概率
- MINOR：小问题，可选择修改

# Fallback
对每个问题，注明应返回哪个 Skill 处理：
- 语言问题 → paper-polish
- 结构问题 → paper-logic-builder
- 图件问题 → scientific-figure-designer
- 无证据结论 → evidence-ledger
- 实验不足 → experiment-auditor
- 协议问题 → protocol-freezer
- 文献与创新问题 → deep-research / idea-evaluator
```

## 期望输出

- 逐项审查意见（按 CRITICAL/MAJOR/MINOR 分级）
- 每个问题的 Skill 回退建议

## 人类审查重点

- [ ] 审查意见是否合理
- [ ] 是否有被忽略的重大问题

## 保存位置

将审查意见记录在 Issue 或 PR 中

## 下一门槛

审查通过后进入 S8（或返回相应阶段修改）
