# SWOT 文献调研 — P03

> 调研日期: 2026-06-09 | 更新: 2026-06-14（补充 Stage 2 相关文献：strain framework + warm ring + Antarctic + Lagrangian）

---

## 1. Archer et al. (2025) — Nature

**Wide-swath satellite altimetry unveils global submesoscale ocean dynamics**

DOI: 10.1038/s41586-025-08722-8 | 代码: Zenodo (10.5281/zenodo.14736001)

### 产品与预处理
- 同时使用 L2 Unsmoothed (250m, PIC0) 和 L3 Expert (2km, v1.0)
- L2 用于展示 (Fig.1,3)，L3 用于分析 (Fig.2,4)
- 预处理链：去 MSS → 沿轨线性趋势（roll error）→ 50km 2D Gaussian 高通（残留地形）→ quality flag → 6km boxcar → SSH 梯度
- 地转流有效分辨率: ≥8.5 km 直径（Chelton 噪声估计）
- Ro > 0.5 时地转失效，需 cyclogeostrophy: V(r) = −fr/2 + (f²r²/4 − g·SSHA)^(1/2)

### 核心发现
- SWOT-DUACS RMS 差异在 WBC 和 ACC 最显著
- 50km 高通 SWOT SSHA RMS 揭示了全球 submesoscale 分布
- 单个 submesoscale eddy (r~15km, SSHA~15cm): Ro > 0.5, 地转流 ~1 m/s, 旋衡流 ~0.5 m/s
- Submesoscale RMS SSHA 约为最高分辨率全球模拟的 3 倍
- 垂直速度估计: −6 至 −14 m/day

### 对 P03
预处理 pipeline 是黄金标准。Cyclogeostrophy 对小涡旋必须。SSH-内波信号分离仍是无解问题。

---

## 2. Carli et al. (2025) — JGR Oceans

**Southern Ocean 3D eddy diagnostics derived from SWOT**

DOI: 10.1029/2024JC022307 | 代码: SwotDiag (github.com/treden/SwotDiag, MIT)

### 方法
- SWOT L3 Basic v1.0 (2km)，5 天相邻 swath
- **SwotDiag 拟合核方法**: n×n 像素滑动窗口内 2D 多项式最小二乘曲面拟合，系数直接给出 dx, dy, dxx, dxy, dyy
- 本研究用 9-pt kernel (~18 km 拟合尺度)，circular kernel 减少角点噪声
- Lanczos 低通滤波 100km 做尺度分离
- 2D 网格化仅用于 eSQG 垂直速度（Verde bicubic spline, 0.07°）

### 核心发现
- 小尺度 (<100 km) 应变率可达大尺度的 3 倍
- 小尺度涡度可达大尺度的 10 倍
- SWOT 小尺度 OW 偏度 −1（MIOST 为 −3）: 应变和涡度趋于平衡，filamentary 结构取代 isotropic 结构
- SWOT w RMS (~24 m/day @ 500m) 是 MIOST/VarDyn 的 2 倍

### 对 P03
SwotDiag 是最核心的代码资产。OW 分布偏移的发现直接支持"不能分别检测"的决策。9-pt circular kernel 经校验可直接复用。

---

## 3. De Marez et al. (2026) — Ocean Science + Nature Geoscience preprint

**SWOT reveals mesoscale eddy hotspots and deserts in subpolar and polar oceans**

DOI (OS): os-22-1515-2026 | DOI (NG preprint): 10.21203/rs.3.rs-8396214/v1 | 代码: 未公开

### 方法 — 第一篇在 SWOT 原生 swath 上跑 py-eddy-tracker
- SWOT L3 Basic v2.0.1→v3.0 (2km)，filtered SLA (U-Net 降噪 2×)
- **128×128 像素滑动窗口**（64 像素重叠）→ **双调和修复**（biharmonic inpainting, skimage）填补空洞
- py-eddy-tracker，**shape_error=85%**（大幅放宽，最大化检测数）
- 筛选: 半径 ≥5 km, 振幅 ≥0.01 m, 空洞率 <40%, 海冰 <15%

### 核心发现
| | SWOT | DUACS (1/4°) | SADCP |
|---|---|---|---|
| 平均半径 | **14 km** | 42 km | 15 km |
| 平均 Vmax | **20 cm/s** | 8 cm/s | 26 cm/s |
- DUACS 漏掉所有半径 <25 km 的涡旋
- 确认"涡旋沙漠"（冰岛以北、威德尔海）
- v3.0 修复了 v2.0.1 的虚假小气旋涡问题

