# P03: Eddy-Periphery Fine-Scale Strain Enhancement Revealed by SWOT

> 原题: Testing Neglected Eddy Boundary Signals with SWOT Altimetry（2026-06-07 D0 proposal）
> 当前方向: 从 "rim-radius offset" 深化为 "eddy-periphery fine-scale strain enhancement"（2026-06-14 更新）

## Status

| Item | Content |
|---|---|
| Current stage | 物理层 + SST 完成；NC 门控策略已定（DIRECTION.md §12）；等待 Gate 0 (Exp 1g) |
| Next action | **Exp 1g background-strain matched control** — Gate 0，决定文章生死 |
| Lead / proposer | Zhisheng Zhang |
| Target journal | Nature Communications / Science Advances（取决于 Stage 2 跨区域 tracer 证据强度） |
| Start date | 2026-06-07 |
| Stage 1 radius-offset test | Completed (2026-06-13): null/weak, used as pivot motivation |
| Exp 1c completed | 2026-06-16 (v2 2026-06-17): N=2956 CLEAN, displaced + same-swath random controls, \|∇SSH\| + S_app, control coords saved |
| Exp 2 completed | 2026-06-16: 6/12/18 km filter sensitivity under displaced control, peak radius stable |
| Exp 1d revised | 2026-06-17 (v2): control-subtracted sector excess; N=815 (mean_E>0), N_eff~4.4 effective sectors, Ctheta lower than background → asymmetric, not annular |
| Exp 1e revised | 2026-06-17 (v2): pixel-level Q_OW successful (core −0.462 rotation → periphery +0.026 strain); S/\|ζ\| flat at 12km |
| Exp 1f | 1-pass SwotDiag vs gradient r=0.85 (exploratory); multi-pass validation pending mask tuning |

## Project Evolution（项目演化）

```
D0（2026-06-07）: "SWOT-resolved rim 是否比 AVISO eddy-core 更好地组织 tracer anomalies?"
  H2: rim-radius offset (R_SWOT − R_DUACS)

↓ Stage 1 实验（2026-06-10 ~ 2026-06-13）

Stage 1 结果: 16 Kuroshio prototype cases, v2 修正.
  5 个 clean cases 的 ΔR 符号混合（+32, −4, +34, −4, −2 km）.
  样本量不足以精确估计总体中位数，但足以排除原半径偏移假说.
  → 排除了低层解释: SWOT 不简单改写边界半径.

↓ 文献深化（2026-06-14）

阅读 Zhang 2019 NC + Dong 2025 NC + Archer 2025 Nature.
  → 方向从 "radius offset" 升级为 "peripheral strain enhancement."

当前: "已编目中尺度涡旋外围是否存在 SWOT 才能解析的细尺度应变增强?"
  详见 DIRECTION.md（冻结版科学方向）
```

## Current Scientific Question

> **Do catalogued mesoscale eddies show statistically significant excess fine-scale strain around their peripheries, as observed by SWOT, relative to matched controls? Does this peripheral strain enhancement predict independent SST and Chl-a responses?**

### 为什么不是"重写"而是"深化"

1. **继承了同一 eddy registry**: DUACS/PET 检测的 7057 对 SWOT-eddy matches
2. **继承了同一诊断目标**: SwotDiag-style derivative diagnostics as reference; production implementation uses CDT filt2 + MATLAB gradient(); SwotDiag consistency verified (r=0.85, 1 pass exploratory)
3. **继承了同一核心策略**: AVISO detect → SWOT measure
4. **Stage 1 的 null/weak 不是失败**: 它排除了低层解释，指向了更深的问题

### 核心创新（vs. 前人）

| 前人工作 | 做了什么 | 我们增量在哪 |
|---------|---------|-----------|
| Archer 2025 Nature | SWOT 全球 fine-scale SSH activity | 首次围绕 catalogued eddies 做 control-subtracted peripheral strain composite |
| Dong 2025 NC | Lofoten Basin 单区域 strain → warm ring（Seaglider + model） | 用 SWOT 实测做跨海盆统计检验；不把 warm ring 当主假说 |
| Zhang 2019 NC | AVISO DUACS strain → ageostrophic motion / Chl | 用 SWOT 替换 AVISO；从全场 strain → eddy-centric periphery |
| Liu 2026 GRL | SWOT Lagrangian flow network（South China Sea） | 刻意避开 network 方向；聚焦 eddy-centric strain organization |

### Exp 1c — Full physical-layer robustness (2026-06-16)

N = 2956 CLEAN SWOT–eddy matches.

**Variables:**
- |∇SSH| — first-derivative SSH gradient, geostrophic-speed proxy
- S_app — apparent geostrophic strain-rate proxy (Zhang 2019 definition)

**Controls:**
- Local displaced control (3–5R, same SWOT pass)
- Same-swath random control

