# OnlineSCI

**标准化 AI 辅助科研工作流工具包**

一套从 GitHub 下载即可使用的开源科研工作流框架。提供标准化阶段（S0–S8）、质量门槛（G0–G5）、可复制的 Prompt 模板、Agent Skills 规范和空白项目模板，帮助研究者在任意 AI Agent（ChatGPT、Claude、Codex、Cursor 等）中执行结构化科研任务。

---

## 核心概念

| 概念 | 说明 |
|------|------|
| **S0–S8** | 科研全生命周期标准阶段：从项目建立到投稿归档 |
| **G0–G5** | 六道质量门槛：每阶段产出必须通过对应门槛才能进入下一阶段 |
| **Skills** | 12 个标准 Agent 任务规范：规定输入、步骤、禁止事项和产出 |
| **Prompts** | 可直接复制使用的 Agent 提示词，每阶段对应 1–2 个 |
| **Checklists** | 人工审查清单：确保 Agent 输出经人类核验 |
| **P01–P10** | 十个空白项目位：结构一致，可同时推进多个研究方向 |

## 快速开始

```text
1. 下载或克隆本仓库
2. 阅读 QUICK_START → 选择空白 P01–P10
3. 在 AI_WORKFLOW_GUIDE 中判断当前阶段
4. 复制对应 Prompt 到任意 Agent 执行
5. 按 G0–G5 和 Checklist 人工核验 Agent 输出
6. 将结果保存到规定项目目录
7. 有协作需求时通过 GitHub Issue/PR 开展交流
```

详见 [docs/QUICK_START.md](docs/QUICK_START.md)。

## 仓库结构

```
OnlineSCI/
├── README.md                 # 本文件
├── AI_WORKFLOW_GUIDE.md      # S0–S8 用户工作流指南
├── SKILL_INDEX.md            # 任务导航表
├── SYSTEM.md                 # 系统概述
├── CLAUDE.md                 # Claude Code 操作规则
├── LICENSE                   # CC BY-NC-SA 4.0
├── LICENSES.md               # 许可证说明
├── NOTICE.md                 # 致谢
├── THIRD_PARTY_NOTICES.md    # 第三方版权声明
├── CODE_OF_CONDUCT.md        # 行为准则
├── CONTRIBUTING.md           # 参与指南
├── COLLABORATION.md          # 协作制度
├── CONTRIBUTORS.md           # 贡献者记录
├── REVIEW_CHECKLIST.md       # 审查清单
│
├── docs/                     # 文档
├── prompts/                  # 用户可直接复制的 Prompt
├── skills/                   # Agent 任务规范（SKILL.md）
├── checklists/               # G0–G5 人工审查清单
├── templates/                # 项目模板文件
├── projects/                 # 实际科研项目（P01–P10）
│   ├── DASHBOARD.md          # 项目总览看板
│   ├── _template/            # 空白项目模板
│   └── p01/ … p10/           # 十个空白项目位
└── shared/                   # 共享资源
```

## 文档索引

| 文档 | 用途 | 适合读者 |
|------|------|----------|
| [QUICK_START](docs/QUICK_START.md) | 5 分钟掌握系统使用 | 新用户 |
| [AI_WORKFLOW_GUIDE](AI_WORKFLOW_GUIDE.md) | S0–S8 完整工作流指南 | 所有用户 |
| [SKILL_INDEX](SKILL_INDEX.md) | 根据任务查找对应 Skill 和 Prompt | 所有用户 |
| [STAGE_GATES](docs/STAGE_GATES.md) | G0–G5 门槛正式文本 | 所有用户 |
| [SYSTEM](SYSTEM.md) | 系统设计说明 | 维护者 |
| [COLLABORATION](COLLABORATION.md) | 署名、分工、协作规则 | 协作者 |
| [CONTRIBUTING](CONTRIBUTING.md) | Fork、分支、PR 规范 | 协作者 |
| [GITHUB_COLLABORATION](docs/GITHUB_COLLABORATION.md) | GitHub 使用规范 | 协作者 |
| [AI_USAGE_AND_LOGGING](docs/AI_USAGE_AND_LOGGING.md) | AI 披露和日志规范 | 所有用户 |
| [DATA_MANAGEMENT](docs/DATA_MANAGEMENT.md) | 数据管理政策 | 所有用户 |
| [REVIEW_CHECKLIST](REVIEW_CHECKLIST.md) | 人工审查检查清单 | 审查者 |

## 许可

OnlineSCI v1 文档、工作流、Skills、Prompt、模板和检查清单采用 **CC BY-NC-SA 4.0** 许可。详见 [LICENSE](LICENSE) 和 [LICENSES.md](LICENSES.md)。

本项目包含源自 OpenSCI-Ocean（Pangeo 社区）的代码，按 MIT License 使用。详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