### 对 P03
滑动窗口 + biharmonic inpainting 方法可直接复用。但 shape_error=85% 对密度普查最优，对边界分析太宽松。P03 应收紧到 55-70%。他们不做 core-vs-rim 对比——这是我们的切入点。

---

## 4. Zhang et al. (2024) — GRL

**Submesoscale eddies detected by SWOT and moored observations in the northwestern Pacific**

DOI: 10.1029/2024GL110000 | 代码: 无

### 方法
- SWOT L3 Expert v1.0 (2km)，CalVal 阶段（1天重复周期）
- **纯手动检测**: ΔSLA = SWOT SLA − DUACS SLA，目视寻找闭合负 ΔSLA 等值线
- 涡旋边界 = 最外层闭合 ΔSLA 等值线
- 系泊验证：4 个系泊（7.5km 间距），Stokes 定理计算涡度
- 流速滤波：4 阶 Butterworth 48h 低通（去 IGW）+ 16 天高通（提取亚中尺度）

### 核心发现
- 两个 SCE：等值半径 16.0/18.8 km，SLA 振幅 2.5/2.0 cm
- 系泊 Ro ~0.4，但系泊在 50m 以浅无数据——真实表面 Ro 应更大
- SWOT 可可靠检测 >10 km 的亚中尺度涡旋
- 持续时间：15 天 / 9 天

### 对 P03
ΔSLA 方法简单有效。系泊验证策略（涡度、Ro、位势高度对比）可供参考。无自动检测方法。

---

## 5. Jensen et al. (2025) — GRL

**SWOT observations unveil small mesoscale variability on the East Greenland shelf**

DOI: 10.1029/2025GL118573 | 代码: MASSH (github.com/leguillf/MASSH)

### 方法
- SWOT L2 LR SSH (2km) + 5 颗 nadir 卫星
- BFN-QG 同化（MASSH）：1.5 层 QG 模型，10 天窗口 3 天步进
- SWOT nudging 权重为 nadir 的 10 倍
- Roll error 修正：100×100km 滑动窗口一阶多项式拟合 + Hanning 平滑
- 仅视觉识别零涡度等值线，无自动 eddy detection

### 核心发现
- 20 km anticyclonic eddy：SWOT 清晰捕捉，DUACS 完全看不到
- SWOT 地转流 0.3-0.6 m/s vs DUACS 0.15-0.3 m/s
- 200km 高通滤波后 SWOT-SST 相关性显著优于 DUACS

### 对 P03
Roll error 修正方法可参考。BFN-QG 输出场可在 DUACS 涡旋中心做对照验证，但 QG 同化会平滑梯度（对 rim detection 不利）。

---

## 6. Verger-Miralles et al. (2025) — GRL

**SWOT enhances small-scale eddy detection in the Mediterranean Sea**

DOI: 10.1029/2025GL116480 | 代码: github.com/everger-miralles/paper_GRL_Verger-Miralles_etal_2025

### 方法
- SWOT L3 Expert v2.0.1 (2km)，手动识别单个 Mallorca ITE (~25km radius)
- 验证：glider 位势高度 + ADCP 断面 + SVP-B drifter
- ADCP 滤波：15-km Butterworth（基于区域 R_D ~10-15 km）

### 核心发现
- SWOT SSH RMSD vs glider: 0.62 cm (−24% vs DUACS)
- SWOT 速度 RMSD vs ADCP: 8.9 cm/s (−35% vs DUACS)
- SWOT Ro ~0.5 vs ADCP ~0.4-0.56，DUACS Ro ~0.1 严重低估
- 结果对 L3 产品版本选择敏感

### 对 P03
SWOT 在中尺度下边界的 SSH/速度误差基准。15-km Butterworth cutoff 可参考。单一涡旋案例，方法论参考有限。

---

## 边缘活性 / tracer response 相关文献（新增）

### 7. Xu et al. (2019) — Scientific Reports

**Chlorophyll rings around ocean eddies in the North Pacific**

DOI: 10.1038/s41598-018-38457-8

**核心发现**：
- 在北太平洋大样本中识别 cyclonic 和 anticyclonic eddies 周围的 chlorophyll rings (CRs)
- **仅 ~1% mesoscale eddies associated with CRs**，但对 basin-scale chlorophyll 贡献不成比例
- CRs 更多出现在 eddy periphery 而非 core

