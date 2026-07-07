# 核心参考文献（L1 摘要级）

> 两层阅读规则：L1 摘要级（默认）→ L2 全文级（按需升级）。
> 升级 L2 由 A 在某轮触发：B 要求"对照 refXX 重新论证"，或 A 自己发现 take-away 不足。

---

## Ref01: Delplace et al. (2017) — 理论锚点 [已 L2 精读]

**Citation**: Delplace, P., Marston, J. B., & Venaille, A. (2017). Topological origin of equatorial waves. *Science*, 358, 1075–1077.

**Role**: 理论基座 — 本文整个科学问题的出发点

**Key take-aways**:
1. 赤道 Kelvin/Yanai 波是拓扑边界态，由 Coriolis 参数 f 在赤道变号（时间反演对称性破缺）产生
2. Bulk Poincaré 波模的 Chern 数 = ±2，通过 bulk-boundary correspondence 保证恰好 2 个单向边界态存在
3. 拓扑保护不依赖地球精确几何（"even a misshapen sphere would support the waves"）
4. 理论仅在理想旋转浅水模型中成立——非 Hermitian（耗散+平均流）和非线性效应是 open questions

**Our use**: 我们检验 take-away 3 在真实海洋中的适用边界，take-away 4 中列出的 open questions 正是我们的研究内容

**Full text**: `literature/delplace2017_topological_origin_equatorial_waves.pdf`

---

## Ref02: 赤道波动力学经典教材 — 方法学参考 [L1]

**Citation**: Vallis, G. K. (2017). *Atmospheric and Oceanic Fluid Dynamics: Fundamentals and Large-Scale Circulation*. Cambridge Univ. Press, ed. 2.

**Role**: 方法学 — 赤道浅水模型、Kelvin/Yanai/Rossby 波色散关系、β-平面近似

**Key take-aways**:
1. 赤道 Kelvin 波色散：ω = c·k_x（非色散，东传）
2. Yanai 波色散：混合 Rossby-重力波，低频西传、高频东传
3. 等效深度 H_eq 和相速度 c = √(g'·H_eq) 的定义
4. 赤道变形半径 L_eq = √(c/β) 决定波的经向约束尺度

**Our use**: 所有理论预言（色散关系、经向结构、相速度）的基准；Δω_eff 估计的理论基础

---

## Ref03: SWOT 任务概述 — 观测能力参考 [L1]

**Citation**: SWOT Mission (2023–). NASA/JPL-CNES joint mission. 

**Role**: 观测数据源 — SWOT KaRIn 宽刈幅 SSH 的技术参数和数据产品

**Key take-aways**:
1. KaRIn 刈幅 ~120 km（2×50 km + 20 km nadir gap），沿轨分辨率 ~2 km
2. 科学轨道重访周期 ~21 天；calval 快速轨道 ~1 天（2023.03–07）
3. L2 LR SSH 是分级产品，L3 是网格化；L2 Expert 包含完整诊断
4. 赤道附近地转近似退化，SSH→地转流反演需谨慎

**Our use**: 核心数据源的技术限制决定了我们能做什么和不能做什么；时间采样限制是最大挑战
