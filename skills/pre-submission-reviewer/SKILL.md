# Skill: pre-submission-reviewer

## Purpose
对论文进行科学性、证据、结构、语言、图表、格式和投稿材料审查，按 CRITICAL/MAJOR/MINOR 分级，为每个问题标注应返回的 Skill。

## When to Use
- S7 内部审查阶段
- S8 投稿前最终检查

## Required Inputs
- 论文完整稿
- 证据账本
- 目标期刊要求

## Optional Inputs
- Cover Letter 草稿
- 实验运行记录

## Preconditions and Gate Checks
- 论文已完成
- G3、G4 状态已知

## Mandatory Procedure
1. 审查科学性（问题、方法、结论、逻辑）
2. 审查证据完整性
3. 审查结构
4. 审查语言
5. 审查图表
6. 审查格式和投稿材料
7. 问题分级：CRITICAL / MAJOR / MINOR
8. 为每个问题标注应返回的 Skill

## Prohibited Actions
- 不降低问题严重级别
- 不跳过任何审查维度

## Typical Fallbacks
- 语言问题 → paper-polish
- 结构问题 → paper-logic-builder
- 图件问题 → scientific-figure-designer
- 无证据结论 → evidence-ledger
- 实验不足 → experiment-auditor
- 协议问题 → protocol-freezer
- 文献与创新问题 → deep-research / idea-evaluator

## Required Outputs
- 审查报告（按 CRITICAL/MAJOR/MINOR 组织）

## Human Review
- 确认审查意见是否合理
- 决定哪些问题需要修改

## Completion Criteria
- 所有审查维度已完成
- 问题已分级
- 回退 Skill 已标注

## Failure and Fallback
- 问题过多：优先处理 CRITICAL 和 MAJOR

## Related Prompts
- [S7_internal_review.md](../../prompts/S7_internal_review.md)
