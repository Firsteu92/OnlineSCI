# Skill: scientific-figure-designer

## Purpose
规划核心图件的面板结构、变量、单位、坐标、图例、视觉层级和期刊尺寸，确保图件准确表达证据。

## When to Use
- S6 阶段，论文提纲已确定时
- 需要设计新图表时

## Required Inputs
- 论文提纲
- 实验数据和结果
- 目标期刊的图件要求

## Optional Inputs
- 已有图件草稿
- 配色方案偏好

## Preconditions and Gate Checks
- G3、G4 应已通过

## Mandatory Procedure
1. 为每个核心图件确定传达的信息
2. 设计面板结构和逻辑
3. 标注坐标轴、单位、色标、图例
4. 规划视觉层级（突出关键、补充次要）
5. 检查色盲友好和期刊分辨率要求
6. 验证图件是否准确表达证据

## Prohibited Actions
- **不得为了美观隐藏不利结果**
- 不创建无数据支撑的图件
- 不误导性缩放坐标轴

## Required Outputs
- `figure_plan.md`
- `figure_checklist.md`

## Human Review
- 确认图件准确反映数据
- 确认标注完整

## Completion Criteria
- 图件布局和规格已确定
- 与提纲中的证据分配一致

## Failure and Fallback
- 数据不足以支撑图件：返回 S4 补充或调整

## Related Prompts
- [S6_scientific_figures.md](../../prompts/S6_scientific_figures.md)
