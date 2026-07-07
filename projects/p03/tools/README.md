# P03 数据下载工具箱

本目录存放可复用的数据下载脚本和来源记录。

## MUR SST

**脚本**: `download_mur_sst.sh` — PO.DAAC MUR-JPL-L4-GLOB-v4.1 子区域下载（NASA Harmony 裁剪）。

**来源**: https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1

**用法示例**:
```bash
# Kuroshio 区域 2023-07 一个月
bash download_mur_sst.sh 2023-07-01 2023-08-01 130 28 170 42 D:/data/MUR_SST

# 全周期下载 (2023-07 ~ 2025-10)，P03 匹配范围
bash download_mur_sst.sh 2023-07-01 2025-11-01 130 28 170 42 D:/data/MUR_SST
```

## SWOT L3 SSH

**产品**: SWOT_L3_LR_SSH Expert v3.0 (2 km, <12 MB/file)

**来源**: [AVISO SWOT L3 Ocean Products](https://www.aviso.altimetry.fr/en/data/products/sea-surface-height-products/global/swot-l3-ocean-products.html)

**获取方式**: AVISO FTP/SFTP（需 AVISO+ 账号）

```
ftp://ftp-access.aviso.altimetry.fr/swot_products/l3_karin_nadir/l3_lr_ssh
sftp://ftp-access.aviso.altimetry.fr:2221/swot_products/l3_karin_nadir/l3_lr_ssh
```

THREDDS 浏览: https://tds-odatis.aviso.altimetry.fr/thredds/catalog/dataset-l3-swot-karin-nadir-validated/l3_lr_ssh/catalog.html

**存储路径**:
- 本地: `H:\Eddy_SWOT\data\` (按 cycle/pass 组织结构)
- HPC: `/slurm/zhangzs/SWOT/Expert/` (reproc/ + forward/ cycle 目录)
