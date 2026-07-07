# P04 v2 数据清单（data_inventory.md）

## 已有数据（本地）

| 数据集 | 本地路径 | 状态 | 说明 |
|---|---|---|---|
| ERA5 u10/v10 | `data/ERA5/era5_wind.nc` | ❌ 仅 README | 原始 NC 未入 git，需重新下载或从远程台式机同步 |
| ERA5 SIC | `data/data_stream-moda_stepType-avgua.nc` | ❌ 仅 README | 同上 |
| CMEMS SSH | `data/CMEMS-SSH/*.nc` | ❌ 仅 README | 同上 |
| NSIDC 海冰指数 | `data/NSIDC Sea Ice Index/*.csv` | ✅ 已有 | 12 个月度 CSV，1979-2026 |
| 气候指数 | `data/climate-indices/*.txt` | ✅ 已有 | AAO/Niño3.4/PDO/SOI |
| CNES MDT | `data/cnes_*.nc` | ❌ | v2 不需要 |

## 需新下载的数据

### 1. ERA5 波浪产品（核心新数据）

| 变量 | CDS 名称 | 分辨率 | 时段 | 估计大小 |
|---|---|---|---|---|
| Significant wave height | `significant_height_of_combined_wind_waves_and_swell` (swh) | 0.5°, 月均 | 1979-2024 | ~200 MB |
| Mean wave period | `mean_wave_period` (mwp) | 0.5°, 月均 | 1979-2024 | ~200 MB |
| Mean wave direction | `mean_wave_direction` (mwd) | 0.5°, 月均 | 1979-2024 | ~200 MB |

**下载方式**: CDS API (`cdsapi`)，产品 `reanalysis-era5-single-levels-monthly-means`

### 2. ERA5 风场 + SIC（重下载，v1 已用但本地无数据）

与 v1 相同参数，需重新下载到本地或从远程台式机同步。

**优先方案**: 先检查远程台式机是否有 v1 时下载的数据。

### 3. 冰架位置数据

| 数据集 | 来源 | 格式 |
|---|---|---|
| MEaSUREs Antarctic boundaries | NSIDC | Shapefile |
| Antarctic coastline/grounding line | BedMachine | GeoTIFF/NetCDF |

## 下载执行计划

1. **P0-1**: 先 SSH 检查远程台式机是否有 v1 的 ERA5 数据
2. **P0-2**: 用 CDS API 下载 ERA5 波浪产品（SWH/MWP/MWD）
3. **P0-3**: 若远程无 v1 数据，重新下载 ERA5 风场+SIC
4. **P0-4**: 下载冰架边界数据

所有下载任务优先在远程台式机 WSL 执行（见 `data-download-guide` skill）。
