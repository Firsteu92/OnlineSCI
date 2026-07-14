# OnlineSCI v1 实施说明

- 文档状态：已确认设计的实施基线
- 版本：v1.0-draft
- 日期：2026-07-14
- 适用对象：维护者、Claude Code、Codex、Cursor 等可编辑本地仓库的 Agent
- 实施原则：先在本地分支修改、检查 Diff，再由用户决定是否提交和推送

---

## 1. 本次改造的最终定位

OnlineSCI v1 不是一个必须安装或自动运行的 Agent 程序，也不是单纯的论文写作规范。

它是一套可以从 GitHub 下载和使用的：

1. 标准化 AI 科研工作流；
2. 可复制的 AI Flow 提示词；
3. Agent 任务规范（Skills）；
4. S0–S8 科研阶段指南；
5. G0–G5 质量门槛；
6. 人工审查清单；
7. P01–P10 空白项目模板；
8. GitHub 科研协作和归档规范。

普通用户的主要使用方式：

```text
下载或克隆 OnlineSCI
→ 选择 P01–P10 中一个空白项目
→ 在 AI_WORKFLOW_GUIDE.md 中判断当前阶段
→ 复制对应 Prompt
→ 在 ChatGPT、Claude、Codex、Cursor 等 Agent 中执行
→ 人工检查 Agent 输出
→ 按 G0–G5 判断是否允许进入下一阶段
→ 将结果保存到规定项目目录
→ 有协作需求时提交到 GitHub
```

GitHub 主要承担发布、版本控制、审查、协作和归档，不是默认的 AI 聊天界面。

---

## 2. 本次实施范围

### 必须完成

- 重写根 README 和用户工作流指南；
- 建立 S0–S8 阶段体系；
- 建立 G0–G5 门槛；
- 建立 12 个核心 Skills；
- 建立可直接复制的 Prompt 文件；
- 建立人工检查清单；
- 统一 P01–P10 空白项目结构；
- 更新 GitHub 协作文档和模板；
- 将项目许可证方向调整为 CC BY-NC-SA 4.0；
- 删除所有指向旧 OpenSCI-Ocean 仓库的链接、徽章、克隆命令和文字；
- 增加 Claude Code 仓库级操作说明。

### 本次不做

- 不开发自动 Router 程序；
- 不开发网页界面；
- 不开发数据库；
- 不预填 P01–P10 的研究主题或真实项目内容；
- 不建立具体学科领域包；
- 不加入复杂 CI、自动引用核验或自动审稿程序；
- 不自动提交或推送 GitHub；
- 不修改用户真实科研数据；
- 不把大型数据文件提交到仓库。

---

## 3. 许可证实施要求

### 3.1 项目许可证

根目录 `LICENSE` 调整为：

```text
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
CC BY-NC-SA 4.0
```

适用于 OnlineSCI v1 的文档、工作流、Skills、Prompt、模板和检查清单。

### 3.2 程序代码

当前 v1 以文档和模板为主，可暂时统一使用 CC BY-NC-SA 4.0。

将来如果增加大量 Python、MATLAB、Shell 或其他程序代码，再另行决定是否对代码使用 MIT 或 Apache-2.0，并在 `LICENSES.md` 中说明。

### 3.3 第三方内容

新增：

```text
NOTICE.md
LICENSES.md
THIRD_PARTY_NOTICES.md
```

要求：

- 在 `NOTICE.md` 中致谢 Supervisor-Skills 对工作流设计的启发；
- 不直接复制无法确认授权范围的外部文字；
- 如保留现有仓库中任何实质性的 MIT 来源内容，在 `THIRD_PARTY_NOTICES.md` 中保留相应原版权与许可声明；
- 不在任何文件中链接或指向旧 OpenSCI-Ocean 仓库；
- 不删除依法必须保留的第三方版权声明；
- 本文件不是法律意见，公开发布前由项目负责人最终确认许可状态。

---

## 4. 最终目录结构

按以下结构实施：

