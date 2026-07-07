---
title: P03 Midterm Review PR — Eddy-Periphery Strain & Tracer Response
author: Zhisheng Zhang
date: 2026-06-19
status: midterm-review-draft
type: PR
purpose: 中期方向审查，请合作者就"目前结果 + 下一步方向 + 创新点定位"两个核心问题给出意见
---

# P03 Midterm Review PR

> **本文不是论文初稿，而是中期方向审查包。**
> 目的：在投入下一阶段（Chl-a + 机制模块）之前，请合作者就科学路线达成共识。

---

## 0. Asks（请优先回答）

| # | 决策点 | 我的倾向 | 请回答 |
|---|--------|---------|--------|
| **A1** | AE/CE 是否在所有 tracer 分析中分开报告？ | 是。SST 已显示 AE/CE 形态不同；Chl-a 对极性更敏感（Klein & Lapeyre 2009; Gaube 2014）。 | ☐ 同意 ☐ 不同意 ☐ 有补充 |
| **A2** | 当前结果 + 下一步方向 + 创新点定位是否成立？ | 见 §5、§6、§7。主线 = Level 1 形态 + Level 3 机制；R² 增量降级为辅助。 | ☐ 同意 ☐ 不同意 ☐ 有补充 |

如果 A1+A2 都同意，我立刻进入 §7 列出的下一步实验。
如果有保留意见，请在对应小节末尾留 comment 行（`> reviewer: ...`）。

---

## 1. Executive Summary

- **Stage 1**（rim-radius offset）= null/weak → pivot 已完成
- **Stage 2 物理层**：Exp 1c / 1d v2 / 1e v2 / 2 已跑完 N=2956 CLEAN 样本，**peripheral fine-scale strain enhancement 在 displaced + same-swath random 双 control 下确证**
- **Stage 2 示踪物（SST）**：Exp 4 全样本 N=1238 已跑完。**形态 = warm core**（不是 rim-peaked）。F_edge 1σ → +0.29 K core SST，ΔR²=0.012。**这一统计关联仅作辅助记录，不再作为主创新点。**
- **Chl-a / 机制 / 跨区域**：尚未开始，下一阶段重点
- **本 PR 求审**：见 §0 Asks

---

## 2. The Pivot — 心路历程

```
D0 (2026-06-07): "SWOT-resolved rim 是否系统性偏离 DUACS rim?"
  ↓
Stage 1 (16 cases, 5 clean): ΔR = +32, −4, +34, −4, −2 km
  → 符号混合 → 排除"系统性半径修正"低层解释
  ↓
文献深化 (Zhang 2019 NC, Dong 2025 NC, Archer 2025 Nature):
  Strain 是细尺度过程的组织变量；涡旋外围有锋生/warm-ring 机制
  ↓
Pivot to Stage 2: "已编目涡旋外围是否存在 SWOT 才能解析的应变增强？"
```

**关键认识**：被隐藏的不是边界的位置，而是边界区域内部的动力学结构。

> **Pivot 证据图**：见 `figures/stage1/FIG01_case02_Anticyclonic_20250429.png`、`case05_Cyclonic`、`case16_Cyclonic`。

---

## 3. Stage 2 已完成实验

### 3.1 Exp 1c — Radial Composite

**问题**：以涡旋为中心，外围 (0.9–1.5R) 是否存在 control-subtracted 应变增强？

**方法**
- 样本：N = 2956 CLEAN SWOT–eddy matches（Kuroshio 2023-07 ~ 2025-10）
- 变量：`|∇SSH|`（一阶梯度，地转流速代理）+ `S_app`（表观地转应变率，Zhang 2019 定义）
- Control：displaced 3–5R + same-swath random（双独立 control）
- 处理：CDT `filt2` 12 km lowpass + MATLAB `gradient()`

**关键结果**

| 变量 | 涡核 (0.1–0.5R) | 外围 peak | Control 一致性 |
|------|----------------|-----------|---------------|
| \|∇SSH\| | −0.91 ~ −0.02 µm/m | +0.40 µm/m at **1.1R** | displaced & random 同号 |
| S_app | −4.23 ~ −0.21 µs⁻¹ | +1.15 µs⁻¹ at **1.3R** | displaced & random 同号 |

> **图**：`figures/exp1c/exp1c_grad_composite.png`、`exp1c_strain_composite.png`

**新发现（不在 Zhang 2019 中）**：涡核 strain 显著低于背景（rotation-dominated），与外围二分。

