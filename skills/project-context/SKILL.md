# Skill: project-context

## Purpose
建立和读取项目卡，汇总当前状态，维护项目阶段、关键决定和下一步，为其他 Skills 提供上下文。

## When to Use
- S0 阶段建立新项目时
- 在任何阶段开始时回顾项目上下文
- 项目状态发生变化时更新

## Required Inputs
- 研究问题的初步描述
- 可用资源和限制

## Optional Inputs
- 已有文献列表
- 初步数据描述
- 协作人员信息

## Preconditions and Gate Checks
- 已选择空白项目位（P01–P10）
- G0：尚未通过时，项目未正式建立

## Mandatory Procedure
1. 确认项目位可用
2. 定义核心研究问题
3. 填写 PROJECT.md（研究问题、假设、预期方法、资源、限制）
4. 创建 STATUS.md（当前阶段、G 门槛状态、各组件状态）
5. 创建 project.yml（标准字段）
6. 定期更新 STATUS.md

## Prohibited Actions
- 不在项目中写入其他项目的上下文
- 不预填真实研究主题到空白模板
- 不修改未授权的 P 项目

## Required Outputs
- `PROJECT.md`
- `STATUS.md`
- `project.yml`

## Human Review
- 确认研究问题准确反映意图
- 确认项目范围合理

## Completion Criteria
- PROJECT.md、STATUS.md、project.yml 均已创建
- G0 状态已更新

## Failure and Fallback
- 项目位已占用：选择另一个空白位
- 研究问题不明确：进一步讨论和细化后再创建

## Related Prompts
- [S0_project_setup.md](../../prompts/S0_project_setup.md)

## Related Templates
- [project.yml](../../templates/project.yml)
- [PROJECT.md](../../templates/PROJECT.md)
- [STATUS.md](../../templates/STATUS.md)