**与 P03/新方向关系**: 这是"rare but active edges"最直接的文献入口。SWOT 可能回答为什么只有这 ~1% 的 eddies 产生边缘信号。

### 8. Gaube et al. (2014) — JGR Oceans

**Regional variations in the influence of mesoscale eddies on near-surface chlorophyll**

DOI: 10.1002/2014JC010111

**核心发现**：
- Eddy 对 chlorophyll 的影响高度区域依赖，与背景梯度、混合层深度、光照相关
- 并非所有 eddies 都产生可检测的 Chl signal

**与 P03/新方向关系**: 为"eddy identity 不足以预测 tracer response"提供文献基础。

### 9. Chelton et al. (2011a) — Progress in Oceanography

**Global observations of nonlinear mesoscale eddies**

DOI: 10.1016/j.pocean.2011.01.002

**核心发现**：
- 全球 mesoscale eddy 统计：数量、半径、振幅、寿命、传播特征
- py-eddy-tracker 方法学基础

**与 P03/新方向关系**: PET 涡旋检测的标准参考，已用于 P03 pipeline。

### 10. Chelton et al. (2011b) — Science

**The influence of nonlinear mesoscale eddies on near-surface chlorophyll**

DOI: 10.1126/science.1208897

**核心发现**：
- 首次大样本证明 AE/CE 在 chlorophyll 上的不同响应
- AE → 负 Chl anomaly（downwelling），CE → 正 Chl anomaly（upwelling）

**与 P03/新方向关系**: Eddy-tracer 关系的奠基性论文。新方向需要解释为什么有些 eddies 偏离这个平均模式。

### 11. Pegliasco et al. (2022) — ESSD

**META3.1exp: A new global mesoscale eddy trajectory atlas derived from altimetry**

DOI: 10.5194/essd-14-1087-2022

**核心发现**：
- META3.1 涡旋追踪数据集，含闭合 SSH contour

**与 P03/新方向关系**: PET contour 数据的来源和格式参考，决定我们能否实现 contour-relative fragment 采样。

---

## 涡旋边界 / 输运理论背景（可选补充）

### 12. Beron-Vera et al. (2008) — GRL

**Oceanic mesoscale eddies as revealed by Lagrangian coherent structures**

DOI: 10.1029/2008GL033957

### 13. Haller & Beron-Vera (2013) — JFM

**Coherent Lagrangian vortices: The black holes of turbulence**

DOI: 10.1017/jfm.2013.391

### 14. McGillicuddy (2016) — AR Marine Science

**Mechanisms of physical-biological coupling in ocean eddies**

DOI: 10.1146/annurev-marine-010814-015606

---

## Stage 2 关键文献：Strain Framework + Halo 机制 + 互补方向

### 15. Zhang et al. (2019) — Nature Communications

**The influence of geostrophic strain on oceanic ageostrophic motion and surface chlorophyll**

DOI: 10.1038/s41467-019-10883-w

**核心发现**：
- 地转应变率 S_g 是比 EKE 更强的 ageostrophic KE 和 chlorophyll 变化的组织变量
- 在强 strain 区（S_g > 1.0×10^−5 s^−1），ageostrophic KE 和 Chl 增加趋势明确
- strain-induced frontal processes：Chl 增加沿锋面 light side，伴随 secondary ageostrophic upwelling
- 平衡态 ageostrophic motion 比非平衡态（波动）更有效驱动 Chl 增加

**方法模板**：
- S_g = √[(∂u/∂x−∂v/∂y)² + (∂v/∂x+∂u/∂y)²]，来自 AVISO 地转流
- 找 strain saddle points 做 composite，旋转到 along-front / cross-front 坐标
- predictor（物理 strain）和 response（log Chl tendency）严格分离
- 用 log Chl 而非 Chl（跨量级变化）

**对 P03 Stage 2**: 这是我们 strain halo 变量体系的核心文献来源。S_g 定义、strain-patch composite 方法、predictor-response 分离逻辑全部直接继承。

---

### 16. Dong et al. (2025) — Nature Communications

**Warm rings in mesoscale eddies in a cold straining ocean**

DOI: 10.1038/s41467-025-64308-y

