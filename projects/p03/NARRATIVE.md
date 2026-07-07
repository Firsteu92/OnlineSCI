# P03 Research Narrative — Nature Communications Level

> 内部文档，用于指导论文写作的叙事骨架。非投稿文本。

---

## 一句话

中尺度涡旋不是孤立的旋转体——它们的外围是一个被传统观测隐藏的应变活跃带。SWOT 在 Kuroshio CLEAN 样本中揭示了统计稳健的涡旋相关外围应变增强，物理层信号已在双变量、双独立 control、滤波敏感性检验下通过。下一步检验它是否独立预测海表温度和叶绿素响应。

## The Story Arc（五幕结构）

### 第一幕：一个被默认的简化

过去十五年，卫星高度计为海洋中尺度涡旋建立了一个极其成功的范式：涡旋是一个由闭合 SSH 等值线定义的旋转核心，我们围绕这个核心做 composite，量化它对温度、叶绿素、碳通量的影响（Chelton et al. 2011a,b; Gaube et al. 2014）。这个"eddy-core"范式之所以成功，是因为 AVISO/DUACS 的有效分辨率（~100–200 km）恰好足以捕捉涡旋核心，但同时也意味着：**核心以外的一切——外围的梯度、应变、非轴对称结构——都被网格化过程平滑掉了。**

这不是一个错误，而是一个尚未被检验的简化。涡旋外围到底是一个安静的过渡区，还是一个动力学活跃的应变带？在 SWOT 之前，这个问题没有观测手段回答。

### 第二幕：理论预期已经存在，但缺少大样本观测验证

两条独立的理论-观测线索已经暗示涡旋外围不安静：

**线索一：应变组织线索。** Zhang et al. (2019, *Nature Communications*) 证明地转应变率是比地转动能更强的非地转运动和叶绿素变化的组织变量。但该工作基于 AVISO（~100 km 分辨率），计算的是全场应变，没有区分应变是否与涡旋相关。问题留在那里：**涡旋外围是否是应变异常集中的区域？**

**线索二：涡旋边缘机制线索。** Dong et al. (2025, *Nature Communications*) 用 Seaglider + 高分辨率模型发现，Lofoten Basin 涡旋边缘的应变通过 frontogenesis 锐化横向浮力梯度，驱动非地转二次环流，产生垂向热输送达 400 W/m² 和 ~0.4°C 的 warm ring SST 响应——在气旋和反气旋周围都存在。但这是单一海盆、依赖模型的结论。问题留在那里：**这是 Lofoten 特例还是普遍现象？没有跨海盆的卫星观测统计来回答。**

两条线索指向同一个缺口：**需要一个能在涡旋尺度上分辨外围细结构的全球观测手段，做大样本统计检验。**

### 第三幕：SWOT 打开了这个窗口——但答案不是简单的"看得更清"

SWOT KaRIn 宽幅高度计以 ~2 km 网格分辨率提供了二维 SSH 场（Archer et al. 2025, *Nature*），第一次让涡旋外围的细尺度梯度结构可以被直接观测。

但如果仅仅是"分辨率更高所以看到更多"，这就是一篇技术笔记而不是科学发现。**关键的概念跃升是：** 我们不再问"SWOT 看到的涡旋边界在哪里"（几何问题），而是问"涡旋外围是否存在系统性的细尺度应变增强"（物理组织问题）。

这个转向来自一个 null result：我们的先导实验（16 个 Kuroshio Extension 原型案例）检验了 SWOT 是否系统性地改写涡旋边界半径——结果发现没有（5 个干净案例的 ΔR 符号混合）。SWOT 不是简单地把边界往外推或往内缩。**被隐藏的不是边界的位置，而是边界区域内部的动力学结构。**

### 第四幕：涡旋外围应变增强——从假说到证据

我们将 2,956 个 CLEAN SWOT–涡旋匹配对的外围（0.9–1.5 R 环带）细尺度应变率与独立 matched controls 对比。已完成 displaced control（局地平移 3–5R）和 same-swath random control，以及三项加固诊断：方位角连续性（control-subtracted sector excess，确认信号不对称不上 halo）、vorticity/OW 分解（Q_OW 分离 rotation-core 与 strain-periphery）、SwotDiag 求导一致性（r=0.85）。Background-strain matched 和 isolated-eddy subset 为下一步加固项。