```text
OnlineSCI/
├── README.md
├── AI_WORKFLOW_GUIDE.md
├── SKILL_INDEX.md
├── SYSTEM.md
├── CLAUDE.md
├── LICENSE
├── LICENSES.md
├── NOTICE.md
├── THIRD_PARTY_NOTICES.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── COLLABORATION.md
├── CONTRIBUTORS.md
├── REVIEW_CHECKLIST.md
├── .gitignore
│
├── docs/
│   ├── QUICK_START.md
│   ├── STAGE_GATES.md
│   ├── GITHUB_COLLABORATION.md
│   ├── AI_USAGE_AND_LOGGING.md
│   └── DATA_MANAGEMENT.md
│
├── prompts/
│   ├── README.md
│   ├── S0_project_setup.md
│   ├── S1_deep_research.md
│   ├── S1_idea_evaluation.md
│   ├── S2_protocol_freeze.md
│   ├── S3_build_and_explore.md
│   ├── S4_formal_experiments.md
│   ├── S5_validation_and_evidence.md
│   ├── S6_paper_logic.md
│   ├── S6_scientific_figures.md
│   ├── S7_paper_writing.md
│   ├── S7_paper_polish.md
│   ├── S7_internal_review.md
│   └── S8_submission_and_archive.md
│
├── skills/
│   ├── README.md
│   ├── project-context/
│   │   └── SKILL.md
│   ├── deep-research/
│   │   └── SKILL.md
│   ├── idea-evaluator/
│   │   └── SKILL.md
│   ├── protocol-freezer/
│   │   └── SKILL.md
│   ├── experiment-auditor/
│   │   └── SKILL.md
│   ├── evidence-ledger/
│   │   └── SKILL.md
│   ├── paper-logic-builder/
│   │   └── SKILL.md
│   ├── scientific-figure-designer/
│   │   └── SKILL.md
│   ├── paper-writer/
│   │   └── SKILL.md
│   ├── paper-polish/
│   │   └── SKILL.md
│   ├── pre-submission-reviewer/
│   │   └── SKILL.md
│   ├── project-handoff/
│   │   └── SKILL.md
│   └── extensions/
│       ├── benchmark-paper/
│       │   └── README.md
│       └── drawio-reconstruction/
│           └── README.md
│
├── checklists/
│   ├── README.md
│   ├── G0_project_card.md
│   ├── G1_literature_and_innovation.md
│   ├── G2_protocol_freeze.md
│   ├── G3_experiment_and_validation.md
│   ├── G4_evidence_ledger.md
│   └── G5_pre_submission.md
│
├── templates/
│   ├── project.yml
│   ├── PROJECT.md
│   ├── STATUS.md
│   ├── decision_record.md
│   ├── literature_review.md
│   ├── reference_ledger.csv
│   ├── protocol.md
│   ├── protocol.yml
│   ├── run_manifest.yml
│   ├── claim_evidence_matrix.csv
│   ├── ai_interaction_log.md
│   └── HANDOFF.md
│
├── projects/
│   ├── DASHBOARD.md
│   ├── _template/
│   ├── p01/
│   ├── p02/
│   ├── p03/
│   ├── p04/
│   ├── p05/
│   ├── p06/
│   ├── p07/
│   ├── p08/
│   ├── p09/
│   └── p10/
│
├── shared/
│   ├── README.md
│   ├── resources.md
│   └── environment.example.yml
│
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── new_project_idea.md
    │   ├── review_request.md
    │   └── stage_discussion.md
    ├── PULL_REQUEST_TEMPLATE.md
    └── labels.yml
```

说明：

- 不增加自动 Router 代码；
- `SKILL_INDEX.md` 只负责帮助用户找到对应 Skill 和 Prompt；
- `skills/` 是完整任务规范；
- `prompts/` 是普通用户可直接复制的版本；
- `checklists/` 是人工门槛检查；
- `projects/` 保存实际科研过程。

---

## 5. S0–S8 工作流

### S0：项目建立 / Project Setup

目标：

- 将模糊想法建立为可管理项目；
- 选择 P01–P10 中的空白项目位；
- 填写项目卡、资源、限制和预期产出。

使用 Skill：

```text
project-context
```

主要产出：

```text
PROJECT.md
STATUS.md
project.yml
```

对应门槛：

```text
G0：没有建立项目卡，不进入正式科研流程。
```

---

### S1：文献与选题核验 / Evidence and Idea Evaluation

目标：

- 检索并核验真实文献；
- 找出最接近的已有工作；
- 判断研究空白、科学意义、创新性和可行性。

使用 Skills：

```text
deep-research
→ idea-evaluator
```

