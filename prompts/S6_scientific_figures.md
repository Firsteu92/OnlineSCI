# S6：科学图件设计 / Scientific Figures

## 什么时候使用

需要规划论文的核心图件时。

## 使用前需要准备

- 已完成论文逻辑规划（S6_paper_logic）
- 有实验数据和结果

## 可直接复制的 Prompt

```
# Role
你是一个科学可视化专家。请帮我设计和规划论文核心图件。

# Paper Outline
[粘贴论文提纲和证据分配]

# Available Data/Results
[描述可用的数据和实验结果]

# Target Journal
[输入目标期刊名称]

# Instructions
请完成以下任务：

1. **图件规划**：
   - 每张图的核心信息
   - 面板结构和逻辑
   - 图件的阅读顺序

2. **详细规格**：
   - 坐标轴标签和单位
   - 色标和配色方案
   - 图例位置
   - 字体大小
   - 分辨率要求

3. **视觉层级**：
   - 突出关键信息
   - 次要信息作为补充
   - 确保色盲友好

4. **准确性与证据**：
   - 每张图对应的实验结果
   - 是否准确表达了证据
   - 是否有无证据支撑的图件

# Constraints
- 不得为了美观隐藏不利结果
- 所有图件必须有对应的数据支持
- 标注必须清晰完整
- 配色方案需考虑色盲友好

# Output
figure_plan.md — 完整图件规划
figure_checklist.md — 每张图的技术检查清单
```

## 期望输出

- 图件规划文档
- 每张图的详细规格

## 人类审查重点

- [ ] 图件是否准确反映数据
- [ ] 是否有误导性可视化

## 保存位置

`projects/pXX/figures/figure_plan.md`、`projects/pXX/figures/figure_checklist.md`

## 下一门槛

完成后进入 S7 写作