**核心发现**：
- Lofoten Basin（sub-Arctic）：5 年 Seaglider + satellite + 2.4 km model
- 涡旋边缘的 geostrophic strain 通过 frontogenesis sharpening 横向浮力梯度 → ageostrophic secondary circulation
- 垂向速度达 60 m/day（>500 m 深度），垂向热输送 VHT ~400 W/m²（局地 1600 W/m²）
- 在 **AE 和 CE 周围都形成 warm ring**（1–10 km 尺度，~0.4°C SST 增暖）
- VHT 超过区域海气热通量 3 倍以上

**方法模板**：
- r/R 归一化 eddy coordinates（center → 2R）
- 按 strain intensity 分组对比 VHT 和 SSTa
- AE 和 CE 分开 composite，但关注 polarity-independent 的 ring 响应
- 应变带和浮力梯度带位于涡旋周围环状区域

**对 P03 Stage 2**: "halo 存在"最直接的前人观测证据。但仅限于 Lofoten Basin + 模型，不是 SWOT 观测。我们增量：用 SWOT 实测检验跨海盆的 halo 存在性。

**注意**：Dong 2025 的 warm ring 是温度响应（~0.4°C），需要高分辨率 SST 才能分辨。如果用粗分辨率 SST（如 OSTIA 5 km），1–10 km 的 warm ring 会被平均掉。P03 Stage 2b 需要评估 SST 产品选择。

---

### 17. Han et al. (2026) — National Science Review

**High coastal eddy activity around Antarctica revealed by SWOT**

DOI: 10.1093/nsr/nwag181

**核心发现**：
- 首次 pan-Antarctic SWOT eddy detection
- ~70% 涡旋半径 <10 km，振幅 <2 cm，强度 5–20 cm/s
- 两种生成机制：冰架基底融水（Bellingshausen–Amundsen）和 Dense Shelf Water 输出（Ross Sea）
- 用 MITgcm  idealized simulation 确认两种机制独立生成涡旋

**对 P03 Stage 2**: 模板价值在于"高空 activity 作为隐藏过程的表面指示器 + 独立机制支持"的论证结构。我们不重复做 eddy detection（已有 PET registry），但可借鉴其 eddy activity → hidden process 的逻辑。

---

### 18. Liu et al. (2026) — Geophysical Research Letters

**Hidden Fine-Scale Transport Pathways and Biological Connectivity Revealed by SWOT**

DOI: 10.1029/2025GL121208

**核心发现**：
- South China Sea SWOT 数据构建 Lagrangian flow network
- SWOT 网络揭示 2–10 天、O(10) km 尺度的 transport pathways
- 识别出更多 sinks / sources / transport gateways
- SWOT-derived 水动力省份更好解释浮游植物群落结构

**对 P03 Stage 2**: 这是我们需要刻意**避开**的方向。Liu 2026 做的是全场景 Lagrangian network，我们做的是 eddy-centric strain organization。互补但不重叠。

---

## 跨论文综合结论

1. **SWOT eddy-periphery strain 检测是空白**。六篇 SWOT 观测论文无一定义或检测 eddy-edge/periphery strain enhancement。
2. **py-eddy-tracker 可跑在 SWOT 上**（De Marez 已验证），但参数需调整。
3. **OW 参数不通用**（Carli 数据证实），支持 AVISO-detect → SWOT-measure 策略。
4. **SwotDiag + Archer pipeline + De Marez gap-handling** 构成 P03 的完整技术栈。
5. **v3.0 是最优产品选择**，覆盖全任务周期，修复了 v2.0.1 的已知问题。
6. **Xu 2019 的 ~1% CRs 概率是入口**：为什么只有极少数涡旋产生强边缘信号？→ 可能因为它们恰好有强 peripheral strain enhancement。
7. **Zhang 2019 提供 strain predictor 框架**：S_g 定义、strain-saddle composite、predictor-response 分离逻辑可直接继承。
8. **Dong 2025 提供 eddy-edge strain → thermal response 机制链**：但仅限于单 basin + 模型。我们用 SWOT 实测跨海盆统计检验 strain enhancement 本身，而非 warm ring。
9. **Han 2026 + Liu 2026 提供互补方向**：分别聚焦 eddy detection 和 Lagrangian network。P03 刻意避开这两个方向，聚焦 eddy-centric peripheral strain organization。
10. **Chen & Chen 2025 JGR** 确认 DUACS 极性可靠（~3% 异常），防御性引用：DUACS AE/CE stratified composites 可靠。
