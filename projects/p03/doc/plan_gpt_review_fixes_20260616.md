# P03 GPT 审查修复计划

> 2026-06-16 | GPT 审查结论: Request changes / 大修后可合并
> Exp 1c/2 径向结果保留，但 "物理层 robustness 完成" 需降级

## 任务链（顺序执行，每轮 Codex 审查→实现）

### Task 1: Fix Exp 1d — control-subtracted azimuthal continuity
- 当前: raw S_app sector means, f_pos 近恒等量, C_theta 定义错误
- 修复: displaced-control-subtracted E_sec, 新指标 (f_pos_E, D_pos, N_eff_E, Ctheta_vec)
- Codex 审查: ✅ 通过，核心方案正确
- 关键细化: mean_E>0 前置条件, D_pos NaN when no excess, sector-balanced C_θ, control-null metrics

### Task 2: Fix Exp 1e — pixel-level vorticity/OW decomposition
- 当前: ratio-of-means S/|ζ|, 无 control subtraction, signed ζ cancellation risk
- 修复: pixel-level |ζ|, normalized OW = (S²-ζ²)/(S²+ζ²), control subtraction

### Task 3: Patch Exp 1c — random control self-exclusion + save control coords
- 当前: random control 未显式排除 target eddy self
- 修复: 加 explicit d2self check, 保存 control center lat/lon

### Task 4: Exp 1f — multi-pass SwotDiag validation
- 当前: 仅 1 pass, r=0.85, 不在 review package 中
- 修复: ≥20 passes 或 ≥100 eddies, pixel-level + bin-level + annulus endpoint comparison

### Task 5: 文档更新 — README/DIRECTION/NARRATIVE 状态统一
- 三层状态: ✅ claim-grade / 🔶 prototype / 🔲 pending
- NARRATIVE 措辞修正 ("涡旋自身组织" → "eddy-associated")

### Task 6: GPT 再讨论 — 更新 summary, 打包重新发送

## 不在此轮修复的内容
- Cluster bootstrap: 用户此前明确不做, 延后讨论
- Background-strain matched control / isolated-eddy subset: Exp 3, 延后
- Cross-region extension: Stage 2, 延后
