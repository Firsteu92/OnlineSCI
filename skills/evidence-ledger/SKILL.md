# Skill: evidence-ledger

## Purpose
建立声明-文献-实验-图表-数据之间的映射，判定证据强度，控制允许使用的结论强度，记录无证据和冲突声明。

## When to Use
- S5 阶段，正式实验完成后
- 写作前需要确认哪些结论有充分证据支持时

## Required Inputs
- 实验运行记录
- 文献检索结果
- 论文主要声明列表

## Optional Inputs
- 验证结果
- 图表清单

## Preconditions and Gate Checks
- G3 应已通过（正式实验和验证已完成）

## Mandatory Procedure
1. 列出论文可能做出的所有主要声明
2. 为每条声明匹配证据来源（文献、实验、图表、数据）
3. 判定每条声明的证据状态
4. 记录无证据和冲突声明
5. 控制结论表述强度（与证据强度匹配）

## Prohibited Actions
- 不夸大证据强度
- 不忽略冲突或否定性证据
- 不创建无证据的声明

## Evidence Status Values
- `supported` — 有充分证据支持
- `partially_supported` — 部分支持
- `conflicting` — 证据冲突
- `unsupported` — 无证据支持
- `pending` — 待补充
- `rejected` — 已被证伪

## Required Outputs
- `claims.csv`
- `claim_evidence_matrix.csv`
- `evidence_ledger.md`
- `unsupported_claims.md`
- `conflicts.md`

## Human Review
- 确认每项声明的证据强度是否合理
- 确认无遗漏的冲突证据

## Completion Criteria
- 所有论文声明已列出
- 每条声明有证据状态
- 无证据声明已标注

## Failure and Fallback
- 实验数据不足：返回 S4 补充实验
- 文献证据不足：返回 S1 补充检索

## Related Prompts
- [S5_validation_and_evidence.md](../../prompts/S5_validation_and_evidence.md)

## Related Templates
- [claim_evidence_matrix.csv](../../templates/claim_evidence_matrix.csv)
