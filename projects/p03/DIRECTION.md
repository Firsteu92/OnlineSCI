# P03 研究方向（DIRECTION.md）

> 立项种子（v0.2）。**写完即冻结**——后续所有方向调整通过 README.md 迭代。
> 本文档是 P03 "做什么" 的 single source of truth。

## 1. 主题与工作标题

- **工作标题（EN）**: Eddy-Periphery Fine-Scale Strain Enhancement Revealed by SWOT Altimetry
- **中文一句话**: SWOT 揭示已编目中尺度涡旋外围的细尺度应变增强
- **核心科学问题**: 传统高度计已编目的中尺度涡旋，其外围是否存在 SWOT 才能解析的细尺度应变增强？这种增强是否独立预测 SST 和 Chl-a 示踪物响应？
- **差异化（vs 前人）**:
  - vs Archer 2025（SWOT 全球 fine-scale SSH）：不做全场景 activity map，聚焦 eddy-centric periphery
  - vs Dong 2025（Lofoten warm ring）：不做单 basin + 模型机制，用 SWOT 实测做跨海盆统计检验；不把 warm ring 当主假说
  - vs Zhang 2019（strain → Chl）：继承 strain predictor 框架，但用 SWOT 替换 AVISO，从全场 strain 转为 eddy-centric peripheral strain
  - vs Liu 2026（SWOT Lagrangian network）：不做 network，不做全场 connectivity
  - vs Chen & Chen 2025（DUACS polarity）：互补——我们依赖 DUACS 极性可靠性做 AE/CE 分层

## 2. 硬约束

| 项 | 值 |
|---|---|
| 投稿目标 / venue | Nature Communications 或 Science Advances（取决于 Stage 2 跨区域 tracer 证据强度） |
| 篇幅上限 | NC 无严格限制；计划 ~5000 词 + 5 主图 |
| Deadline | 无硬性截止；Stage 2 原型目标 2–4 周 |
| 算力 | HPC（/slurm/zhangzs/Eddy_SWOT/），MATLAB R2025a + Python |
| 数据 | 全部公开数据（SWOT / DUACS / SST / Ocean Color） |
| 研究区域 | 第一阶段 Kuroshio Extension；跨区域扩展 Gulf Stream / Agulhas Return Current |

## 3. 科学问题演化（P03 连续性）

```
原始 P03 D0（2026-06-05）:
  "SWOT-resolved rim 是否比传统 eddy-core 更好地组织 tracer anomalies?"
  H2: rim-radius offset (R_SWOT − R_DUACS)

Stage 1 结果（2026-06-13）:
  16 Kuroshio prototype cases, v2 修正.
  5 clean cases 的 ΔR 符号混合（+32, −4, +34, −4, −2 km）.
  样本量不足以精确估计总体，但足以排除原半径偏移假说.
  → 排除了低层解释: SWOT 不简单改写边界半径.

文献深化（2026-06-14）:
  阅读 Zhang 2019 NC + Dong 2025 NC + Archer 2025 Nature.
  → 方向从 "radius offset" 升级为 "peripheral strain enhancement."

当前 P03（v0.2）:
  "已编目中尺度涡旋外围是否存在 SWOT 才能解析的细尺度应变增强?"
```

## 4. 核心假说

> **H1（主假说 — physical organization）**: Catalogued mesoscale eddies show statistically significant excess fine-scale strain around their peripheries, relative to matched controls, as observed by SWOT.

> **H2（tracer response — gated on H1）**: The peripheral strain enhancement predicts independent SST and Chl-a responses: eddies with stronger peripheral strain show stronger surface thermal and biological signatures.

## 5. 方法框架

### 5.1 两层框架

```
第一层（predictor，纯 SWOT SSH，lock-box）:
  检验 eddy periphery 是否存在 excess fine-scale strain.
  不碰 SST/Chl-a.

第二层（response，打开 lock-box）:
  检验 peripheral strain enhancement 是否预测 tracer response.
```

### 5.2 主 predictor

| 变量 | 定义 | 物理含义 |
|------|------|---------|
| E_e(ρ) | P_e(ρ) − C_e(ρ) | **核心**: excess strain（超出 matched control 的 peripheral strain） |
| F_edge | annulus 内 S_app > control P90 的面积比例 | 外围应变空间覆盖度 |
| S_app | SWOT SSH-derived apparent geostrophic strain rate proxy | 表观地转应变率（Zhang 2019 定义） |
| A_∇_HP | median(|∇η_SWOT^HP|) in annulus | 稳健性替代指标（避免二阶导数噪声） |

### 5.3 四类 Matched Controls

