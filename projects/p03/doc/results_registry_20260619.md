---
title: P03 Results Registry
date: 2026-06-19
purpose: 每张图、每个 .mat 产物对应的脚本/参数/样本量索引；PR 审稿和后续复现用
---

# P03 Results Registry — 2026-06-19

> 跟随 `PR_2026-06-19_midterm_review.md` 一起阅读。
> 路径以 OpenSCI-Ocean repo 为相对根。HPC 路径前缀: `/slurm/zhangzs/Eddy_SWOT/`，本地路径前缀: `H:\Eddy_SWOT\`。

---

## Stage 1 — Rim-radius offset (null/pivot)

| 图 | 来源脚本 | 数据 | N | 说明 |
|----|---------|------|---|------|
| `figures/stage1/FIG01_case02_Anticyclonic_20250429.png` | `swot_code/st2_match/st_03c_select_cases.m` + plot | matched_eddies.mat 子集 | 1 case | AE 案例，ΔR=+34 km |
| `figures/stage1/FIG01_case05_Cyclonic_20240221.png` | 同上 | 同上 | 1 case | CE 案例，ΔR=−4 km |
| `figures/stage1/FIG01_case16_Cyclonic_20240625.png` | 同上 | 同上 | 1 case | CE 案例，ΔR=−2 km |
| `figures/stage1/exp1a_composite.png` | `st_04_exp1a_*` (early) | exp1a_full.mat | 7057 → 2957 CLEAN | full-sample first-pass composite |
| `figures/stage1/exp1b_excess_N500.png` | `st_04_exp1b_fast.m` | exp1b_pilot.mat | 200 pilot | displaced control pilot |

---

## Exp 1c — Radial Composite (N=2956)

**主脚本**: `swot_code/st3_strain/st_04_exp1c_full.m`
**绘图**: `swot_code/st3_strain/st_04_exp1c_plot.m`
**SBATCH**: `st_04_exp1c_sbatch.sh`、`st_04_exp1c_plot_sbatch.sh`
**数据产物**: `datamat/exp1c_full.mat`（HPC）

**关键参数**（见 `swot_code/lib/analysis_rule.m`）
- `cfg.smooth.lambda_m = 12000`（filt2 12 km lowpass）
- `cfg.radial.r_bins_R = 0:0.2:3.0`（15 bins）
- `cfg.ctrl.N_disp = 10`、`disp_R_min/max = 3/5`、`rand_lat_band = 3°`

| 图 | 内容 | 关键数 |
|----|------|--------|
| `figures/exp1c/exp1c_grad_composite.png` | \|∇SSH\| 径向剖面 P / C_disp / C_rand / E | peak E = +0.40 µm/m at 1.1R |
| `figures/exp1c/exp1c_strain_composite.png` | S_app 径向剖面 P / C_disp / C_rand / E | peak E = +1.15 µs⁻¹ at 1.3R |

---

## Exp 1d v2 — Azimuthal Continuity (control-subtracted)

**主脚本**: `swot_code/st3_strain/st_04_exp1d_azimuthal.m`
**绘图**: `swot_code/st3_strain/st_04_exp1d_plot.m`（2026-06-19 新增）
**SBATCH**: `st_04_exp1d_sbatch.sh`
**数据产物**: `datamat/exp1d_azimuthal_v2.mat`（HPC）

**关键参数**
- 12 个方位扇区
- 0.9–1.5R 环带
- N_disp = 10 displaced controls

**关键数（来自 .mat 检视记录）**
- N_total CLEAN = 2956
- N（mean_E > 0 子集）= 815
- f_pos_E = 0.657
- N_eff_E ≈ 4.4
- Ctheta_vec = 0.207（control: 0.268）

**图**

| 图 | 内容 |
|----|------|
| `figures/exp1d/exp1d_sector_excess.png` | 极坐标扇形条 + 线性条形：12 扇区 mean E_sec ± SEM |
| `figures/exp1d/exp1d_diagnostics.png` | N_eff_E / f_pos_E / Ctheta_vec / ΔCtheta vs control null 直方图 |

---

## Exp 1e v2 — Q_OW Pixel-level

**主脚本**: `swot_code/st3_strain/st_04_exp1e_ow.m`
**绘图**: `swot_code/st3_strain/st_04_exp1e_plot.m`（2026-06-19 新增）
**SBATCH**: `st_04_exp1e_sbatch.sh`
**数据产物**: `datamat/exp1e_ow_v2.mat`（HPC）

**关键数**
- N = 2647 CLEAN（has 有效 pixel-level Q_OW）
- 涡核 P_QOW = −0.462（rotation）；E_QOW = −0.163
- 外围 P_QOW = +0.026（strain）；E_QOW = +0.012
- S/\|ζ\| ratio @ 12 km: 1.05–1.12

**图**

| 图 | 内容 |
|----|------|
| `figures/exp1e/exp1e_qow_radial.png` | 六联径向图：S_app, \|ζ\|, **Q_OW**, OW(signed), \|OW\|, S/\|ζ\|；每图含 P / C_disp / E = P-C |

---

## Exp 2 — Filter-Scale Sensitivity

**主脚本**: `swot_code/st3_strain/st_04_exp2_sensitivity.m`
**绘图**: `swot_code/st3_strain/st_04_exp2_plot.m`（2026-06-19 新增）
**SBATCH**: `st_04_exp2_sbatch.sh`
**数据产物**: `datamat/exp2_filt2_sensitivity.mat`（HPC）

**关键参数**
- `cfg.smooth.lambda_list_m = [6000, 12000, 18000]`
- N = 2956 / scale，displaced control only

**关键数**

| Cutoff | \|∇SSH\| peak E | S_app peak E | Peak 位置稳定 |
|--------|-----------------|--------------|--------------|
| 6 km | +0.39 µm/m | +0.75 µs⁻¹ | ✅ 1.1R / 1.3R |
| 12 km | +0.40 µm/m | +1.09 µs⁻¹ | ✅ 1.1R / 1.3R |
| 18 km | +0.41 µm/m | +1.20 µs⁻¹ | ✅ 1.1R / 1.3R |

**图**

| 图 | 内容 |
|----|------|
| `figures/exp2/exp2_filter_sensitivity.png` | 双面板：\|∇SSH\| 与 S_app 的 E(r/R) 在 6/12/18 km 三尺度叠加；含 SEM 阴影 + peak marker |

---

## Exp 1f — SwotDiag Cross-Validation

**主脚本**: `swot_code/st3_strain/st_04_exp1f_swotdiag_verify.py`
**SBATCH**: `st_04_exp1f_sbatch.sh`
**数据产物**: 单 pass 验证结果（暂未保存 .mat）

**关键数**
- SwotDiag 9-pt fit vs MATLAB `gradient()` r = 0.85（exploratory，1 pass）
- Multi-pass validation: pending mask tuning

---

## Exp 4 — SST Tracer Response

**主脚本**: `swot_code/st4_sst/st_05_exp4_sst_full.m`
**辅助脚本**:
- `st_05_exp4_sst_audit.m`（selection audit + polarity radial）
- `st_05_exp4_sst_regression.m`（F_edge 独立性回归）
- `st_05_exp4_sst_map2d.m`（2D 合成图）
- `st_05_exp4_sst_plot.m`（基础出图）

**SBATCH**: `st05_exp4_sst_sbatch.sh`、`st05_exp4_map2d_sbatch.sh`

**数据产物**
- `datamat/exp4_sst_full.mat`
- `datamat/exp4_sst_2dmap.mat`
- `datamat/exp4_sst_regression.mat`
- `datamat/exp4_sst_audit.mat`

**关键参数**
- 数据：MUR-JPL-L4-GLOB-v4.1（0.01° daily）
- 时间：2023-07 ~ 2025-10（854 天）
- 区域：Kuroshio [130–170E, 28–42N]
- 双 control：displaced 3–5R + same-swath random
- F_edge 定义：`mean(E_S_disp(:, r ∈ [1.0, 1.5]R))`
- core annulus：0.3–0.9R；edge annulus：0.9–1.5R

**样本**
- N_total CLEAN = 2956
- N_valid (has_ctrl) = 1238
- AE = 700, CE = 538

| 图 | 内容 | 关键数 |
|----|------|--------|
| `figures/exp4/exp4_sst_dual_control.png` | 全样本径向 P / C_disp / C_rand / E | warm-core, not rim-peaked |
| `figures/exp4/exp4_sst_composite.png` | 全样本径向 composite | — |
| `figures/exp4/exp4_sst_polarity.png` | AE vs CE 径向对比 | 两类皆正 SST excess，形态不同 |
| `figures/exp4/exp4_sst_AE_fedge.png` | AE 按 F_edge 高/低分层 | High − Low ≈ +1.36 K |
| `figures/exp4/exp4_sst_CE_fedge.png` | CE 按 F_edge 高/低分层 | CE 增量更大 |
| `figures/exp4/exp4_sst_fedge.png` | 全样本 F_edge 高/低径向 | High core excess +1.70 K, Low +0.34 K |
| `figures/exp4/exp4_sst_fedge_composite.png` | 同上，含 control | — |
| `figures/exp4/exp4_sst_fedge_diff.png` | High − Low 差图 | — |
| `figures/exp4/exp4_sst_2dmap.png` | 涡旋坐标 2D 合成 SST anomaly | — |
| `figures/exp4/exp4_sst_map2d_all.png` | 全样本 2D map | — |
| `figures/exp4/exp4_sst_map2d_high.png` | High F_edge 子集 2D | — |
| `figures/exp4/exp4_sst_map2d_low.png` | Low F_edge 子集 2D | — |
| `figures/exp4/exp4_sst_map2d_diff.png` | High − Low 差图 | — |
| `figures/exp4/exp4_sst_pc.png` | F_edge 与 SST 的 partial correlation | — |
| `figures/exp4/exp4_audit.png` | included vs excluded 协变量分布 | included 偏大偏强 AE |

**Exp 4 回归结果**
```
M0: A_SST_core ~ amplitude + radius + polarity + lat + lon + month
   R² = 0.5926, RMSE = 1.79 K, N = 1238
