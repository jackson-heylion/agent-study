# Agent 学习进度跟踪

开始日期：2026-08-31

详细学习路线见 [`LEARNING_PLAN.md`](./LEARNING_PLAN.md)。本文件只记录**当前状态、实际产出、耗时和复盘**，避免和计划文件重复。

---

# 一、总进度看板

| 模块 | 状态 | 完成度 | 当前产出 |
|---|---|---:|---|
| Agent Core | 🟨 进行中 | 5% | `lessons/01-agent-loop.md`、`labs/agent-loop/` |
| Agent Runtime | ⬜ 未开始 | 0% | - |
| Context Engineering | ⬜ 未开始 | 0% | - |
| RAG Engineering | ⬜ 未开始 | 0% | - |
| Evaluation | ⬜ 未开始 | 0% | - |
| Observability | ⬜ 未开始 | 0% | - |
| MCP / Tool / Skills | ⬜ 未开始 | 0% | - |
| Workflow + Agent | ⬜ 未开始 | 0% | - |
| Security / Permission | ⬜ 未开始 | 0% | - |
| Human-in-the-loop | ⬜ 未开始 | 0% | - |
| Model Router / Cost | ⬜ 未开始 | 0% | - |
| Production Agent | ⬜ 未开始 | 0% | - |

状态：⬜ 未开始 / 🟨 进行中 / ✅ 已完成 / 🔁 需要回炉

---

# 二、当前阶段

## Phase 1：Agent Core + Runtime

阶段目标：

- 自己实现最小 Agent Loop
- 理解 Tool Calling / Tool Result / Stop Condition
- 实现 Agent Runtime 的 State / Step / Checkpoint
- 实现 Retry / Resume / Cancel / Timeout
- 输出 Agent Runtime 设计笔记和架构图

阶段完成标准：

- [ ] 不依赖 Agent 框架实现 Agent Loop
- [ ] 支持连续多 Tool 调用
- [ ] 能解释 Function Calling 与 Agent 的区别
- [ ] 能解释 Model / Tool / Runtime 的职责边界
- [ ] 实现 Task State
- [ ] 实现 Checkpoint
- [ ] 实现 Retry
- [ ] 实现 Resume
- [ ] 实现 Tool Idempotency
- [ ] 完成 Long-running Agent Demo

---

# 三、本周

## Week 01：2026-08-31 ～ 2026-09-06

主题：**Minimal Agent Loop**

课程：[`lessons/01-agent-loop.md`](./lessons/01-agent-loop.md)

Lab：[`labs/agent-loop/`](./labs/agent-loop/)

### 本周目标

- [ ] 理解 LLM 不执行 Tool，只产生 Tool Call
- [ ] 理解 Tool Definition / Tool Implementation 的区别
- [ ] 自己实现最小 Agent Loop
- [ ] 实现 `calculator`
- [ ] 实现 `get_order`
- [ ] 支持 Tool Result 回灌
- [ ] 支持连续两次 Tool 调用
- [ ] 支持 `MAX_STEPS`
- [ ] 处理 Unknown Tool
- [ ] 处理参数错误
- [ ] 处理 Tool Exception
- [ ] 跑通 6 个验收 Case

### 当前状态

已开始。

已完成：

- [x] 建立 Week 01 学习目标
- [x] 建立 Lesson 01
- [x] 建立 Lab 01 验收标准

待完成：

> 从 `labs/agent-loop/` 开始写代码。第一版不要使用 LangGraph / Dify / AutoGen。

### 代码产出

- Commit / PR：待填写
- Demo：`labs/agent-loop/`
- 文档：`lessons/01-agent-loop.md`

### 学到的关键点

完成 Lab 后填写：

1. 
2. 
3. 

### Badcase

完成 Lab 后至少记录一个：

- 

### 工作中的实际应用

本周观察工作中的现有系统，找一个可以抽象成：

```text
User → Agent → Tool → Enterprise API
```

的真实场景，不要求马上实现。

候选：财务异常分析 / IAM 权限诊断 / 合同审查 / 工单分析 / 门店异常诊断。

### 本周时间投入

- 编码：0h
- 阅读：0h
- 总计：0h

### Week 01 验收问题

完成前必须能不看资料回答：

1. Function Calling 和 Agent 有什么区别？
2. 为什么 Tool Calling 不代表模型真正执行了函数？
3. Tool Result 为什么必须回灌 Context？
4. Agent Loop 为什么需要 Stop Condition？
5. Max Steps 属于 Prompt 层还是 Runtime 层？
6. Tool Schema 和实际 Tool 实现是什么关系？
7. Model / Tool / Runtime 分别负责什么？
8. “查询订单金额再乘 3”为什么需要多轮决策？

---

# 四、工作进度

## AI 工作机会

- [ ] 找到 3 个真实业务 Agent 场景
- [ ] 输出 1 份正式 AI 技术方案
- [ ] 主导 1 个 Agent PoC
- [ ] 推动 1 个真实 AI 项目上线
- [ ] 建立项目 Evaluation 指标
- [ ] 负责 MCP / Tool / 权限中的一个核心模块
- [ ] 成为团队 Agent 技术问题主要负责人之一

## 角色变化

逐月检查：

- [ ] 普通 CRUD 编码占比下降
- [ ] 架构设计占比提升
- [ ] 业务分析占比提升
- [ ] AI 方案占比提升
- [ ] Code Review 占比提升
- [ ] Coding Agent 使用比例提升
- [ ] 开始负责跨系统 AI 架构问题

---

# 五、月度复盘模板

```markdown
# YYYY-MM 月度复盘

## 本月完成度

- 计划：
- 实际：
- 完成率：xx%

## 最重要的 3 个产出

1. 
2. 
3. 

## 技术能力变化

- Agent Runtime：
- Context：
- Eval：
- RAG：
- Enterprise Integration：

## 工作变化

- 是否参与 AI 项目：
- 是否输出架构方案：
- 是否有生产落地：
- CRUD 占比是否下降：

## 最大问题

- 

## 下个月只做的 3 件事

1. 
2. 
3. 
```

---

# 六、年度验收

一年后至少拥有：

1. 一个 Agent Runtime 项目：Tool Registry / State / Checkpoint / Retry / Resume / Trace / Evaluation / Model Router / Permission。
2. 一个真实业务 Agent：真实用户、真实数据、真实权限、真实业务指标。
3. 能按高级 Agent / AI Application 岗位标准讨论 Runtime、Context、Eval、RAG、Tool、权限和成本。

最终目标：

> 能独立设计并落地一个生产级企业 Agent，从业务问题、Workflow、Agent Runtime、Tool、权限、Context、RAG、Evaluation 到上线指标形成完整闭环。
