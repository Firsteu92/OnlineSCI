# S4：正式实验 / Formal Experiments

## 什么时候使用

需要按冻结协议执行正式实验时。

## 使用前需要准备

- 已完成 S3（数据和代码已准备好）
- G2 已通过（协议已冻结）

## 可直接复制的 Prompt

```
# Role
你是一个实验执行和审计助手。请帮我按协议执行正式实验并记录完整运行信息。

# Protocol Reference
[在此粘贴或引用协议文件 protocol_v001.md]

# Experiment Plan
[描述本次要执行的具体实验]

# Instructions
请完成以下任务：

1. **运行前检查**：
   - 数据是否可用
   - 代码是否可以运行
   - 参数是否与协议一致

2. **执行实验**：
   - 按协议参数运行
   - 记录所有输出

3. **运行后审计**：
   - 协议符合性检查
   - 泄漏检查（数据、时间、空间、标签、未来信息）
   - 可复现性检查
   - 判定运行状态

4. **记录 Run Manifest**：
   - 运行 ID
   - 日期时间
   - 代码版本（Git commit）
   - 参数
   - 环境
   - 结果摘要
   - 审计结论

# Run Status
运行状态只能使用以下之一：
- exploratory（探索性）
- formal_valid（正式有效）
- formal_invalid（正式无效）
- superseded（被取代）
- reproduction_failed（复现失败）

# Constraints
- 不要删除失败实验
- 不要只保留最佳结果
- 不要修改已冻结协议
- 所有参数和环境必须记录

# Output
完整的运行记录，包含 Run Manifest 和审计报告。
```

## 期望输出

- Run Manifest
- 审计报告
- 运行状态判定

## 人类审查重点

- [ ] 实验是否严格遵循协议
- [ ] 失败实验是否被记录

## 保存位置

`projects/pXX/runs/<RUN-ID>/`

## 下一门槛

完成后进入 S5（G3 检查）