**Key results:**
- |∇SSH|: core suppression at 0.1–0.5R (−0.91 to −0.02 µm/m); peripheral excess at 0.9–1.5R; peak +0.40 µm/m at 1.1R
- S_app: strong core suppression (−4.23 to −0.21 µs⁻¹); peripheral excess at 1.1–1.5R; peak +1.15 µs⁻¹ at 1.3R
- Random control gives same-sign but slightly weaker excess, supporting robustness against swath geometry

**Exp 2 — Filter-scale sensitivity (2026-06-16)**
- 6/12/18 km cutoff wavelength; N=2956 per scale
- |∇SSH| peak E: +0.39 / +0.40 / +0.41 µm/m (all at 1.1R)
- S_app peak E: +0.75 / +1.09 / +1.20 µs⁻¹ (all at 1.3R)
- Peak radius stable across all scales

**Production pipeline:**
SWOT L3 Expert v3.0 → CDT `filt2` 2-D lowpass → `gradient()` → radial composite → displaced + random controls.
Validation: 1-pass SwotDiag 9-point kernel vs gradient r=0.85 (exploratory); multi-pass validation pending.

**与 Zhang 2019 NC 对比:**

| | Zhang 2019 | P03 本阶段 |
|---|---|---|
| 分析单位 | Strain saddle point | Eddy center + annulus |
| 数据 | AVISO DUACS (0.25°) | SWOT KaRIn (2 km) |
| 组织方式 | 全场 S_g quantile | Eddy-centric, control-subtracted |
| 有无 control | 无（strain 是 predictor） | 有（eddy 是 predictor，需 control） |
| 涡核发现 | 无（不区分核/外围） | 涡核 strain 低于背景 37% — 新发现 |
| 互补性 | 建立 strain→tracer 框架 | 首次用 SWOT 证实 strain 围着涡旋组织 |

### 两层框架

```
第一层（predictor, 纯 SWOT SSH, lock-box）:
  检验 eddy periphery 是否存在 excess fine-scale strain.
  四类 matched controls: same-swath random / local displaced / background-strain matched / isolated-eddy.

第二层（response, 打开 lock-box）:
  检验 peripheral strain enhancement 是否预测 SST/Chl-a response.
  措辞: "predicts / covaries with", 不声称 causation.
```

### 术语规范

| 推荐（主文） | 内部简称 | 何时升级 |
|------------|---------|---------|
| eddy-periphery fine-scale strain enhancement | strain halo | 仅当数据证实 annular continuity + radial localization + azimuthal coverage |
| peripheral strain activity | — | — |
| F_edge（peripheral strain-enhanced fraction） | — | — |
| catalogued / parent mesoscale eddies | — | — |

### 关键口径（已定，详见 DIRECTION.md）

1. 不声称"边界比涡核重要"——说 core mode + peripheral strain mode 并存
2. 不声称 genesis——第一阶段只主张 matched controls 后的 eddy-associated excess strain
3. 不把 warm ring 当主假说——Dong 2025 是机制支撑
4. predictor-response 分离——不用 tracer 定义物理状态
5. PET 作 registry，不作 boundary-definer

---

## 当前实验路线（5 Experiments，详见 DIRECTION.md）

| Exp | 问题 | 状态 |
|-----|------|------|
| 1 | 是否存在 excess peripheral strain? | ✅ Exp 1c: N=2956, dual variables, dual controls |
| 2 | 空间范围和滤波尺度敏感性? | ✅ 6/12/18 km under displaced control; peak location stable |
| 3 | 伪影排除（完整 controls）? | 🔶 displaced + same-swath random done; Exp 1d azimuthal (control-subtracted) done → asymmetric not annular; Exp 1e vorticity/OW done → Q_OW confirms rotation-core/strain-periphery; background-strain matched / isolated-eddy subset pending |
| 4 | 是否预测 SST/Chl-a response? | 🔶 Exp 4 SST 完成；Chl-a 待下载 |
| 5 | F_edge 分布形态（连续 vs 分群）? | 🔲 依赖 Exp 4 |

---

## Progress Log

