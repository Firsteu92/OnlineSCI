# Quick Start — 5 分钟上手 OnlineSCI

## 1. 获取 OnlineSCI

```bash
git clone https://github.com/Firsteu92/OnlineSCI.git
cd OnlineSCI
```

或直接在 GitHub 页面下载 ZIP。

## 2. 选择空白项目

选择一个空白项目位：

```bash
# 查看项目看板
cat projects/DASHBOARD.md

# 进入一个空白项目（例如 P01）
cd projects/p01/
```

所有项目（P01–P10）结构完全一致，都是空白模板。

## 3. 判断当前阶段

打开工作流指南：

```bash
cat AI_WORKFLOW_GUIDE.md
```

如果你是**第一次开始一个研究项目**，你处于 **S0（项目建立）** 阶段。

## 4. 找到对应 Prompt

每个阶段都有对应的 Prompt 文件：

```
prompts/S0_project_setup.md    # 如果你在 S0
prompts/S1_deep_research.md    # 如果你在 S1
...
```

## 5. 复制 Prompt 到 Agent

打开对应 Prompt 文件，复制内容到任意 AI Agent（ChatGPT、Claude、Codex、Cursor 等）。

Prompt 中包含 `[占位符]`，按你的实际情况填写。

## 6. 人工核验 Agent 输出

Agent 执行完成后，使用对应的 Checklist 逐项检查：

```
checklists/G0_project_card.md           # S0 完成后检查
checklists/G1_literature_and_innovation.md  # S1 完成后检查
...
```

## 7. 保存结果

将 Agent 的输出保存到项目目录的规定位置：

```
projects/p01/PROJECT.md          # 项目卡
projects/p01/literature/         # 文献笔记
projects/p01/protocols/          # 实验协议
...
```

## 8. 进入下一阶段

当当前门槛通过后，返回第 3 步，进入下一阶段。

---

**详细说明请阅读：** [AI_WORKFLOW_GUIDE.md](../AI_WORKFLOW_GUIDE.md)
