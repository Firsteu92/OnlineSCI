# Skill: deep-research

## Purpose
进行真实、可核验的文献检索，分析研究现状、共识、争议和最接近工作，区分已确认空白和待核验空白。

## When to Use
- S1 阶段进行文献调研时
- 需要了解某个方向的研究现状时
- 论文 Discussion 中需要与已有工作对比时

## Required Inputs
- 研究问题或关键词
- 检索范围（领域、年限）

## Optional Inputs
- 已知的核心文献
- 目标期刊列表

## Preconditions and Gate Checks
- G0 应已通过（项目已建立）

## Mandatory Procedure
1. 检索相关文献（使用真实检索工具或明确提示 AI 使用已知文献）
2. 核验每篇文献的 DOI 和作者
3. 总结研究现状、共识和争议
4. 找出最接近的已有工作
5. 分析研究空白——区分"已确认"和"待核验"
6. 输出结构化文献清单

## Prohibited Actions
- **禁止编造论文、作者、DOI 和结论**
- **禁止将"没搜到"直接认定为"首次发现"**
- 不忽略明显相关的重要工作
- 不歪曲已有文献的结论

## Required Outputs
- `literature_review.md` — 文献综述
- `reference_ledger.csv` — 文献账本
- `closest_prior_work.md` — 最接近工作分析

## Human Review
- 每条引用必须通过 Google Scholar / Crossref 核验
- 确保无编造引用
- 确认未遗漏关键文献

## Completion Criteria
- 至少覆盖该方向核心文献
- 每篇文献有 DOI 和核验状态
- 研究空白已识别

## Failure and Fallback
- 搜索范围太窄导致文献不足：扩展检索词或范围
- 发现关键文献被遗漏：补充后重新分析

## Related Prompts
- [S1_deep_research.md](../../prompts/S1_deep_research.md)

## Related Templates
- [literature_review.md](../../templates/literature_review.md)
- [reference_ledger.csv](../../templates/reference_ledger.csv)
