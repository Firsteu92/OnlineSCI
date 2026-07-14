# Skill: idea-evaluator

## Purpose
基于已核验文献评价研究想法的新颖性、科学意义、可验证性、可行性和发表潜力，检查致命缺陷，给出决策建议。

## When to Use
- S1 阶段文献检索完成后
- 需要决定是否继续推进一个研究方向时

## Required Inputs
- 已核验的文献列表
- 研究问题和核心假设
- 可用数据和方法描述

## Optional Inputs
- 风险评估偏好
- 目标期刊要求

## Preconditions and Gate Checks
- 文献检索已完成（deep-research 已执行）
- 文献引用已人工核验
- G1 未通过时，不得确认创新

## Mandatory Procedure
1. 审查文献检索结果
2. 按五个维度评分：新颖性、科学意义、可验证性、可行性、发表潜力
3. 检查致命缺陷
4. 给出最终决定：PROCEED / PROCEED_WITH_CHANGES / HOLD / STOP
5. 为 HOLD 或 STOP 提供明确理由

## Prohibited Actions
- 不基于未核验的文献做判断
- 不忽略明显的致命缺陷
- 不替用户做最终决定（只提供建议）

## Required Outputs
- `idea_evaluation.md` — 多维度评估报告
- `risk_register.md` — 风险登记册
- `decision.md` — 最终决定

## Human Review
- 确认评分是否合理
- 确认致命缺陷分析是否完整
- 做出最终推进决定

## Completion Criteria
- 五个维度均已评分
- 致命缺陷已检查
- 最终决定已给出

## Failure and Fallback
- 文献不足无法判断：退回 deep-research 补充
- 评分矛盾：重新评估，说明理由

## Related Prompts
- [S1_idea_evaluation.md](../../prompts/S1_idea_evaluation.md)

## Related Templates
- [decision_record.md](../../templates/decision_record.md)
