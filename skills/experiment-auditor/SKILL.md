# Skill: experiment-auditor

## Purpose
执行正式运行前检查、Run Manifest 记录、运行后审计、协议符合性检查、泄漏检查和可复现性检查，判定运行状态。

## When to Use
- S3 中运行前检查
- S4 中正式实验执行和审计
- S5 中验证分析

## Required Inputs
- 冻结协议（protocol_v001.md/yml）
- 运行参数和代码
- 运行环境说明

## Optional Inputs
- 历史运行记录

## Preconditions and Gate Checks
- S4 前：G2 应已通过
- 协议已冻结且版本已知

## Mandatory Procedure
1. **运行前检查**：验证数据可用、代码可运行、参数与协议一致
2. **执行**：运行实验，记录所有输出
3. **运行后审计**：
   - 协议符合性检查
   - 泄漏检查（数据、时间、空间、标签、未来信息）
   - 可复现性检查
4. **状态判定**：从以下状态中选择一个
   - `exploratory` — 探索性
   - `formal_valid` — 正式有效
   - `formal_invalid` — 正式无效
   - `superseded` — 被取代
   - `reproduction_failed` — 复现失败
5. 记录 Run Manifest

## Prohibited Actions
- **禁止删除失败实验或只保留最佳结果**
- 不跳过审计步骤
- 不修改运行状态判定规则

## Required Outputs
- `RUN_INDEX.csv` — 运行索引
- `runs/<RUN-ID>/manifest.yml` — 运行清单
- `runs/<RUN-ID>/audit.md` — 审计报告

## Human Review
- 确认审计结论是否准确
- 确认失败实验已被记录

## Completion Criteria
- 运行记录完整
- 审计完成
- 运行状态已判定

## Failure and Fallback
- 运行前检查失败：修复问题后重试
- 协议偏差：创建新协议版本或标记结果

## Related Prompts
- [S3_build_and_explore.md](../../prompts/S3_build_and_explore.md)
- [S4_formal_experiments.md](../../prompts/S4_formal_experiments.md)

## Related Templates
- [run_manifest.yml](../../templates/run_manifest.yml)
