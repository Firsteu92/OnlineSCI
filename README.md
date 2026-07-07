# OnlineSCI

**AI-assisted open research framework for physical oceanography and ocean remote sensing.**

多研究方向并行推进的开放科学研究框架。AI 辅助文献调研、数据分析、图表生成和论文撰写，人类科学家负责物理把关和审核纠偏。研究过程全程公开。

---

## Overview / 概述

OnlineSCI 是一个面向物理海洋学和海洋遥感的开放研究框架。每个方向在独立目录下自包含运行，包含完整的文献调研、分析脚本、图表、论文手稿和 AI 交互日志。框架设计为可复制、可扩展的研究结构，适用于并行推进多个课题。

## Projects / 研究方向

当前框架预留了多个研究方向位（P01-P10），每个方向在 [projects/](projects/) 下独立管理。

- [项目总览](projects/DASHBOARD.md) — 框架结构和启用手册
- [项目模板](projects/PROJECT_TEMPLATE.md) — 新项目初始化模板

每个研究方向目录自包含以下结构：

```
pXX/
├── README.md          # 项目信息卡片：科学问题、状态、数据链接
├── literature/        # AI 文献调研笔记
├── analysis/          # 分析脚本
├── figures/           # 图表文件
├── manuscript/        # 论文手稿全版本管理
│   ├── v1_ai_draft/  # AI 生成初稿
│   ├── v2_delivery/  # 人类审查交付稿
│   ├── v3_final/     # 内部评审定稿
│   └── submitted/    # 投稿版本
└── logs/             # AI 交互日志
```

## Repository Structure / 仓库结构

```
OnlineSCI/
├── README.md                 # 本文件
├── COLLABORATION.md          # 协作规则、署名、工作流
├── CONTRIBUTORS.md           # 贡献者追踪
├── LICENSE                   # MIT
├── projects/
│   ├── DASHBOARD.md          # 框架结构总览
│   ├── PROJECT_TEMPLATE.md   # 新项目模板
│   ├── p01/ ... p10/         # 各研究方向（独立自包含）
├── shared/                   # 共享工具和配置
│   ├── ai_workflow.md        # AI Prompt 模板
│   ├── data_sources.md       # 公开数据源目录
│   └── environment.yml       # Conda 环境配置
└── docs/                     # 通用文档
```

## Rules & Documentation / 规范文档

| 文档 | 用途 |
|------|------|
| [COLLABORATION.md](COLLABORATION.md) | 署名、角色分工、工作流、数据策略 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Fork、分支、PR 规范 |
| [REVIEW_CHECKLIST.md](REVIEW_CHECKLIST.md) | 审查检查清单 |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | 行为准则 |
| [CONTRIBUTORS.md](CONTRIBUTORS.md) | 贡献者追踪板 |
| [shared/ai_workflow.md](shared/ai_workflow.md) | 各阶段 AI Prompt 模板 |
| [shared/data_sources.md](shared/data_sources.md) | 公开数据源目录 |
| [shared/environment.yml](shared/environment.yml) | Conda 环境配置 |

### 基本原则

- 每个方向独立署名，遵循 [CRediT](https://credit.niso.org/) 分类体系
- AI 使用在每个手稿中完全披露
- 零容忍虚假引用
- 仓库不存储原始数据，仅保留数据链接和脚本
- 计算在本地或租赁服务器完成

## License / 许可

MIT License. See [LICENSE](LICENSE).

---

*Framework adapted from [OpenSCI-Ocean](https://github.com/pangeo-data/OpenSCI-Ocean) (Pangeo community, MIT License).*
