# P04 v2 数据路径登记（DATA_PATHS.md）

> 约定：**大体积数据下载一律在远程办公室台式机执行**，不占用 Mac 本地磁盘。
> 小型衍生产物（JSON/PNG/CSV）回传本仓库；大型 .nc 留在远程。

## 远程（办公室 Windows / WSL）

| 数据集 | 远程路径（WSL 视角） | 变量 | 时段 | 分辨率 | 生成脚本 | 状态 |
|---|---|---|---|---|---|---|
| ERA5 波浪产品 | (远程 WSL `p04v2_data/`) | SWH, MWP, MWD | 1979-2024 | 0.5°, 月均 | `analysis/p04v2_download_era5_waves.py` | ❌ 待下载 |
| ERA5 10m 风 | (远程 WSL `p04v2_data/`) | u10, v10 | 1979-2024 | 0.25°, 月均 | 同上 | ❌ 待下载 |
| ERA5 海冰浓度 | (远程 WSL `p04v2_data/`) | siconc | 1979-2024 | 0.25°, 月均 | 同上 | ❌ 待下载 |

## 本地 Mac（已有，v1 遗留可复用的小文件）

| 数据集 | 本地路径 | 变量 | 时段 | 状态 |
|---|---|---|---|---|
| NSIDC 海冰指数 | `data/NSIDC Sea Ice Index/S_*.csv` | 南极月度 extent/area | 1979-2026 | ✅ 已有 |
| 气候指数 AAO | `data/climate-indices/aao_monthly.txt` | AAO 月度 | 1979-2024 | ✅ 已有 |
| 气候指数 Niño3.4 | `data/climate-indices/nino34_ersst.txt` | Niño3.4 月度 | 1950-2024 | ✅ 已有 |
| 气候指数 SAM/PDO/SOI | `data/climate-indices/` | 多个指数 | 各异 | ✅ 已有 |

## 衍生产物（分析产出，commit 到仓库）

| 产物 | 路径 | 内容 | 生成脚本 | 状态 |
|---|---|---|---|---|
| Fetch 月度时序 | `analysis/p04v2_fetch_timeseries.csv` | 环南极分区 fetch 月均 | TBD | ❌ 待开发 |
| MIZ 宽度时序 | `analysis/p04v2_miz_width.csv` | 经向 MIZ 宽度 | TBD | ❌ 待开发 |
| 冰架缓冲天数 | `analysis/p04v2_shelf_buffer.csv` | 5 个冰架的缓冲天数年际 | TBD | ❌ 待开发 |
| 反馈增益 | `analysis/p04v2_feedback_gain.csv` | 滚动回归 feedback gain | TBD | ❌ 待开发 |

## 远程→本地回传方式

- **坚果云中转**：远程结果文件放入坚果云同步目录，Mac 自动同步
- **小文件 scp**：从远程 scp 回传到本地
- **结果 JSON/CSV**：直接回传后 git commit

## CDS API 凭证

- 远程 WSL：`~/.cdsapirc`（✅ 已确认）
- 本地 Mac：`~/.cdsapirc`（✅ 已有）
