# S5：验证与证据整理 / Validation and Evidence

## 什么时候使用

正式实验完成后，需要验证结果并建立证据链时。

## 使用前需要准备

- 已完成 S4（有正式实验运行记录）
- G3 应已通过

## 可直接复制的 Prompt

```
# Role
你是一个科研证据管理助手。请帮我验证实验结果并建立证据账本。

# Research Question
[在此输入研究问题]

# Experiment Results
[粘贴或描述已完成的实验结果]

# Instructions
请完成以下任务：

1. **验证分析**：
   - 检查结果是否可重复
   - 是否支持独立验证
   - 跨数据/场景验证
   - 分析失败和冲突结果

2. **证据账本**：
   - 列出论文中可能做出的每一条主要声明
   - 为每条声明匹配证据来源（文献、实验、图表）
   - 判定每条声明的证据强度

3. **证据状态**（每项声明选择一个）：
   - supported — 有充分证据支持
   - partially_supported — 部分支持
   - conflicting — 证据冲突
   - unsupported — 无证据支持
   - pending — 待补充
   - rejected — 已被证伪

4. **无证据声明**：
   - 列出当前无证据支持但论文可能需要的声明
   - 建议如何补充

# Output Format
输出以下文件：
1. claims.csv — 声明清单
2. claim_evidence_matrix.csv — 声明-证据矩阵
3. evidence_ledger.md — 综合证据账本
4. unsupported_claims.md — 无证据声明
5. conflicts.md — 冲突结果分析

# Constraints
- 诚实地记录冲突和失败结果
- 不夸大证据强度
- 区分"有证据"和"无证据"
- 不要让论文结论超出证据支持范围
```

## 期望输出

- 证据账本和声明矩阵
- 无证据声明清单
- 冲突结果分析

## 人类审查重点

- [ ] 声明的证据强度判定是否合理
- [ ] 是否有被忽略的冲突证据

## 保存位置

`projects/pXX/evidence/`

## 下一门槛

**G4**：通过后进入 S6
