# Skill: project-handoff

## Purpose
记录项目当前进度、关键文件、环境和运行方式、有效和失败结果、已排除路线、关键决定、未解决问题和下一步，为接手者提供完整上下文。

## When to Use
- S8 阶段项目完成或暂停时
- 项目交接给其他研究者时

## Required Inputs
- 完整项目状态（PROJECT.md、STATUS.md、project.yml）
- 所有产出和运行记录
- G0–G5 状态

## Optional Inputs
- 协作人员信息
- 未来计划

## Preconditions and Gate Checks
- G5 应已通过（项目已完成投稿前准备）

## Mandatory Procedure
1. 汇总项目进度（已完成、进行中、未完成）
2. 列出关键文件和目录索引
3. 记录环境配置和运行方式
4. 总结有效和失败结果
5. 记录已排除的研究路线
6. 记录关键决定和理由
7. 列出未解决问题和下一步建议
8. 标注禁止误改的内容

## Prohibited Actions
- 不编造不存在的结论
- 不省略失败的尝试
- 不标注未经验证的建议作为确定性信息

## Required Outputs
- `HANDOFF.md`
- `FILE_INDEX.md`
- `OPEN_ISSUES.md`
- `environment.yml`

## Human Review
- 确认交接文档完整
- 确认未省略重要信息

## Completion Criteria
- 所有交接产出文件已创建
- 项目状态可被新接手者快速理解

## Failure and Fallback
- 信息不全：补充后再生成交接文档

## Related Prompts
- [S8_submission_and_archive.md](../../prompts/S8_submission_and_archive.md)

## Related Templates
- [HANDOFF.md](../../templates/HANDOFF.md)