主要产出：

```text
literature/literature_review.md
literature/reference_ledger.csv
literature/closest_prior_work.md
idea/idea_evaluation.md
idea/risk_register.md
idea/decision.md
```

对应门槛：

```text
G1：没有完成真实、可核验的文献检索，不确认研究创新性。
```

---

### S2：实验协议冻结 / Protocol Freeze

目标：

- 在正式实验前冻结假设、数据范围、划分、基线、指标和验证方案。

使用 Skill：

```text
protocol-freezer
```

主要产出：

```text
protocols/protocol_v001.md
protocols/protocol_v001.yml
protocols/CHANGELOG.md
```

对应门槛：

```text
G2：没有冻结实验协议，产生的结果只能视为探索性结果，不能认定为正式实验结果。
```

---

### S3：数据准备与探索实现 / Build and Explore

目标：

- 整理数据；
- 跑通预处理和基础代码；
- 复现基线；
- 完成探索性分析；
- 为正式实验做好准备。

主要使用：

- Agent 编程、调试和数据分析能力；
- `experiment-auditor` 的运行前检查规则。

阶段产出：

```text
data/data_manifest.yml
data/README.md
code/
analysis/
runs/exploratory/
```

本阶段所有实验必须标记为：

```text
exploratory
```

---

### S4：正式实验 / Formal Experiments

目标：

- 严格按照冻结协议执行正式实验；
- 保留数据、代码、参数、环境、日志和结果记录；
- 检查协议偏差、泄漏和可复现性。

使用 Skill：

```text
experiment-auditor
```

运行状态只能使用：

```text
exploratory
formal_valid
formal_invalid
superseded
reproduction_failed
```

主要产出：

```text
runs/RUN_INDEX.csv
runs/<RUN-ID>/manifest.yml
runs/<RUN-ID>/command.txt
runs/<RUN-ID>/environment.yml
runs/<RUN-ID>/metrics.json
runs/<RUN-ID>/audit.md
runs/<RUN-ID>/outputs/
```

---

### S5：验证与证据整理 / Validation and Evidence

目标：

- 进行重复、独立、跨数据或跨场景验证；
- 分析失败和冲突结果；
- 建立论文声明与文献、运行记录、图表和数据之间的证据链。

使用 Skills：

```text
experiment-auditor
→ evidence-ledger
```

主要产出：

```text
evidence/claims.csv
evidence/claim_evidence_matrix.csv
evidence/evidence_ledger.md
evidence/unsupported_claims.md
evidence/conflicts.md
```

对应门槛：

```text
G3：没有完整运行记录和有效验证，不生成带有确定性结论的完整论文。

G4：没有建立证据账本，不形成或发布最终研究结论。
```

---

### S6：论文逻辑与图件规划 / Paper Story and Figures

目标：

- 建立论文主线、贡献、章节和段落结构；
- 为每个论点分配证据；
- 规划核心图件和面板逻辑。

使用 Skills：

```text
paper-logic-builder
→ scientific-figure-designer
```

主要产出：

```text
manuscript/planning/paper_story.md
manuscript/planning/detailed_outline.md
manuscript/planning/contribution_plan.md
manuscript/planning/section_evidence_map.csv
figures/figure_plan.md
figures/figure_checklist.md
```

---

### S7：论文写作与内部修改 / Writing and Internal Review

目标：

- 根据已核验的结构、图件和证据撰写正文；
- 润色语言；
- 进行内部审查；
- 将问题返回正确阶段处理。

使用 Skills：

```text
paper-writer
→ paper-polish
→ pre-submission-reviewer
```

写作权限：

- G3 未通过：只能写背景、文献、数据方法、实验计划和待验证提纲；
- G3 通过、G4 未通过：可写 Results 和 Discussion 草稿，但不得定稿最终 Abstract、Conclusions 和贡献声明；
- G3、G4 均通过：可以生成完整论文，但所有表述必须遵守证据账本。

---

### S8：投稿准备与项目归档 / Submission and Archive

目标：

- 完成投稿前检查；
- 准备投稿材料；
- 保存投稿版本和返修记录；
- 生成项目交接档案。

使用 Skills：

```text
pre-submission-reviewer
→ project-handoff
```

主要产出：

