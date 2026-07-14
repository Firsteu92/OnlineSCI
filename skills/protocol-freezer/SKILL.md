# Skill: protocol-freezer

## Purpose
在正式实验前冻结研究假设、数据范围、基线、指标和验证方案，确保实验可复现、可审计。

## When to Use
- S2 阶段，正式实验开始前
- 实验方案需要团队确认时

## Required Inputs
- 研究假设
- 可用数据描述
- 评价指标

## Optional Inputs
- 已有基线方法
- 计算资源限制

## Preconditions and Gate Checks
- G1 应已通过（创新已确认）
- 研究假设已明确

## Mandatory Procedure
1. 明确可检验的研究假设（H0/H1）
2. 确定数据范围和划分方式（训练/测试/验证）
3. 确定基线和主/次评价指标
4. 设计主实验、消融、鲁棒性和独立验证方案
5. 设定失败标准
6. 建立协议变更规则（变更必须创建新版本）
7. 输出 protocol_v001.md 和 protocol_v001.yml

## Prohibited Actions
- 不创建无版本号的协议
- 不修改已冻结协议（只能创建新版本）
- 不规定无法测量的指标
- 不省略失败标准

## Required Outputs
- `protocol_v001.md` — 协议正文
- `protocol_v001.yml` — 结构化版本
- `CHANGELOG.md` — 变更日志

## Human Review
- 确认假设可检验
- 确认指标合理
- 确认失败标准明确

## Completion Criteria
- 协议包含所有必需字段
- 版本号已标注
- 变更规则已建立

## Failure and Fallback
- 假设不可检验：返回 S1 重新定义
- 数据不可用：返回 S3 准备数据

## Related Prompts
- [S2_protocol_freeze.md](../../prompts/S2_protocol_freeze.md)

## Related Templates
- [protocol.md](../../templates/protocol.md)
- [protocol.yml](../../templates/protocol.yml)
