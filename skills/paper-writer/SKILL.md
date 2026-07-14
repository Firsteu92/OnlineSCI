# Skill: paper-writer

## Purpose
根据已批准的结构和证据撰写论文各部分，严格遵守 G3、G4 写作权限。

## When to Use
- S7 阶段，论文逻辑已确定时
- 需要撰写特定章节时

## Required Inputs
- 论文提纲和结构
- 证据账本
- 写作权限（基于 G3/G4 状态）
- 目标期刊

## Optional Inputs
- 已有草稿
- 参考文献列表

## Preconditions and Gate Checks
- 写作权限规则：
  - G3 未通过：只能写背景、文献、数据方法、实验计划和待验证提纲
  - G3 通过、G4 未通过：可写 Results 和 Discussion 草稿，不得定稿 Abstract、Conclusions 和贡献声明
  - G3、G4 均通过：可写完整论文，但所有表述必须遵守证据账本

## Mandatory Procedure
1. 确认当前写作权限
2. 根据提纲逐部分撰写
3. 每部分引用对应的证据和文献
4. 确保表述不超过证据范围

## Prohibited Actions
- **禁止创造数据、文献、实验和结论**
- 不超出写作权限范围
- 不编造引用

## Required Outputs
- `manuscript/v1_ai_draft/` 下的论文初稿

## Human Review
- 确认内容在写作权限范围内
- 确认无无证据支撑的声明

## Completion Criteria
- 所有指定部分已完成
- 内容在权限范围内
- 引用和证据已标注

## Failure and Fallback
- 证据不足无法撰写：返回相应阶段补充
- 结构问题：返回 paper-logic-builder 调整

## Related Prompts
- [S7_paper_writing.md](../../prompts/S7_paper_writing.md)