```text
manuscript/submission/
handoff/HANDOFF.md
handoff/FILE_INDEX.md
handoff/OPEN_ISSUES.md
handoff/environment.yml
```

对应门槛：

```text
G5：没有通过投稿前审查，不将项目标记为“可投稿”。
```

---

## 6. G0–G5 门槛正式文本

| 门槛 | 正式规则 |
|---|---|
| G0：项目建立门槛 | 没有建立项目卡，不进入正式科研流程。 |
| G1：创新判断门槛 | 没有完成真实、可核验的文献检索，不确认研究创新性。 |
| G2：正式实验门槛 | 没有冻结实验协议，产生的结果只能视为探索性结果，不能认定为正式实验结果。 |
| G3：结论写作门槛 | 没有完整运行记录和有效验证，不生成带有确定性结论的完整论文。 |
| G4：证据确认门槛 | 没有建立证据账本，不形成或发布最终研究结论。 |
| G5：投稿状态门槛 | 没有通过投稿前审查，不将项目标记为“可投稿”。 |

门槛关系：

```text
G0 建立项目
→ G1 核验创新
→ G2 冻结实验方案
→ G3 完成正式实验与有效验证
→ G4 建立结论证据链
→ G5 完成投稿前审查
```

---

## 7. 12 个核心 Skills

### 7.1 `project-context`

负责：

- 建立和读取项目卡；
- 汇总当前状态；
- 维护项目阶段、关键决定和下一步；
- 为其他 Skills 提供上下文。

不负责：

- 文献综述；
- 创新判断；
- 正式实验；
- 完整论文写作。

---

### 7.2 `deep-research`

负责：

- 真实文献检索；
- 文献核验；
- 研究现状、共识、争议和最接近工作分析；
- 区分已确认空白和待核验空白。

禁止：

- 编造论文、作者、DOI 和结论；
- 将“没搜到”直接认定为“首次”。

---

### 7.3 `idea-evaluator`

负责：

- 基于已核验文献评价新颖性、科学意义、可验证性、可行性和发表潜力；
- 检查致命缺陷；
- 给出 `PROCEED`、`PROCEED_WITH_CHANGES`、`HOLD` 或 `STOP`。

没有通过 G1 时，不得确认创新。

---

### 7.4 `protocol-freezer`

负责：

- 冻结研究假设；
- 数据范围和划分；
- 基线；
- 主指标和次指标；
- 主实验、消融、鲁棒性和独立验证；
- 失败标准；
- 允许和禁止的协议变更。

协议修改必须创建新版本，不覆盖旧版本。

---

### 7.5 `experiment-auditor`

负责：

- 正式运行前检查；
- Run Manifest；
- 运行后审计；
- 协议符合性；
- 数据、时间、空间、标签和未来信息泄漏检查；
- 可复现性检查；
- 判定运行状态。

禁止删除失败实验或只保留最佳结果。

---

### 7.6 `evidence-ledger`

负责：

- 建立声明—文献—实验—图表—数据之间的映射；
- 判定 `supported`、`partially_supported`、`conflicting`、`unsupported`、`pending`、`rejected`；
- 控制允许使用的结论强度；
- 记录无证据和冲突声明。

---

### 7.7 `paper-logic-builder`

负责：

- 论文主线；
- 章节级和段落级详细提纲；
- 贡献安排；
- 论点、证据、引用和图件分配。

不直接撰写完整正文。

---

### 7.8 `scientific-figure-designer`

负责：

- 核心图件规划；
- 面板结构；
- 变量、单位、坐标、图例和图注；
- 视觉层级、期刊尺寸和分辨率；
- 图件是否准确表达证据。

不得为了美观隐藏不利结果。

---

### 7.9 `paper-writer`

负责：

- 根据已批准结构和证据撰写论文各部分；
- Introduction Drafter 合并为 `mode: introduction`；
- 严格遵守 G3、G4 写作权限。

禁止创造数据、文献、实验和结论。

---

### 7.10 `paper-polish`

负责：

- 语法；
- 清晰度；
- 术语；
- 衔接；
- 期刊风格；
- 减少 AI 腔。

不得改变科学含义、增加结果或补造引用。

---

### 7.11 `pre-submission-reviewer`

负责：

- 科学性、证据、结构、语言、图表、格式和投稿材料审查；
- 按 `CRITICAL`、`MAJOR`、`MINOR` 分级；
- 为每个问题标注应返回的 Skill。

