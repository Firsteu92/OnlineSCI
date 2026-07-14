# Skill: paper-logic-builder

## Purpose
建立论文主线、贡献、章节和段落结构，为每个论点分配证据、引用和图件，不直接撰写完整正文。

## When to Use
- S6 阶段，证据账本已就绪时
- 需要从零组织论文结构时

## Required Inputs
- 证据账本
- 核心发现和声明
- 目标期刊

## Optional Inputs
- 已有提纲草稿
- 图件草稿

## Preconditions and Gate Checks
- G3、G4 应已通过

## Mandatory Procedure
1. 确定论文核心故事线
2. 列出 2-4 条清晰、可验证的贡献声明
3. 构建章节级和段落级详细提纲
4. 为每个主要论点分配证据、引用和图件
5. 规划图件布局

## Prohibited Actions
- 不直接撰写完整正文
- 不编造不在证据账本中的结论
- 不过度承诺贡献

## Required Outputs
- `paper_story.md`
- `detailed_outline.md`
- `contribution_plan.md`
- `section_evidence_map.csv`

## Human Review
- 确认故事线是否清晰
- 确认每个论点有足够证据

## Completion Criteria
- 提纲覆盖论文全部章节
- 每个段落有明确的要点
- 证据分配完整

## Failure and Fallback
- 证据不足以支持论点：返回 S5 补充或调整
- 结构不合理：重新组织

## Related Prompts
- [S6_paper_logic.md](../../prompts/S6_paper_logic.md)
