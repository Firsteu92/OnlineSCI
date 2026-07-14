# Data Management — 数据管理

## 核心原则

**GitHub 仓库不存储原始数据文件，只保存数据的元信息和访问方式。**

## 数据存储规则

| 应上传 | 不应上传 |
|--------|----------|
| 数据下载脚本 | 原始数据文件（.nc, .hdf5, .mat, .csv 等大文件） |
| 数据源 URL/DOI | 中间处理结果 |
| 数据说明文档 | 临时缓存文件 |
| 数据 Manifest | 本地配置文件 |
| 校验和文件 | 密钥和凭证 |

## 数据目录结构（每项目）

```
data/
├── README.md          # 数据目录说明
├── data_manifest.yml  # 所有数据集的元数据
├── checksums/         # 校验和文件
└── samples/           # 小样本文件（可选）
```

## 数据 Manifest 格式

```yaml
datasets:
  - id: "dataset_name"
    source: "CMEMS / ERA5 / 本地采集"
    url: "https://..."
    version: "v1.0"
    access_date: "2026-07-14"
    license: "CC-BY 4.0 / 专有"
    checksum: "sha256:..."
    notes: "使用方法和注意事项"
```

## 大型数据存储

真实大型数据应存储在本地、服务器或合规云存储中。路径、版本、来源和校验信息写入 `data_manifest.yml`。

## 数据引用

所有使用的数据集必须在论文中正确引用，包括 DOI 和版本号。