如果涡旋外围的应变增强在 matched controls 后仍然显著，那么这种增强可被表述为 eddy-associated，而非仅由随机 swath geometry 或局地背景平均水平解释。

这是第一层（lock-box，纯 SWOT SSH）的结论。

第二层打开 lock-box：将涡旋按外围应变强度分组，检验应变更强的涡旋是否表现出更强的 SST 和 Chl-a 响应。predictor（应变）和 response（示踪物）严格分离，避免循环论证。**如果应变增强独立预测示踪物响应，那么涡旋外围就不只是一个几何边界，而是一个功能性的动力学区域。**

### 第五幕：从 eddy-core 到 eddy-system——范式补完

如果上述证据链成立，结论不是"eddy-core 范式是错的"，而是**它是不完整的**。

传统范式只看到涡旋的一种影响模式：核心垂向泵浦（core mode）。我们提出的是并存的第二种模式：**外围应变模式（peripheral strain mode）——涡旋通过其外围的细尺度应变场组织侧向混合、frontogenesis 和示踪物交换。** 两种模式共存于同一个涡旋，但作用于不同的径向位置、通过不同的物理机制、影响不同的尺度。

这个补完有三重意义：

1. **解释旧谜题。** Xu et al. (2019) 发现全球只有 ~1% 的涡旋产生可检测的叶绿素环。如果 peripheral strain 是连续谱而非全有全无，那么"为什么只有 1%"的答案就是：不是 1% 的涡旋特殊，而是只有处于高应变环境中的涡旋才激活了 peripheral strain mode。
2. **修正 composite 方法。** 传统 eddy-centric composite 将所有涡旋等权平均，把应变活跃和应变安静的涡旋混在一起，稀释了外围信号。按 F_edge（外围应变增强分数）分层 composite，可以恢复被稀释的信号。
3. **连接尺度。** 中尺度涡旋是海洋中最大的可识别结构，但它们如何向下级联能量、如何驱动亚中尺度混合，一直是理论推断多于观测约束。peripheral strain 提供了一个可观测的中间变量：**中尺度涡旋通过外围应变场组织细尺度过程，SWOT 让这个中间环节第一次可以被统计量化。**

---

## 标题备选

1. **Mesoscale eddies organize fine-scale strain beyond their conventional boundaries** — 强调"beyond boundaries"的发现
2. **A hidden strain mode around ocean eddies revealed by wide-swath altimetry** — 强调"hidden"和新观测手段
3. **Peripheral strain enhancement around mesoscale eddies links eddy identity to surface tracer response** — 强调 predictor-response 闭环
4. **The missing periphery: SWOT reveals strain-active zones around catalogued ocean eddies** — 最直接

推荐: **#1** — 简洁、准确、不过度声称、暗示范式修正。

---

## 论文结构映射

| 论文部分 | 叙事幕 | 核心要传达的信息 |
|---------|--------|----------------|
| Abstract | 全部浓缩 | 涡旋外围存在 SWOT 才能解析的应变增强（H1），且独立预测 tracer response（H2） |
| Introduction ¶1 | 第一幕 | Eddy-core 范式的成功与默认简化 |
| Introduction ¶2 | 第二幕 | 两条独立线索：strain organizing（Zhang 2019）+ edge mechanism（Dong 2025） |
| Introduction ¶3 | 第三幕前半 | SWOT 的观测能力（Archer 2025）+ 为什么不是分辨率比较 |
| Introduction ¶4 | — | 本文做什么：两层 lock-box，四类 controls，跨区域统计 |
| Results §1 | 第四幕上 | Excess peripheral strain profile E(r/R)，composite maps |
| Results §2 | 第四幕上 | Filter-scale sensitivity + controls survival |
| Results §3 | 第四幕下 | F_edge vs SST/Chl-a response（第二层） |
| Results §4 | 第四幕下 | 跨区域一致性（Kuroshio / Gulf Stream / Agulhas） |
| Discussion ¶1 | 第五幕 | Core mode + peripheral strain mode 并存 |
| Discussion ¶2 | 第五幕 | 解释 ~1% Chl rings 之谜 |
| Discussion ¶3 | 第五幕 | Composite 方法的修正建议 |
| Discussion ¶4 | — | Limitations：snapshot claim, 21-day sampling, strain ≠ causation |
| Discussion ¶5 | 第五幕 | 尺度连接：中尺度 → 亚中尺度的可观测中间变量 |

