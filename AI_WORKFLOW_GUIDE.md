# AI Workflow Guide — AI 工作流指南

本文档定义 OnlineSCI 的 S0–S8 标准科研工作流。每个阶段包含目标、任务、Skills、Prompt 链接、审查重点、产出、门槛和常见错误。

---

## S0：项目建立 / Project Setup

### 阶段目标
将模糊想法建立为可管理的项目：选择空白项目位、填写项目卡、确定资源限制和预期产出。

### 适用场景
- 开始一个全新的研究方向
- 需要一个正式的项目结构来组织工作

### AI 任务清单
1. 选择 P01–P10 中的空白项目位
2. 定义核心研究问题
3. 填写项目卡（PROJECT.md）
4. 初始化项目状态（STATUS.md, project.yml）
5. 列出已知资源、限制和预期产出

### 对应 Skills
- [project-context](../skills/project-context/SKILL.md)

### 推荐 Prompt
- [S0_project_setup.md](../prompts/S0_project_setup.md)

### 人类审查重点
- [ ] 研究问题是否清晰、可检验
- [ ] 项目范围是否合理
- [ ] 资源需求是否现实

### 产出文件
- `projects/pXX/PROJECT.md`
- `projects/pXX/STATUS.md`
- `projects/pXX/project.yml`

### 下一门槛
**G0**：没有建立项目卡，不进入正式科研流程。

### 常见错误
- 在项目卡中写入过多未经核实的假设
- 跳过此步骤直接进入实验或写作

### 示例使用过程
1. 用户复制 `S0_project_setup.md` Prompt 到 Claude
2. Agent 引导用户填写研究问题、范围和预期产出
3. 用户根据输出填写 `PROJECT.md` 和 `project.yml`
4. 用户使用 `G0_project_card.md` 检查清单核验
5. G0 通过，进入 S1

---

## S1：文献与选题核验 / Evidence and Idea Evaluation

### 阶段目标
检索并核验真实文献，找出最接近的已有工作，判断研究空白、科学意义、创新性和可行性。

### 适用场景
- 需要确认研究想法是否新颖
- 需要了解领域研究现状
- 需要找最相关的对标工作

### AI 任务清单
1. 系统检索相关文献
2. 核验文献真实性（DOI、作者、期刊）
3. 分析研究现状、共识和争议
4. 判断研究空白（区分已确认和待核验）
5. 评估新颖性、科学意义、可验证性和可行性

### 对应 Skills
- [deep-research](../skills/deep-research/SKILL.md)
- [idea-evaluator](../skills/idea-evaluator/SKILL.md)

### 推荐 Prompt
- [S1_deep_research.md](../prompts/S1_deep_research.md)（先做文献检索）
- [S1_idea_evaluation.md](../prompts/S1_idea_evaluation.md)（再做创新判断）

### 人类审查重点
- [ ] 核验 AI 列出的每篇文献是否真实存在
- [ ] knowledge gap 是否真的存在（而非 AI 编造）
- [ ] 评估选题的科学意义

### 产出文件
- `literature/literature_review.md`
- `literature/reference_ledger.csv`
- `literature/closest_prior_work.md`
- `idea/idea_evaluation.md`
- `idea/risk_register.md`
- `idea/decision.md`

### 下一门槛
**G1**：没有完成真实、可核验的文献检索，不确认研究创新性。

### 常见错误
- 不核验 AI 生成的文献引用
- 将"没搜到"直接认定为"首次发现"
- 忽略最接近的已有工作

---

## S2：实验协议冻结 / Protocol Freeze

### 阶段目标
在正式实验前冻结假设、数据范围、基线、指标和验证方案，避免事后修改导致偏差。

### 适用场景
- 开始正式实验前
- 需要在团队中统一实验方案

### AI 任务清单
1. 明确研究假设
2. 确定数据范围和划分方式
3. 确定基线方法
4. 定义主指标和次指标
5. 规划主实验、消融、鲁棒性和独立验证
6. 设定失败标准和协议变更规则

### 对应 Skills
- [protocol-freezer](../skills/protocol-freezer/SKILL.md)

### 推荐 Prompt
- [S2_protocol_freeze.md](../prompts/S2_protocol_freeze.md)

### 人类审查重点
- [ ] 假设是否可检验
- [ ] 指标是否合理
- [ ] 失败标准是否明确

### 产出文件
- `protocols/protocol_v001.md`
- `protocols/protocol_v001.yml`
- `protocols/CHANGELOG.md`

### 下一门槛
**G2**：没有冻结实验协议，产生的结果只能视为探索性结果，不能认定为正式实验结果。