| Date | Stage | Content | Output |
|---|---|---|---|
| 2026-06-07 | D0 | Initial idea: SWOT-resolved eddy rims vs. AVISO/py-eddy-tracker eddy-core framework | D0 README |
| 2026-06-08 | D0 | R0 review: reviewer report + editorial decision | `review/reviewer/R0-reviewer-report.md`, `review/editor/R0-editorial-decision.md` |
| 2026-06-10 | D1 | st_01 PET eddy detection (816 days, 1632 NC) | Job 19588 |
| 2026-06-10 | D1 | st_02 extract Kuroshio eddy centers (36543) | Job 19590 |
| 2026-06-11 | D1 | st_03a SWOT coverage scan (2891 passes) | Job 19609 |
| 2026-06-11 | D1 | st_03b SWOT-eddy matching (7057 pairs) | Job 19610 |
| 2026-06-12 | D1 | st_03c case selection (16 prototypes) | — |
| 2026-06-12 | D1 | FIG_01 radial profile comparison (v1 → v2 correction) | 16 figures (Job 19656) |
| 2026-06-13 | D2 | Stage 1 conclusion: rim-radius offset null/weak; pivot direction discussion | Closeout |
| 2026-06-14 | D2 | Direction updated: peripheral fine-scale strain enhancement; literature supplemented | DIRECTION.md, literature_survey.md |
| 2026-06-14 | D2 | R1 review response in preparation | (draft) |
| 2026-06-15 | D2 | st_04 Exp 1a full: 7057 eddies, 4.2h, CLEAN N=2957, peak |∇SSH| 3.39 µm/m at 1-1.5R | `data/exp1a_full.mat` |
| 2026-06-16 | D2 | st_04 Exp 1b (200 pilot): E(1.1R)=+0.32 µm/m, core E=−0.77 — displaced control 证实 excess | `data/exp1b_pilot.mat` |
| 2026-06-16 | D2 | st_04 Exp 1c full: N=2956 CLEAN, dual variables (\|∇SSH\| + S_app), dual controls (displaced + random), 8min | `data/exp1c_full.mat` |
| 2026-06-16 | D2 | st_04 Exp 2 filter sensitivity: 6/12/18 km, N=2956/scale, peak location stable | `data/exp2_filt2_sensitivity.mat` |
| 2026-06-16 | D2 | Physical-layer conclusion: H1 supported in Kuroshio CLEAN sample; pipeline upgraded to filt2+gradient | 本 PR |
| 2026-06-17 | D2 | Exp 4 SST 全部完成: N=1238 双 control, F_edge Δ=+1.4K, 回归 ΔR²=1.15% (t=5.97), AE/CE 分层, 2D maps | `data/exp4_sst_*.mat` |
| 2026-06-19 | D2 | **Midterm review PR #9** to upstream: 3 commits + figures archive + results registry | `PR_2026-06-19_midterm_review.md` |
| 2026-06-19 | D2 | 补图：Exp 1d/1e/2 三个 `_plot.m` HPC 渲染 + 图归档到 figures/ 子目录 | `st_04_exp1d/e/2_plot.m` |
| 2026-06-19 | D2 | GPT 讨论确定三层框架（L1/L3 主线，L2 降级）+ Ni 2021 高通策略 | conversational |
| 2026-06-20 | D2 | **PR #9 审查通过 + merge**；PR #8 确认已含于 #9 | upstream merge |
| 2026-06-20 | D2 | **NC 门控策略制定**：Gate 0 (Exp 1g)、Chl-a 升为主线、跨区域必做、机制聚焦 | DIRECTION.md §12, NARRATIVE.md v0.2 |

---

## 当前待办（2026-06-20 更新，按 NC 门控策略重排）

> 详见 DIRECTION.md §12。Chl-a 升为主证据线，SST 降为 supporting。

**Phase 0: 物理层封口 — Gate 0 决定文章生死**
- [ ] **Exp 1g: Background-strain matched control** ← 最高优先级
- [ ] Exp 1i: Cluster bootstrap (pass-level / date-block)
- [ ] Exp 1h: Isolated-eddy subset (邻近 < 3R 排除)

**Phase 1: Chl-a 主证据线 — NC 的核心 "so what"**
- [ ] Exp 5a: Chl-a radial composite (Copernicus GlobColour L4 NRT daily)
- [ ] Exp 5b: Chl-a × F_edge 分层 + AE/CE 分层
- [ ] Exp 5c: Chl-a lag (t0, +1d, +3d, +7d, t0−3d placebo)
- [ ] Exp 5d: F_edge 连续谱 vs Xu 2019 的 1% 阈值 ← 新增

**Phase 2: 跨区域复制 — NC vs GRL 分水岭（必做）**
- [ ] Exp 7a: Gulf Stream (Exp 1c + 5a 等价)
- [ ] Exp 7b: Agulhas Return Current (Exp 1c + 5a 等价)

**Phase 3: 机制聚焦 — 做精一个**
- [ ] Exp 6a: Front-strain alignment（主机制）
- [ ] Exp 6b: Light-side / dense-side Chl（辅助）
- [ ] ~~Exp 6c~~: 降级为 Supplementary

**支线（不阻塞主线）:**
- [ ] Exp 4b: SST 重做 with Ni 2021 6° 高通 (supporting evidence)
- [ ] Exp 1f-mp: SwotDiag multi-pass (Methods supplement)

**已完成:**
- [x] Exp 1c/1d/1e/2 物理层全套
- [x] Exp 4 SST tracer (N=1238, 双 control, F_edge, AE/CE 分层)
- [x] 中期 PR #9 审查通过 + merge (2026-06-20)