| Control | 方法 | 排除的混淆 |
|---------|------|-----------|
| A: Same-swath random | 同 swath、同纬度、同覆盖率随机中心 | Swath geometry + 观测噪声 |
| B: Local displaced | eddy center 平移 3–5R | 大尺度流系 + 区域 EKE |
| C: Background-strain matched | 按低通 DUACS strain/EKE 分层匹配 | "涡旋偏好高应变区" |
| D: Isolated-eddy subset | 排除邻近 eddy < 3R | Eddy-eddy interaction / saddle 误判 |

### 5.4 五实验路线

| Exp | 问题 | 输出 |
|-----|------|------|
| 1 | 是否存在 excess peripheral strain? | radial profile E(r/R), composite maps |
| 2 | 空间范围和滤波尺度敏感性? | heatmap(filter × r/R), regional profiles |
| 3 | 伪影排除（四类 controls）? | control summary, retained effect size |
| 4 | 是否预测 SST/Chl-a response? | F_edge vs tracer response |
| 5 | F_edge 分布形态（连续 vs 分群）? | distribution, dip test |

## 6. 关键口径（已定）

1. **不声称"边界比涡核重要"**: 说 core mode（垂向泵浦）和 peripheral strain mode（侧向应变/前生化）并存。
2. **不声称 genesis**: 第一阶段不声称涡旋生成了 strain；只主张 matched controls 后的 eddy-associated peripheral strain excess。
3. **不把 warm ring 当主假说**: Dong 2025 是机制支撑，不是我们直接检验的对象。
4. **术语保守化**: 主文用 "eddy-periphery fine-scale strain enhancement"。"halo" 仅在数据证实 annular continuity + radial localization + azimuthal coverage 后作为 shorthand。
5. **Predictor-response 分离**: 先证明物理 organization，再检验 tracer response。不用 tracer 定义物理状态。
6. **PET 作 registry，不作 boundary-definer**: AVISO detect → SWOT measure。

## 7. 风险

- **最大风险**: excess strain 完全由 background fronts 解释（matched controls 无法区分）
- **Swath edge 污染**: SWOT swath 边缘噪声可能伪装成 fine-scale strain
- **滤波尺度敏感**: 如果 signal 只在单一尺度出现
- **SST 数据分辨率**: Dong 2025 的 warm ring 是 1–10 km / ~0.4°C，需要高分辨率 SST 才能分辨
- **F_edge 可能单峰分布**: 如果是连续谱，不能强行分 "rich vs poor"

## 8. 参考文献（核心 6 篇）

1. **Zhang et al. 2019** — Nature Communications. 地转应变作为 ageostrophic motion 和 Chl 的组织变量。Strain predictor 框架来源。
2. **Dong et al. 2025** — Nature Communications. Lofoten Basin 涡旋边缘应变 → warm ring。机制支撑。
3. **Archer et al. 2025** — Nature. SWOT 全球 1–100 km fine-scale SSH。数据能力基础。
4. **De Marez et al. 2026** — Ocean Science. 首次在 SWOT swath 上跑 py-eddy-tracker。P03 pipeline 直接参考。
5. **Carli et al. 2025** — JGR Oceans. SwotDiag 拟合核方法。梯度计算核心代码。
6. **Han et al. 2026** — NSR. SWOT Antarctic eddy activity。论文结构模板（surface activity → hidden process）。

## 9. 与 Zhang 2019 的定位关系（2026-06-16 新增）

Zhang 2019 证明了 **strain 是海洋细尺度过程的关键组织变量**——全场 S_g 越高，ageostrophic KE 和 Chl 越强。但 Zhang 2019 不问"strain 围着涡旋组织吗？"

P03 的增量：
1. **从全场 → eddy-centric**：Zhang 2019 按 S_g quantile 分 bin，P03 按涡旋中心做 annulus composite
2. **从无 control → control-subtracted**：Zhang 2019 不需要 control（strain 是自变量），P03 引入 displaced control 分离 eddy-associated 信号
3. **涡核-外围二分**：Zhang 2019 不区分，P03 发现涡核 strain 显著低于背景（新发现）
4. **SWOT 分辨率**：2 km vs 0.25°，直接验证低分数据推断的 fine-scale structure
5. **互补而非替代**：Zhang 2019 的 strain→tracer 框架是 P03 Exp 4 的理论基础

---

## 10. Empirical update — 2026-06-17, v0.4 addendum

Physical-layer H1 supported in Kuroshio CLEAN sample (N=2956):