---

### 3.2 Exp 1d v2 — Azimuthal Continuity

**问题**：外围应变是否环状连续（halo）还是局部斑块？

**方法**
- 12 个方位扇区，0.9–1.5R 环带
- Control-subtracted sector excess `E_sec = P_sec − ⟨C_sec⟩`
- 指标：`f_pos_E`（正异常扇区比例）、`N_eff_E`（有效扇区数）、`Ctheta_vec`（径向 vs 锋面取向）

**关键结果**
- N = 815（mean_E > 0 子集）
- `f_pos_E = 0.657`（约 8/12 扇区为正）
- `N_eff_E ≈ 4.4` → **不是 12 个扇区均匀分布，而是约 4 个有效扇区**
- `Ctheta_vec = 0.207`（**低于** background 0.268）→ 偏锋面取向，非环状

**结论**：peripheral strain enhancement **是 asymmetric/patchy，不是 halo**。术语应用 "fine-scale strain enhancement"，**慎用 "halo"**。

> **图**：`figures/exp1d/exp1d_sector_excess.png`（12 扇区极坐标 + 线性条形）、`exp1d_diagnostics.png`（N_eff_E / f_pos_E / Ctheta vs control null）。.mat：`/slurm/zhangzs/Eddy_SWOT/datamat/exp1d_azimuthal_v2.mat`。

---

### 3.3 Exp 1e v2 — Q_OW Pixel-level

**问题**：涡核-外围 rotation/strain 二分能否在 Okubo-Weiss 框架下独立验证？

**方法**：pixel-level Q_OW = S² − ω²，再做 displaced control 减法

**关键结果**

| 区域 | P_QOW | E_QOW |
|------|-------|-------|
| 涡核 | **−0.462**（rotation-dominated） | −0.163（比背景更 rotation） |
| 外围 | **+0.026**（slightly strain-dominated） | +0.012（比背景更 strain） |

`S/|ζ|` ratio 在 12 km filter 下平稳（~1.05–1.12）→ **Q_OW 是判别核-外围的有效量**。

> **图**：`figures/exp1e/exp1e_qow_radial.png`（六联图：S_app, |ζ|, Q_OW, OW, |OW|, S/|ζ|，含 P/C/E）。.mat：`/slurm/zhangzs/Eddy_SWOT/datamat/exp1e_ow_v2.mat`。

---

### 3.4 Exp 2 — Filter-Scale Sensitivity

**问题**：peripheral strain peak 是否依赖滤波尺度？

**方法**：filt2 cutoff = 6, 12, 18 km；displaced control；N = 2956 / scale

**关键结果**

| Cutoff | \|∇SSH\| peak E | S_app peak E | Peak 位置 |
|--------|----------------|--------------|----------|
| 6 km | +0.39 µm/m | +0.75 µs⁻¹ | 1.1R / 1.3R |
| 12 km | +0.40 µm/m | +1.09 µs⁻¹ | 1.1R / 1.3R |
| 18 km | +0.41 µm/m | +1.20 µs⁻¹ | 1.1R / 1.3R |

**结论**：peak 位置在三个尺度下完全稳定 → 不是滤波伪影。

> **图**：`figures/exp2/exp2_filter_sensitivity.png`（双面板：\|∇SSH\| 与 S_app 的 6/12/18 km 叠加 E(r/R)，含 SEM 阴影 + peak marker）。.mat：`/slurm/zhangzs/Eddy_SWOT/datamat/exp2_filt2_sensitivity.mat`。

---

### 3.5 Exp 1f — SwotDiag Cross-Validation（探索性）

**方法**：SwotDiag 9-point fit kernel vs MATLAB `gradient()`，单 pass 验证
**结果**：r = 0.85（一致性可接受）；多 pass 验证待 mask 调优后跑 HPC。

---

## 4. Exp 4 SST — Tracer Response

**数据**：MUR-JPL-L4-GLOB-v4.1（0.01°，daily）；2023-07 ~ 2025-10；Kuroshio
**样本**：N = 1238（has_ctrl=true 子集）；AE = 700, CE = 538

### 4.1 形态结果

