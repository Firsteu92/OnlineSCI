#!/bin/bash
# download_mur_sst.sh — MUR SST 子区域下载脚本（可复用）
#
# 用法:
#   bash download_mur_sst.sh <START_DATE> <END_DATE> <W_LON> <S_LAT> <E_LON> <N_LAT> [OUTPUT_DIR]
#
# 示例:
#   bash download_mur_sst.sh 2023-07-01 2023-08-01 130 28 170 42 D:/data/MUR_SST
#
# 安装: pip install podaac-data-submitter（一次性），然后去 https://urs.earthdata.nasa.gov 注册
#   Earthdata 账号，在 ~/.netrc (Windows: ~/_netrc) 写入 machine/ login/ password 三行即可使用。
#
# 说明:
#   - 使用 NASA Harmony API 做 on-the-fly 子区域裁剪（--subset）
#   - 原始全球文件 ~700 MB/天，裁剪后 ~12 MB/天（Kuroshio 区域）
#   - 已下载的文件会自动跳过（checksum 校验），断点续传安全
#   - 集合名: MUR-JPL-L4-GLOB-v4.1 (0.01°, daily L4)

# ---- 参数 ----
START=${1:?需要 START_DATE (YYYY-MM-DD)}
END=${2:?需要 END_DATE (YYYY-MM-DD)}
WLON=${3:?需要 W_LON}
SLAT=${4:?需要 S_LAT}
ELON=${5:?需要 E_LON}
NLAT=${6:?需要 N_LAT}
OUTDIR=${7:-D:/data/MUR-JPL-L4-GLOB-v4.1}

# ---- podaac CLI 路径 ----
PODAAC="$HOME/AppData/Roaming/Python/Python312/Scripts/podaac-data-downloader"

if [ ! -f "$PODAAC" ]; then
    echo "ERROR: podaac-data-downloader not found at $PODAAC"
    echo "Install: pip install podaac-data-submitter"
    exit 1
fi

# ---- 下载 ----
echo "=== MUR SST Download ==="
echo "  Date:  ${START} to ${END}"
echo "  BBox:  [${WLON}-${ELON}E, ${SLAT}-${NLAT}N]"
echo "  Dest:  ${OUTDIR}"
echo ""

mkdir -p "$OUTDIR"

"$PODAAC" \
    -c MUR-JPL-L4-GLOB-v4.1 \
    -d "$OUTDIR" \
    -sd "${START}T00:00:00Z" \
    -ed "${END}T00:00:00Z" \
    -b="${WLON},${SLAT},${ELON},${NLAT}" \
    --subset

echo ""
echo "=== Done ==="
echo "Files: $(ls "$OUTDIR"/*.nc4 2>/dev/null | wc -l)"
du -sh "$OUTDIR"