### 常见错误
- 协议写得过于笼统，无法据此判断实验是否合格
- 没有规定失败标准
- 修改协议后不创建新版本

---

## S3：数据准备与探索实现 / Build and Explore

### 阶段目标
整理数据、跑通预处理和基础代码、复现基线、完成探索性分析，为正式实验做好准备。

### 适用场景
- 需要准备数据和代码环境
- 需要进行探索性分析验证技术路线

### AI 任务清单
1. 整理数据目录和 Manifest
2. 编写数据预处理和加载代码
3. 复现公开基线方法
4. 完成探索性分析
5. 检查数据质量和潜在问题

### 对应 Skills
- 通用 Agent 编程能力
- 参考 [experiment-auditor](../skills/experiment-auditor/SKILL.md) 的运行前检查规则

### 推荐 Prompt
- [S3_build_and_explore.md](../prompts/S3_build_and_explore.md)

### 人类审查重点
- [ ] 数据处理流程是否正确
- [ ] 基线结果是否合理
- [ ] 探索性分析是否发现了需要关注的问题

### 产出文件
- `data/data_manifest.yml`
- `data/README.md`
- `code/`
- `analysis/`
- `runs/exploratory/`

本阶段所有实验运行状态必须标记为 `exploratory`。

### 下一门槛
G2（与 S2 共同为 S4 做准备）

### 常见错误
- 在本阶段就进行参数调优（应等到 S4）
- 不记录数据来源和版本
- 忽略数据质量问题

---

## S4：正式实验 / Formal Experiments

### 阶段目标
严格按照冻结协议执行正式实验，保留完整运行记录，检查协议偏差、泄漏和可复现性。

### 适用场景
- 协议已冻结
- 需要产生正式实验结果

### AI 任务清单
1. 按协议执行正式实验
2. 记录每次运行的完整参数和环境
3. 检查协议符合性
4. 检查泄漏（数据、时间、空间、标签、未来信息）
5. 检查可复现性
6. 判定运行状态

### 对应 Skills
- [experiment-auditor](../skills/experiment-auditor/SKILL.md)

### 推荐 Prompt
- [S4_formal_experiments.md](../prompts/S4_formal_experiments.md)

### 人类审查重点
- [ ] 实验是否严格遵循冻结协议
- [ ] 是否有未声明的参数修改
- [ ] 失败实验是否被排除或隐藏

### 运行状态
只能使用：`exploratory` / `formal_valid` / `formal_invalid` / `superseded` / `reproduction_failed`

### 产出文件
- `runs/RUN_INDEX.csv`
- `runs/<RUN-ID>/manifest.yml`
- `runs/<RUN-ID>/command.txt`
- `runs/<RUN-ID>/environment.yml`
- `runs/<RUN-ID>/metrics.json`
- `runs/<RUN-ID>/audit.md`
- `runs/<RUN-ID>/outputs/`

### 下一门槛
**G3**：没有完整运行记录和有效验证，不生成带有确定性结论的完整论文。

### 常见错误
- 只保留最佳结果，删除失败实验
- 不记录运行参数和环境
- 协议已修改但不更新版本

---

## S5：验证与证据整理 / Validation and Evidence

### 阶段目标
进行重复、独立、跨数据或跨场景验证，建立论文声明与文献、运行记录、图表和数据之间的证据链。

### 适用场景
- 正式实验已完成
- 需要判断哪些结论有充分证据支持

### AI 任务清单
1. 执行重复和独立验证
2. 分析失败和冲突结果
3. 建立声明-证据映射
4. 判定每项声明证据强度
5. 记录无证据和冲突声明

### 对应 Skills
- [experiment-auditor](../skills/experiment-auditor/SKILL.md)
- [evidence-ledger](../skills/evidence-ledger/SKILL.md)

### 推荐 Prompt
- [S5_validation_and_evidence.md](../prompts/S5_validation_and_evidence.md)

### 人类审查重点
- [ ] 证据是否真正支持声明
- [ ] 冲突结果是否被诚实地记录
- [ ] 结论强度是否与证据匹配

### 证据状态
`supported` / `partially_supported` / `conflicting` / `unsupported` / `pending` / `rejected`

### 产出文件
- `evidence/claims.csv`
- `evidence/claim_evidence_matrix.csv`
- `evidence/evidence_ledger.md`
- `evidence/unsupported_claims.md`
- `evidence/conflicts.md`

### 下一门槛
**G4**：没有建立证据账本，不形成或发布最终研究结论。

### 常见错误
- 忽略与结论矛盾的证据
- 将相关性直接认定为因果
- 夸大证据支持的结论强度

---

## S6：论文逻辑与图件规划 / Paper Story and Figures