| 项 | 结果 | 图 |
|---|------|----|
| 全样本径向剖面 | warm-core, 不是 rim-peaked | `figures/exp4/exp4_sst_dual_control.png` |
| AE/CE 形态对比 | 两类都呈正 SST excess，但形态不同 | `exp4_sst_polarity.png`、`exp4_sst_composite.png` |
| 2D map（high/low F_edge） | High F_edge 涡旋核 SST excess 更强 | `exp4_sst_map2d_high.png`、`_low.png`、`_diff.png` |
| AE high/low F_edge 分层 | High vs Low Δ ≈ +1.36 K | `exp4_sst_AE_fedge.png` |
| CE high/low F_edge 分层 | CE 增量更大 | `exp4_sst_CE_fedge.png` |
| Selection audit | included 偏大偏强 AE | `exp4_audit.png` |

### 4.2 F_edge 回归（**辅助记录，不作主创新点**）

```
M0: A_SST_core ~ amplitude + radius + polarity + lat + lon + month
   R² = 0.5926, RMSE = 1.79 K, N=1238
M1: M0 + F_edge
   R² = 0.6041, ΔR² = 0.0115, t_F_edge = 5.97, p ≈ 0
   1σ F_edge → +0.29 K core SST
```

> **明确口径**：ΔR² = 0.012 太小，不应作主创新点。F_edge 与 SST 共为强涡旋指标的"果"，**不能讲因果**。该结果在 PR 中仅作 supplementary。

> **图**：`figures/exp4/exp4_sst_fedge.png`、`exp4_sst_fedge_composite.png`、`exp4_sst_fedge_diff.png`、`exp4_sst_pc.png`、`exp4_sst_2dmap.png`、`exp4_sst_map2d_all.png`

---

## 5. 创新点定位（请审）

### 5.1 三层框架

```
Level 1 — 形态（Where）  ← 主创新
  应变峰、SST 峰、Chl-a 峰在 eddy-centric 坐标的位置和不对称性

Level 2 — 强度关系（How much）  ← 辅助
  F_edge / amplitude 等强度指标的统计关联
  Exp 4 SST regression 属此层；ΔR² = 0.012 不是亮点

Level 3 — 机制（Why）  ← 主创新（待做）
  front-strain alignment, light/dense side, lagged response
```

### 5.2 vs 前人的增量

| 前人 | 做了什么 | P03 增量 |
|------|---------|---------|
| Zhang 2019 NC | 全场 strain → ageostrophic / Chl，不分涡内外 | **eddy-centric annulus + control-subtracted**；新发现涡核 strain 低于背景 |
| Dong 2025 NC | 单 basin（Lofoten）+ 模型，warm ring 机制 | **跨海盆 SWOT 实测统计检验**；不预设 warm ring |
| Archer 2025 Nature | SWOT 全球 fine-scale activity | **eddy-centric peripheral**，与 catalog 接通 |
| Xu 2019 Sci Rep | Chl rings 出现频率 ~1% | **加入 strain predictor**：可能解释为何只有少数涡旋激活 |
| Ni 2021 JPO | 全球 CAE/WCE 极性反转统计；6° 高通方法 | **从极性 → 应变组织**；借用其 SST/Chl 高通方案 |
| Liu 2026 GRL | SWOT Lagrangian network | 刻意避开 network；聚焦 strain organization |

### 5.3 一句话定位

> **SWOT 让我们第一次在已编目中尺度涡旋坐标中，统计刻画出 control-subtracted 的外围细尺度应变增强；这个增强不构成环状 halo（Exp 1d 已确证），但它对应一个独立于 core pumping 的 peripheral strain mode，其 SST/Chl-a tracer signature 与 Zhang 2019 描述的 strain → frontogenesis → ageostrophic motion → tracer response 物理链一致。**

---

## 6. 背景场剔除策略（请审）

| 数据 | 拟用方法 | 来源 | 备注 |
|------|---------|------|------|
| **SWOT 应变** | control-subtracted（displaced 3–5R + same-swath random） | 本工作 | 已实施 |
| **SST** | 6° 空间高通 + 多年气候态减去 | Ni 2021（Chelton 2011b 系列） | 待重做 Exp 4b |
| **Chl-a** | log10 + 减气候态 + 6° 高通 | Ni 2021 | 待新建 Exp 5 |
| **备选: 1–3R 环带平均** | 局地环带平均作为背景 | Li 2025 Sci Adv | 作 sensitivity 对比 |

**SWOT 不能做 6° 高通的原因**：单 swath ≈ 120 km 宽，6°（~670 km）核放不进；且 SWOT 的目标本就是细尺度。两套方法各管尺度，不冲突。

**计划增加的 control（物理层加固）**