典型回退：

```text
语言问题 → paper-polish
结构问题 → paper-logic-builder
图件问题 → scientific-figure-designer
无证据结论 → evidence-ledger
实验不足 → experiment-auditor
协议问题 → protocol-freezer
文献与创新问题 → deep-research / idea-evaluator
```

---

### 7.12 `project-handoff`

负责：

- 当前进度；
- 关键文件；
- 环境和运行方式；
- 有效和失败结果；
- 已排除路线；
- 关键决定；
- 未解决问题；
- 下一步；
- 禁止误改内容。

---

## 8. 每个 `SKILL.md` 的统一结构

每个核心 Skill 必须按以下标题编写：

```markdown
# Skill: <name>

## Purpose
## When to Use
## Required Inputs
## Optional Inputs
## Preconditions and Gate Checks
## Mandatory Procedure
## Prohibited Actions
## Required Outputs
## Human Review
## Completion Criteria
## Failure and Fallback
## Related Prompts
## Related Templates
```

要求：

- 不能只写一个长 Prompt；
- 必须规定输入、步骤、禁止事项、产出和完成标准；
- 不复制外部 Skill 的长段原文；
- 可以在许可允许范围内参考其结构和思想；
- 使用清晰、可执行的中文说明，必要时保留英文术语。

---

## 9. Prompt 文件统一结构

每个 `prompts/*.md` 必须包含：

```markdown
# <阶段与任务名称>

## 什么时候使用
## 使用前需要准备
## 可直接复制的 Prompt
## 期望输出
## 人类审查重点
## 保存位置
## 下一门槛
```

“可直接复制的 Prompt”必须：

- 使用可填写占位符；
- 要求 Agent 不编造文献、数据或结果；
- 要求区分已确认事实和待核验内容；
- 要求输出结构化结果；
- 告知用户需要把输出保存到哪个目录；
- 不依赖某一特定 Agent 品牌。

---

## 10. P01–P10 空白项目模板

### 10.1 统一结构

`projects/_template/` 和 `projects/p01` 至 `projects/p10` 使用完全一致的结构：

```text
project.yml
PROJECT.md
STATUS.md
idea/
literature/
protocols/
data/
code/
analysis/
runs/
results/
evidence/
figures/
manuscript/
logs/
handoff/
```

Git 无法保存空目录时，可使用 `.gitkeep`。

### 10.2 不允许预填

P01–P10 中不得写入：

- 具体科研主题；
- 用户个人研究方向；
- 真实数据路径；
- 真实作者姓名；
- 真实实验结果；
- 目标期刊；
- 任何默认项目名称。

只允许保留：

- 空字段；
- 填写说明；
- 通用目录说明；
- 模板链接。

### 10.3 `project.yml`

最低字段：

```yaml
project_id: P01
title: ""
status: blank
stage: S0
owner: ""
created_at: ""
updated_at: ""

research_question: ""
project_type: ""
domain: ""

gates:
  G0: not_checked
  G1: not_checked
  G2: not_checked
  G3: not_checked
  G4: not_checked
  G5: not_checked

data_status: not_defined
code_status: not_defined
protocol_status: not_created
evidence_status: not_created
manuscript_status: not_started
```

P02–P10 仅修改 `project_id`。

### 10.4 大型数据

`data/` 默认不保存大型原始数据，只保存：

```text
README.md
data_manifest.yml
checksums/
samples/
```

真实大数据可存储在本地、服务器或合规云存储中。路径、版本、来源和校验信息写入 Manifest。

---

## 11. 用户工作流指南的呈现形式

`AI_WORKFLOW_GUIDE.md` 继续沿用原项目易读的说明方式。

每个 S 阶段必须包含：

1. 阶段目标；
2. 适用场景；
3. AI 任务清单；
4. 对应 Skills；
5. 推荐 Prompt 链接；
6. 人类审查重点；
7. 产出文件；
8. 进入下一阶段的门槛；
9. 常见错误；
10. 示例使用过程。

这份文件面向普通用户，不能写成内部系统设计文档。

---

## 12. `SKILL_INDEX.md`

此文件替代自动 Router，提供人工任务导航。

建议表格：