### 阶段目标
建立论文主线、贡献、章节和段落结构，为每个论点分配证据，规划核心图件和面板逻辑。

### 适用场景
- 已有足够的实验证据
- 需要组织论文结构和图件

### AI 任务清单
1. 确定论文核心贡献
2. 构建章节级和段落级提纲
3. 为每个论点分配证据和引用
4. 规划核心图件和面板逻辑
5. 设计图件视觉层级

### 对应 Skills
- [paper-logic-builder](../skills/paper-logic-builder/SKILL.md)
- [scientific-figure-designer](../skills/scientific-figure-designer/SKILL.md)

### 推荐 Prompt
- [S6_paper_logic.md](../prompts/S6_paper_logic.md)
- [S6_scientific_figures.md](../prompts/S6_scientific_figures.md)

### 人类审查重点
- [ ] 论文故事线是否清晰有力
- [ ] 每个论点是否有足够的证据支持
- [ ] 图件是否准确表达证据

### 产出文件
- `manuscript/planning/paper_story.md`
- `manuscript/planning/detailed_outline.md`
- `manuscript/planning/contribution_plan.md`
- `manuscript/planning/section_evidence_map.csv`
- `figures/figure_plan.md`
- `figures/figure_checklist.md`

### 下一门槛
G3、G4 必须已通过。

### 常见错误
- 跳过提纲直接写正文
- 图件设计不合理，隐藏不利结果
- 论点与证据不匹配

---

## S7：论文写作与内部修改 / Writing and Internal Review

### 阶段目标
根据已核验的结构、图件和证据撰写正文，润色语言，进行内部审查，将问题返回正确阶段处理。

### 适用场景
- S6 已完成
- 需要撰写、润色和审查论文

### AI 任务清单
1. 根据提纲和证据撰写各部分正文
2. 润色语言（语法、清晰度、术语、衔接）
3. 进行内部审查
4. 将问题返回正确阶段

### 对应 Skills
- [paper-writer](../skills/paper-writer/SKILL.md)
- [paper-polish](../skills/paper-polish/SKILL.md)
- [pre-submission-reviewer](../skills/pre-submission-reviewer/SKILL.md)

### 推荐 Prompt
- [S7_paper_writing.md](../prompts/S7_paper_writing.md)
- [S7_paper_polish.md](../prompts/S7_paper_polish.md)
- [S7_internal_review.md](../prompts/S7_internal_review.md)

### 写作权限
- **G3 未通过**：只能写背景、文献、数据方法、实验计划和待验证提纲
- **G3 通过、G4 未通过**：可写 Results 和 Discussion 草稿，但不得定稿最终 Abstract、Conclusions 和贡献声明
- **G3、G4 均通过**：可以生成完整论文，但所有表述必须遵守证据账本

### 人类审查重点
- [ ] 论文是否准确反映证据
- [ ] 是否有过度推断
- [ ] 语言是否自然

### 产出文件
- `manuscript/v1_ai_draft/`
- `manuscript/v2_delivery/`
- `manuscript/v3_final/`

### 下一门槛
G5（完成后进入 S8）

### 常见错误
- 在 G3/G4 未通过时写出确定性结论
- 审查发现的问题不返回正确阶段处理
- AI 润色改变了科学含义

---

## S8：投稿准备与项目归档 / Submission and Archive

### 阶段目标
完成投稿前检查，准备投稿材料，保存投稿版本和返修记录，生成项目交接档案。

### 适用场景
- 论文已完成
- 需要准备投稿和归档

### AI 任务清单
1. 完成投稿前审查（科学性、证据、结构、语言、图表、格式）
2. 准备投稿材料（Cover Letter、Data Availability Statement、AI 声明）
3. 保存投稿版本
4. 准备项目交接文档

### 对应 Skills
- [pre-submission-reviewer](../skills/pre-submission-reviewer/SKILL.md)
- [project-handoff](../skills/project-handoff/SKILL.md)

### 推荐 Prompt
- [S8_submission_and_archive.md](../prompts/S8_submission_and_archive.md)

### 人类审查重点
- [ ] 投稿材料是否齐全
- [ ] AI 使用声明是否如实
- [ ] 项目交接文档是否完整

### 产出文件
- `manuscript/submission/`
- `handoff/HANDOFF.md`
- `handoff/FILE_INDEX.md`
- `handoff/OPEN_ISSUES.md`
- `handoff/environment.yml`

### 下一门槛
**G5**：没有通过投稿前审查，不将项目标记为"可投稿"。

### 常见错误
- 跳过投稿前审查直接投稿
- 交接文档写得太简略，后续参与者无法接手
- 不记录投稿版本和审稿过程