**Claim-grade:**
- **Exp 1c**: |∇SSH| and S_app, displaced + same-swath random controls. Core suppression (S_app −4.2 to −0.2 µs⁻¹), peripheral excess (|∇SSH| +0.40 µm/m at 1.1R; S_app +1.15 µs⁻¹ at 1.3R). Both controls agree.
- **Exp 2**: 6/12/18 km filter sensitivity under displaced control. Peak location stable (1.1R for |∇SSH|, 1.3R for S_app).

**Revised (2026-06-17), not yet claim-grade:**
- **Exp 1d v2**: Control-subtracted sector excess. N=815 with mean_E>0, f_pos_E=0.657, N_eff_E=4.4 effective sectors, Ctheta_vec 0.207 (LOWER than control 0.268). The excess is real but asymmetric — supports "strain enhancement" without "halo."
- **Exp 1e v2**: Pixel-level Q_OW with displaced controls. Core P_QOW=−0.462 (rotation-dominated), E_QOW=−0.163 (more rotation than background); periphery P_QOW=+0.026 (slightly strain-dominated), E_QOW=+0.012 (more strain than background). S/|ζ| ratio flat at 12km (~1.05-1.12) — Q_OW is the effective discriminator.
- **Exp 1f**: 1-pass SwotDiag 9pt-fit vs gradient r=0.85 (exploratory). Multi-pass validation pending mask tuning on HPC.

**Remaining physical-layer checks before manuscript-level H1 claim:**
1. Cluster bootstrap (statistical independence: pass-level, date-block)
2. Background-strain matched control
3. Isolated-eddy subset
4. Exp 1f multi-pass SwotDiag validation

**Terminology**: "eddy-periphery fine-scale geostrophic strain enhancement" confirmed as primary descriptor. "Strain halo" remains provisional — Exp 1d v2 confirms asymmetry (N_eff~4, not 12; Ctheta lower than background).

Core hypotheses unchanged — this addendum records empirical status only.

---

## 11. Exp 4 SST Plan — 2026-06-17