| 用户想做什么 | 当前阶段 | 使用 Prompt | 对应 Skill | 门槛 |
|---|---|---|---|---|
| 建立新项目 | S0 | `S0_project_setup.md` | `project-context` | G0 |
| 查文献 | S1 | `S1_deep_research.md` | `deep-research` | G1 |
| 判断创新性 | S1 | `S1_idea_evaluation.md` | `idea-evaluator` | G1 |
| 冻结实验方案 | S2 | `S2_protocol_freeze.md` | `protocol-freezer` | G2 |
| 跑探索流程 | S3 | `S3_build_and_explore.md` | 通用 Agent 能力 | — |
| 跑正式实验 | S4 | `S4_formal_experiments.md` | `experiment-auditor` | G2/G3 |
| 判断结论能否写 | S5 | `S5_validation_and_evidence.md` | `evidence-ledger` | G4 |
| 搭论文结构 | S6 | `S6_paper_logic.md` | `paper-logic-builder` | G3/G4 |
| 设计科研图件 | S6 | `S6_scientific_figures.md` | `scientific-figure-designer` | G3/G4 |
| 写论文 | S7 | `S7_paper_writing.md` | `paper-writer` | 按 G3/G4 分级 |
| 润色论文 | S7 | `S7_paper_polish.md` | `paper-polish` | — |
| 内部审查 | S7 | `S7_internal_review.md` | `pre-submission-reviewer` | — |
| 投稿与交接 | S8 | `S8_submission_and_archive.md` | `project-handoff` | G5 |

---

## 13. GitHub 协作规则

### GitHub 的角色

- 发布 OnlineSCI；
- 保存项目结构和轻量产出；
- 记录修改历史；
- 通过 Issue 讨论科学问题；
- 通过 Pull Request 进行审查；
- 多人协作；
- 归档投稿版本和返修过程。

### 不应提交

- 密钥、Token、密码；
- 涉密或受限数据；
- 未匿名化个人数据；
- 大型原始数据；
- 违反许可的数据；
- Agent 私密凭证；
- 未确认可公开的论文稿件。

### PR 模板必须检查

- 当前项目和阶段；
- 涉及的 G 门槛；
- 是否增加或修改结论；
- 是否附有实验运行记录；
- 是否更新证据账本；
- 是否包含 AI 生成内容；
- 是否完成人工审查；
- 是否提交了大文件或敏感信息。

---

## 14. 现有文件的处理规则

### 重写

以下文件需要按新定位重写：

```text
README.md
COLLABORATION.md
CONTRIBUTING.md
REVIEW_CHECKLIST.md
projects/DASHBOARD.md
projects/PROJECT_TEMPLATE.md
shared/ai_workflow.md
shared/data_sources.md
shared/environment.yml
.github/PULL_REQUEST_TEMPLATE.md
.github/ISSUE_TEMPLATE/*.md
```

### 检查后保留或轻改

```text
CODE_OF_CONDUCT.md
CONTRIBUTORS.md
.github/labels.yml
.gitignore
```

### 删除或迁移

- 将 `shared/ai_workflow.md` 的有效思想迁移到根目录 `AI_WORKFLOW_GUIDE.md`；
- 将 `projects/PROJECT_TEMPLATE.md` 的有效内容迁移到 `projects/_template/` 和 `templates/`；
- 删除旧文件前，确认新文件已覆盖其必要功能；
- 清理 p02–p04 中与其他项目不一致的多余空目录；
- 统一所有 P 项目结构。

---

## 15. 旧仓库引用清理

完成后执行全文检查：

```bash
rg -n -i "OpenSCI-Ocean|opensci-ocean|old repository|旧仓库" .
```

要求：

- README 不包含旧仓库徽章；
- 不包含旧仓库 URL；
- 不包含旧仓库克隆命令；
- Issue、PR、贡献和协作文档不指向旧仓库；
- 所有内部链接改为 OnlineSCI 当前相对路径；
- Git 历史本次不重写，除非用户另行明确要求。

---

## 16. `CLAUDE.md` 必须包含的仓库规则

`CLAUDE.md` 面向 Claude Code，至少写入：