M1: + F_edge
   R² = 0.6041, ΔR² = 0.0115, t_F_edge = 5.97, p ≈ 0
   1σ F_edge → +0.29 K
```
**口径**：仅作 supplementary。R² 增量微小，且 F_edge 与 SST 共为强涡旋"果"。

---

## 缺图待补清单

~~Exp 1d / 1e / 2 缺图~~ → **2026-06-19 已全部补齐**：
- `st_04_exp1d_plot.m` → `figures/exp1d/exp1d_sector_excess.png` + `exp1d_diagnostics.png`
- `st_04_exp1e_plot.m` → `figures/exp1e/exp1e_qow_radial.png`
- `st_04_exp2_plot.m`  → `figures/exp2/exp2_filter_sensitivity.png`

驱动脚本：`st_04_run_all_plots.m`（HPC sbatch 一次跑完）。

---

## 后续实验占位（按 PR §7 路线）

| 编号 | 状态 | 占位 |
|------|------|------|
| Exp 1g | 🔲 设计中 | Background-strain matched control |
| Exp 1h | 🔲 设计中 | Isolated-eddy subset |
| Exp 1i | 🔲 设计中 | Cluster bootstrap |
| Exp 4b | 🔲 设计中 | SST 重做 (Ni 2021 高通) |
| Exp 5a | 🔲 设计中 | Chl-a radial composite (GlobColour L4 NRT) |
| Exp 5b | 🔲 设计中 | Chl-a × F_edge × AE/CE 分层 |
| Exp 5c | 🔲 设计中 | Chl-a lag (+1d, +3d, +7d, t0−3d placebo) |
| Exp 6a | 🔲 设计中 | Front-strain alignment |
| Exp 6b | 🔲 设计中 | Light-side / dense-side Chl 不对称 |
| Exp 6c | 🔲 设计中 | Eddy intensification tendency control |
| Exp 7 | 🔲 设计中 | Gulf Stream / Agulhas Return Current 重复 |

---

*v0.1 | 2026-06-19*