---

## 数据

所有数据均为公开数据。原始数据不上传 repo。

### Stage 1（已完成）

- SWOT KaRIn L3 Expert v3.0 (2 km) — 7057 对 SWOT-eddy matches
- AVISO/DUACS gridded SLA + geostrophic currents (CMEMS DT2024)
- py-eddy-tracker on DUACS（PET registry）

### Stage 2（计划中）

- **SST**: GHRSST MUR (~1 km) 或 Sentinel-3 SLSTR (1 km) — 需评估云覆盖对 warm ring signal 的影响
- **Ocean color / Chl-a**: MODIS/VIIRS — log Chl, ±1–3 day lag
- 代码: SwotDiag (Carli 2025, MIT license)

---

## 参考文献（经核验）

### 核心框架文献（Stage 2 新增）

- **Zhang, Z., Qiu, B., Klein, P., & Travis, S. (2019).** The influence of geostrophic strain on oceanic ageostrophic motion and surface chlorophyll. *Nature Communications*, 10, 2838. doi:10.1038/s41467-019-10883-w
- **Dong, H., Zhou, M., McWilliams, J.C., et al. (2025).** Warm rings in mesoscale eddies in a cold straining ocean. *Nature Communications*, 16, 9252. doi:10.1038/s41467-025-64308-y
- **Archer, M., Wang, J., Klein, P., Dibarboure, G., & Fu, L.-L. (2025).** Wide-swath satellite altimetry unveils global submesoscale ocean dynamics. *Nature*, 640, 691–696. doi:10.1038/s41586-025-08722-8
- **Han, X., Wang, Q., Stewart, A.L., et al. (2026).** High coastal eddy activity around Antarctica revealed by SWOT. *National Science Review*, 13(9), nwag181. doi:10.1093/nsr/nwag181
- **Liu, Y., He, Q., Zhan, W., et al. (2026).** Hidden fine-scale transport pathways and biological connectivity revealed by SWOT. *Geophysical Research Letters*, 53(10). doi:10.1029/2025GL121208
- **Chen, X., & Chen, G. (2025).** On the ambiguity of oceanic eddy polarity. *JGR Oceans*, 130. doi:10.1029/2024JC022239

### SWOT 观测方法

- **De Marez, C., et al. (2026).** SWOT reveals mesoscale eddy hotspots and deserts in subpolar and polar oceans. *Ocean Science*, 22, 1515–2026. doi:10.5194/os-22-1515-2026
- **Carli, T., et al. (2025).** Southern Ocean 3D eddy diagnostics derived from SWOT. *JGR Oceans*. doi:10.1029/2024JC022307
- **Jensen, M., et al. (2025).** SWOT observations unveil small mesoscale variability on the East Greenland shelf. *GRL*. doi:10.1029/2025GL118573
- **Verger-Miralles, E., et al. (2025).** SWOT enhances small-scale eddy detection in the Mediterranean Sea. *GRL*. doi:10.1029/2025GL116480

### 经典涡旋 / 示踪物文献

- Chelton, D. B., et al. (2011a). *Progress in Oceanography*, 91, 167–216. doi:10.1016/j.pocean.2011.01.002
- Chelton, D. B., et al. (2011b). *Science*, 334, 328–332. doi:10.1126/science.1208897
- Gaube, P., et al. (2014). *JGR Oceans*, 119. doi:10.1002/2014JC010111
- Xu, G., et al. (2019). *Scientific Reports*, 9, 2056. doi:10.1038/s41598-018-38457-8
- Pegliasco, C., et al. (2022). *ESSD*, 14, 1087–1107. doi:10.5194/essd-14-1087-2022

### 概念框架综述

- **Zhang, Z., et al. (2024).** Three-dimensional structure of oceanic mesoscale eddies. *Ocean-Land-Atmosphere Research*, 0051. doi:10.34133/olar.0051
- **Dong, H., et al. (2025).** Oceanic mesoscale eddies. *Ocean-Land-Atmosphere Research*, 0081. doi:10.34133/olar.0081

---

## 审稿状态

| 轮次 | 文件 | 日期 | 状态 |
|------|------|------|------|
| R0 Reviewer | `review/reviewer/R0-reviewer-report.md` | 2026-06-08 | 已接收 |
| R0 Editor | `review/editor/R0-editorial-decision.md` | 2026-06-08 | 已接收 |
| R1 Response | `review/R1-response-to-reviewer.md` | 2026-06-15 | ✅ 已起草 |

---

> **冻结版科学方向**: 见 `DIRECTION.md`（v0.2, 2026-06-14）
> **详细文献调研**: 见 `literature/literature_survey.md`
> **代码路线图**: 见 HPC 本地 `H:\Eddy_SWOT\swot_code\README.md`