1. 先读取本实施说明和相关文件；
2. 默认先 Plan，后修改；
3. 未经用户明确授权，不执行 `git commit`、`git push`、创建 PR 或合并；
4. 不直接修改 `main`；
5. P01–P10 必须保持空白；
6. 不写入用户个人真实研究内容；
7. 不引用旧 OpenSCI-Ocean 仓库；
8. 不编造文献、数据、实验和结果；
9. 不删除第三方许可声明；
10. 不提交大文件、密钥和隐私数据；
11. 修改后执行链接、目录、阶段和命名一致性检查；
12. 所有阶段名称统一为 S0–S8；
13. 所有门槛统一为 G0–G5；
14. 不实现自动 Router；
15. 不添加本说明未要求的复杂功能。

---

## 17. 验收标准

### 17.1 结构验收

- 根目录和主要目录均存在；
- 12 个核心 `SKILL.md` 均存在；
- 13 个用户 Prompt 均存在；
- 6 个 Gate Checklist 均存在；
- P01–P10 目录结构一致；
- P01–P10 没有真实项目内容。

### 17.2 内容验收

- README 能在 5 分钟内让新用户理解系统；
- QUICK_START 能让新用户完成第一个 S0 项目；
- AI_WORKFLOW_GUIDE 覆盖 S0–S8；
- STAGE_GATES 正确呈现 G0–G5；
- Skill、Prompt、Checklist 三者互相链接；
- 写作权限正确区分 G3/G4；
- GitHub 与 Agent 的职责没有混淆。

### 17.3 一致性验收

全文检查：

```bash
rg -n "D0|D1|D2|D3|D4" .
rg -n "S[0-8]" .
rg -n "G[0-5]" .
rg -n -i "OpenSCI-Ocean|opensci-ocean" .
```

要求：

- 旧 D0–D4 只允许在迁移说明中作为历史背景出现，正式工作流不得继续使用；
- S0–S8 名称一致；
- G0–G5 文本一致；
- 无旧仓库引用。

### 17.4 Git 验收

在推送前检查：

```bash
git status
git diff --stat
git diff
git ls-files | sort
```

并确认：

- 没有意外删除用户文件；
- 没有大文件；
- 没有凭证；
- 没有真实项目内容；
- 没有自动生成的缓存；
- 没有未经许可复制的大段外部文本。

---

## 18. Claude Code 推荐实施顺序

### Phase A：只规划

1. 读取本实施说明；
2. 检查当前仓库；
3. 列出新增、重写、迁移、删除和保留的文件；
4. 暂不修改。

### Phase B：建立骨架

1. 创建目录；
2. 创建空白模板；
3. 统一 P01–P10；
4. 建立索引和内部链接骨架。

### Phase C：编写内容

1. README、SYSTEM、QUICK_START；
2. AI_WORKFLOW_GUIDE；
3. STAGE_GATES；
4. Skills；
5. Prompts；
6. Checklists；
7. 协作与数据管理文档。

### Phase D：许可证和清理

1. 更新许可证文件；
2. 添加 NOTICE 和第三方说明；
3. 清理旧仓库引用；
4. 迁移或删除旧文件。

### Phase E：验证

1. 检查目录；
2. 检查 Markdown 链接；
3. 检查 S/G 编号；
4. 检查 P01–P10；
5. 输出完整 Diff 摘要；
6. 不提交、不推送，等待用户确认。

---

## 19. 不得擅自决定的事项

Claude Code 遇到以下内容不得自行扩大范围：

- 是否重写 Git 历史；
- 是否删除旧提交；
- 是否将代码单独改成 MIT 或 Apache-2.0；
- 是否添加自动 Router；
- 是否添加 CI；
- 是否预填任何真实项目；
- 是否创建正式 GitHub Release；
- 是否直接推送到 `main`；
- 是否公开仓库。

---

## 20. 完成定义

当以下条件全部满足时，本次实施才算完成：

```text
用户可以从 GitHub 下载 OnlineSCI
→ 阅读 QUICK_START 和 AI_WORKFLOW_GUIDE
→ 选择空白 P01–P10
→ 按 S0–S8 找到当前阶段
→ 复制对应 Prompt 到任意 Agent
→ 按 Skill 规范获得结构化输出
→ 按 G0–G5 和 Checklist 人工核验
→ 将产出保存到统一目录
→ 需要协作时通过 GitHub Issue、PR 和版本记录开展科研交流
```

这就是 OnlineSCI v1 的目标，不要求自动化 Agent 程序。
