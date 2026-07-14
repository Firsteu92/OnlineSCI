# Stage Gates — 质量门槛

G0–G5 是 OnlineSCI 的六道质量门槛。每道门槛规定了进入下一阶段前必须满足的条件。

## 门槛总览

| 门槛 | 名称 | 规则 |
|------|------|------|
| G0 | 项目建立 | 没有建立项目卡，不进入正式科研流程。 |
| G1 | 创新判断 | 没有完成真实、可核验的文献检索，不确认研究创新性。 |
| G2 | 正式实验 | 没有冻结实验协议，产生的结果只能视为探索性结果，不能认定为正式实验结果。 |
| G3 | 结论写作 | 没有完整运行记录和有效验证，不生成带有确定性结论的完整论文。 |
| G4 | 证据确认 | 没有建立证据账本，不形成或发布最终研究结论。 |
| G5 | 投稿状态 | 没有通过投稿前审查，不将项目标记为"可投稿"。 |

## 门槛推进顺序

```text
G0 建立项目
  → G1 核验创新
    → G2 冻结实验方案
      → G3 完成正式实验与有效验证
        → G4 建立结论证据链
          → G5 完成投稿前审查
```

## 写作权限与 G3/G4 的关系

- **G3 未通过**：只能写背景、文献、数据方法、实验计划和待验证提纲
- **G3 通过、G4 未通过**：可写 Results 和 Discussion 草稿，但不得定稿最终 Abstract、Conclusions 和贡献声明
- **G3、G4 均通过**：可以生成完整论文，但所有表述必须遵守证据账本

## 各门槛对应 Checklist

| 门槛 | 核验清单 |
|------|----------|
| G0 | [G0_project_card.md](../checklists/G0_project_card.md) |
| G1 | [G1_literature_and_innovation.md](../checklists/G1_literature_and_innovation.md) |
| G2 | [G2_protocol_freeze.md](../checklists/G2_protocol_freeze.md) |
| G3 | [G3_experiment_and_validation.md](../checklists/G3_experiment_and_validation.md) |
| G4 | [G4_evidence_ledger.md](../checklists/G4_evidence_ledger.md) |
| G5 | [G5_pre_submission.md](../checklists/G5_pre_submission.md) |