**Data**: GHRSST MUR-JPL-L4-GLOB-v4.1 (0.01°, daily)
- URL: https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1
- Download: podaac-data-submitter (https://github.com/podaac/data-subscriber)
- Strategy: L4 only (no L2), eddy-centric radial extraction
- Time: 2023-07 pilot → expand to full SWOT cycles
- Region: Kuroshio [130-170E, 28-42N]
- Workflow: download locally → transfer to HPC → extract per-eddy → radial composite

**Rationale**: MUR L4 is sufficient for eddy-centric composite — ~3000 eddies averaging suppresses random noise; sub-km L2 unnecessary for radial mean SST anomaly profiles.

---

---

## 12. NC Gating Strategy & Revised Priority — 2026-06-20

> PR #9 审查通过后制定。目标：确保证据链够 NC，而非停留在 GRL/JGR。

### 12.1 Go / No-Go Gate

```
Gate 0: Exp 1g (background-strain matched control)
  ├─ PASS (excess 仍显著) → 进入 Phase 1–4
  └─ FAIL (excess 消失或大幅衰减)
       ├─ 如果 effect size 下降 >50% → 科学问题需重新定义，降级 GRL 或 pivot
       └─ 如果 下降 <50% 且仍显著 → 继续，但论文需在 Discussion 正面讨论 background contribution
```

**Gate 0 是整篇文章的生死线。在 Gate 0 通过之前，不启动任何数据下载或新实验。**

### 12.2 四阶段执行计划

```
Phase 0  ┃ 物理层封口（2 周）
         ┃ Exp 1g → Exp 1i → Exp 1h
         ┃ Gate 0 判定
         ┃
Phase 1  ┃ Chl-a 主证据线（3 周）          ← NC 的核心 "so what"
         ┃ Exp 5a (radial composite)
         ┃ Exp 5b (F_edge 分层 + AE/CE)
         ┃ Exp 5c (lag: t0, +1d, +3d, +7d, t0−3d placebo)
         ┃ Exp 5d (F_edge 连续谱 vs Xu 2019 的 1% 阈值)    ← 新增
         ┃
Phase 2  ┃ 跨区域复制（2 周）              ← NC vs GRL 的分水岭
         ┃ Exp 7a: Gulf Stream [280–320E, 32–45N]
         ┃ Exp 7b: Agulhas Return Current [20–60E, 35–45S]
         ┃ 每个区域重复 Exp 1c + 5a 等价物
         ┃ 最低标准：3 个海域 strain peak 位置和符号一致
         ┃
Phase 3  ┃ 机制聚焦（2 周）               ← 做精一个，不做散三个
         ┃ Exp 6a: front-strain alignment（主机制证据）
         ┃ Exp 6b: light-side / dense-side Chl 不对称（辅助）
         ┃ Exp 6c: 降级为 Supplementary，非必须
         ┃
─ ─ ─ ─ ┃ 以下穿插进行，不阻塞主线 ─ ─ ─ ─
         ┃
支线 A   ┃ SST 重做 (Exp 4b, Ni 2021 高通)
         ┃ 定位：supporting evidence，不进主图
         ┃ SST 的亮点不是 ΔR²，而是 AE/CE 形态差异
         ┃
支线 B   ┃ Exp 1f-mp (SwotDiag multi-pass)
         ┃ 定位：Methods supplement
```

### 12.3 NC 必达证据清单

| # | 证据 | 对应实验 | 缺了会怎样 |
|---|------|---------|-----------|
| 1 | Peripheral strain excess 在 background-matched control 后仍显著 | Exp 1g | 没文章 |
| 2 | Cluster bootstrap 后统计显著性不崩溃 | Exp 1i | Reviewer reject |
| 3 | Chl-a 对 F_edge 有清晰分层响应（形态图 + 分位数） | Exp 5a+5b | 只有物理层 = GRL |
| 4 | Chl-a lag 分析区分涡致 vs 背景共变 | Exp 5c | "也许只是背景 Chl 梯度" |
| 5 | ≥3 个海域 strain peak 位置和符号一致 | Exp 7a+7b | "Kuroshio 特例" → JGR |
| 6 | ≥1 个机制诊断（front-strain alignment） | Exp 6a | 能发但 reviewer 不满意 |

### 12.4 关键科学策略调整

**（1）Chl-a 升为主证据线，SST 降为 supporting。**

理由：
- SST ΔR²=0.012 撑不住 NC 的 tracer claim
- Chl-a 直接连接生物地球化学（frontogenesis → 营养盐供给 → 浮游植物响应），NC 编辑更看重这条链
- Chl-a 对极性更敏感（Gaube 2014），AE/CE 分层更可能出清晰信号
- Zhang 2019 的核心结果就是 strain → Chl，我们接的是同一条线

**（2）新增 Exp 5d：F_edge 连续谱 vs Xu 2019 的 1% 阈值。**

Xu 2019 发现全球只有 ~1% 涡旋产生可检测 Chl rings。如果我们能证明 F_edge 是连续谱、只有 top quantile 激活可见 Chl 响应，那就直接解释了"为什么只有 1%"——这是一个 Discussion 的杀手级论点，值得专门做一个实验支撑。

**（3）跨区域从"加分项"提升为"必做项"。**

只有 Kuroshio = regional study → JGR 天花板。Gulf Stream + Agulhas 是两个动力学环境差异最大的西边界流区域，如果 peripheral strain enhancement 在三者中一致，普适性声明成立。

**（4）机制模块聚焦 front-strain alignment。**

Exp 6a 是最直接的机制证据：strain 是否沿锋面取向增强？这和 Zhang 2019 的 frontogenesis 框架直接对接。Exp 6b（light/dense side）作辅助。Exp 6c（intensification tendency）降级为 supplement——做精一个比做散三个强。

**（5）AE/CE 形态差异作为独立发现。**

SST polarity 图显示 CE 的径向 excess 向外递增——这不是 warm-core，可能反映 CE 的 tracer 响应由外围主导。这个发现如果在 Chl-a 中复现，可以独立成段：不同极性的涡旋可能有不同的主导 tracer 模式（AE = core pumping 主导，CE = peripheral strain 主导）。

### 12.5 论文主图修订（5 图）

| Fig | 内容 | 叙事功能 | vs 原规划变化 |
|-----|------|---------|-------------|
| **1** | SWOT 单案例：SSH + \|∇SSH\|_HP + strain 2D vs DUACS | 视觉冲击："传统高度计看不到" | 不变 |
| **2** | 径向 E(r/R)：三海域叠加 + controls survival | 核心物理层证据 + 普适性 | 合并原 Fig 2+3，跨区域前置 |
| **3** | **Chl-a** F_edge 分层 composite + AE/CE 形态 + lag | NC 的 "so what"——生物地球化学闭环 | **新设计**：Chl-a 取代 controls 作独立主图 |
| **4** | Front-strain alignment 机制诊断 + F_edge 连续谱 vs 1% | "why" + 解释旧谜题 | **新设计**：机制+谱分布合并 |
| **5** | Core mode vs peripheral strain mode 概念图 + 实测支撑 | 范式补完的视觉总结 | 不变 |

SST 结果（Exp 4/4b）→ Extended Data / Supplementary Figure。

---

*冻结日期: 2026-06-14 | 版本: v0.2 | Addendum: 2026-06-17 v0.4 | NC strategy: 2026-06-20 v0.5*