---

## 核心 Figure 规划（5 主图）— 2026-06-20 修订

> 修订原则：Chl-a 升为主证据线，SST 降至 Extended Data。跨区域前置进主图。

| Fig | 内容 | 叙事功能 |
|-----|------|---------|
| **1** | SWOT 单案例展示：一个涡旋的 SSH、\|∇SSH\|_HP、strain rate 二维图 + DUACS 同位置对比 | "这就是传统高度计看不到的东西"——视觉冲击力 |
| **2** | 径向 E(r/R)：三海域（Kuroshio / Gulf Stream / Agulhas）叠加 + background-strain matched + filter sensitivity | 核心物理证据 + 普适性 + robustness 合一；合并原 Fig 2+3 |
| **3** | **Chl-a**: F_edge 分层 radial composite（AE/CE 分开）+ lag 时间序列 + 2D composite 差图 | NC 的 "so what"——生物地球化学闭环，取代 SST 回归作为主 tracer 证据 |
| **4** | 机制：front-strain alignment 诊断 + F_edge 连续谱 vs Xu 2019 的 1% 阈值检验 | "why" + 解释 "为什么只有 1% 涡旋有 Chl rings" |
| **5** | 概念模型：core mode vs peripheral strain mode 双模示意图，附实测 composite 支撑 | 范式补完的视觉总结 |

**Extended Data / Supplementary:**
- ED Fig 1: SST radial composite + AE/CE 形态差异（Exp 4/4b）
- ED Fig 2: Azimuthal sector analysis（Exp 1d）
- ED Fig 3: Q_OW 核-外围分解（Exp 1e）
- ED Fig 4: Isolated-eddy subset 结果（Exp 1h）
- Supp Table 1: 各区域样本量、effect size、p 值汇总

---

## 口径红线（论文中不能说的话）

1. 不说"eddy boundaries are wrong"——说 conventional boundaries capture the core but miss the periphery
2. 不说"peripheral strain causes tracer anomalies"——说 predicts / covaries with / is associated with
3. 不说"halo" 除非数据证实环状连续性——主文用 peripheral strain enhancement
4. 不说"SWOT is better than AVISO"——说 SWOT resolves structures that gridded altimetry smooths by design
5. 不说"all eddies have active peripheries"——说 peripheral strain enhancement is a continuous spectrum; eddies in the upper quantiles show significantly stronger tracer responses
6. 不说 lifecycle evolution——所有结论限定为 snapshot statistical claims

---

## 为什么这是 NC 而不是 GRL

| 维度 | GRL 水平 | NC 水平（本文目标） |
|------|---------|-------------------|
| 发现 | 涡旋外围存在 SWOT 可见的应变增强 | + 这种增强独立预测 tracer response |
| 方法 | 单区域 composite | + 跨区域（≥3）一致性 |
| 影响 | 技术观测报告 | + 修正 eddy-core composite 范式 |
| 叙事 | "SWOT sees more" | "eddy paradigm is incomplete" |
| Controls | 一两类 | 四类 matched controls + synthetic-front null |

**关键判据：** 如果只有第一层（物理存在性），是 GRL/JGR。第一层 + 第二层（tracer 闭环）+ 跨区域一致性 = NC。

**2026-06-20 更新**：Chl-a 升为主 tracer 证据线（SST ΔR²=0.012 不足以支撑 NC tracer claim）。跨区域从加分项改为必做项。详见 DIRECTION.md §12。

---

*版本: v0.1 | 2026-06-15 | 修订: v0.2 | 2026-06-20*