| Control | 排除的混淆 | 状态 |
|---------|-----------|------|
| Background-strain matched | "涡旋偏好高应变区" | 🔲 待实施（Exp 1g） |
| Isolated-eddy subset (邻近 < 3R 排除) | Eddy-eddy interaction | 🔲 待实施（Exp 1h） |
| Cluster bootstrap | 非独立样本（pass-level / date-block） | 🔲 待实施（Exp 1i） |

---

## 7. 下一步实验路线

按现有试验编号延续：

### 7.1 物理层加固（先做）

| 编号 | 实验 | 目的 |
|------|------|------|
| **Exp 1g** | Background-strain matched control | 排除 "涡旋偏好高应变区" 这一最大混淆 |
| **Exp 1h** | Isolated-eddy subset | 排除 eddy-eddy 相互作用 |
| **Exp 1i** | Cluster bootstrap (pass / date-block) | 修正样本独立性 |
| **Exp 1f-mp** | SwotDiag multi-pass validation | 跨求导核一致性 |

### 7.2 Tracer 重做与扩展

| 编号 | 实验 | 目的 |
|------|------|------|
| **Exp 4b** | SST 重做 with Ni 2021 高通 + 减气候 | 统一背景剔除口径 |
| **Exp 5a** | Chl-a 下载 + radial composite (Copernicus GlobColour L4 NRT daily) | tracer 第二条独立证据 |
| **Exp 5b** | Chl-a × F_edge 分层 + AE/CE 分层 | tracer 形态学 |
| **Exp 5c** | Chl-a lag t0, +1d, +3d, +7d, t0−3d placebo | 区分背景 vs 涡致 |

### 7.3 机制模块（Level 3）

| 编号 | 实验 | 目的 |
|------|------|------|
| **Exp 6a** | Front-strain alignment（Zhang-style） | 检验 strain 是否沿锋面取向 |
| **Exp 6b** | Light-side / dense-side Chl 不对称 | Zhang 2019 预测的关键签名 |
| **Exp 6c** | Eddy intensification tendency control | 区分 core pumping vs peripheral strain |

### 7.4 跨区域（NC 必做）

| 编号 | 实验 | 目的 |
|------|------|------|
| **Exp 7** | Gulf Stream / Agulhas Return Current 重复 | 跨海盆一致性 → NC level |

---

## 8. 关键缺口与风险

### 8.1 已知缺口

1. ~~**Exp 1d / 1e / 2 三个实验缺成图**~~ → ✅ 已补（2026-06-19，新增 `st_04_exp1d_plot.m` / `_exp1e_plot.m` / `_exp2_plot.m`）
2. **Background-strain matched control 未做**：这是 ChatGPT 强调的最大混淆排除项
3. **Cluster bootstrap 未做**：当前 p 值假设样本独立，可能高估显著性
4. **Chl-a 数据未下载**

### 8.2 风险

- **最大风险**：Exp 1g 后 excess 显著性下降，意味着 peripheral strain 主要由 background fronts 解释
- **SWOT snapshot 限制**：21 天重访 → 所有结论限定为 statistical snapshot claim，不做 lifecycle/genesis 声明
- **F_edge 形态**：可能是连续谱（与 Xu 2019 的 1% 不一致），需 Exp 5b 后判定
- **AE/CE 极性混淆**：Chen & Chen 2025 已警示 DUACS 极性可疑率，需 Ni 2021 风格 CAE/WCE 二次分类

---

## 9. 文件索引

| 类型 | 路径 |
|------|------|
| 科学方向冻结版 | `DIRECTION.md` |
| 论文叙事骨架 | `NARRATIVE.md` |
| 项目说明（progress log） | `README.md` |
| 本 PR | `manuscript/v2_delivery/PR_2026-06-19_midterm_review.md` |
| 图（按试验编号） | `figures/{stage1,exp1c,exp1d,exp1e,exp2,exp4}/` |
| 结果清单 | `doc/results_registry_20260619.md` |
| 代码（HPC 镜像） | `H:\Eddy_SWOT\swot_code\` ↔ `/slurm/zhangzs/Eddy_SWOT/swot_code/` |

---

## 10. 审稿留言区（合作者请在此填写）

```
> reviewer-1 (name, date):
>   A1:
>   A2:
>   其他:

> reviewer-2 (name, date):
>   A1:
>   A2:
>   其他:
```

---

*Draft v0.1 | 2026-06-19 | 本 PR 用于中期方向审查，不投稿*
