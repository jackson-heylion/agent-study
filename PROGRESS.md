# Agent 学习进度跟踪

开始日期：2026-08-31

用途：持续记录学习进度、代码产出、工作落地和阶段复盘。

---

# 一、总进度看板

| 模块 | 状态 | 完成度 | 产出 |
|---|---|---:|---|
| Agent Core | ⬜ 未开始 | 0% | - |
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

状态约定：

- ⬜ 未开始
- 🟨 进行中
- ✅ 已完成
- 🔁 需要回炉

---

# 二、阶段目标

## Phase 1：Agent Core + Runtime

目标时间：第 1～2 个月

### Agent Core

- [ ] 自己实现最小 Agent Loop
- [ ] 支持 Tool Calling
- [ ] 支持 Structured Output
- [ ] 支持 Max Steps
- [ ] 支持 Stop Condition
- [ ] 支持 Timeout
- [ ] 支持 Tool Error
- [ ] 理解 ReAct
- [ ] 理解 Plan & Execute
- [ ] 对比手写 Agent Loop 与 LangGraph

### Agent Runtime

- [ ] 定义 Task State
- [ ] 实现 Executor
- [ ] 实现 Step
- [ ] 实现 Checkpoint
- [ ] 实现 Retry
- [ ] 实现 Resume
- [ ] 实现 Cancel
- [ ] 实现 Timeout
- [ ] 实现 Tool Idempotency
- [ ] 区分 LLM / Tool / Network / Business Error
- [ ] 完成 Long-running Agent Demo

### 阶段产出

- [ ] `labs/agent-loop/`
- [ ] `labs/agent-runtime/`
- [ ] 一篇 Agent Runtime 设计笔记
- [ ] 一张 Runtime 架构图

---

## Phase 2：Context + RAG

目标时间：第 3～4 个月

### Context Engineering

- [ ] 梳理 Context 组成
- [ ] 实现 Dynamic Context
- [ ] 实现 Context Trimming
- [ ] 实现 Context Compression
- [ ] 实现 Tool Result Compression
- [ ] 实验 Prompt Cache
- [ ] 实验长任务 Context 管理
- [ ] 对比不同 Context 策略效果

### Memory

- [ ] 区分 Conversation / User / Task / Business Memory
- [ ] 明确 Memory 持久化策略
- [ ] 明确哪些数据不应该进入向量库

### RAG

- [ ] 文档 Parse / Clean
- [ ] Chunk Strategy
- [ ] Embedding
- [ ] Vector Retrieval
- [ ] BM25
- [ ] Hybrid Search
- [ ] Query Rewrite
- [ ] Rerank
- [ ] Metadata Filter
- [ ] Permission Filter
- [ ] Citation
- [ ] Retrieval Evaluation

### 阶段产出

- [ ] `labs/context-engineering/`
- [ ] `labs/rag/`
- [ ] Context Strategy 对比记录
- [ ] RAG Eval 数据集

---

## Phase 3：Evaluation + Observability

目标时间：第 5～6 个月

### Evaluation

- [ ] 建立 Eval Dataset
- [ ] 至少准备 30 条 Case
- [ ] 扩展到 100 条 Case
- [ ] Task Success Rate
- [ ] Tool Success Rate
- [ ] Accuracy
- [ ] Recall
- [ ] Hallucination Rate
- [ ] Human Intervention Rate
- [ ] Prompt v1 vs v2
- [ ] Model A vs Model B
- [ ] RAG Strategy A vs B
- [ ] Regression Test

### Observability

- [ ] Task Trace
- [ ] LLM Span
- [ ] Tool Span
- [ ] Retrieval Span
- [ ] Token
- [ ] Latency
- [ ] Cost
- [ ] Error Classification
- [ ] Badcase Trace Replay

### 阶段产出

- [ ] `labs/evaluation/`
- [ ] Eval Dashboard / 报表
- [ ] Badcase 文档
- [ ] Prompt / Model 对比报告

---

## Phase 4：Enterprise Integration

目标时间：第 7～9 个月

### MCP / Tool

- [ ] Tool Registry
- [ ] Tool Schema
- [ ] Tool Version
- [ ] MCP Server
- [ ] Tool Timeout
- [ ] Tool Retry
- [ ] Tool Idempotency
- [ ] Tool Permission

### Security

- [ ] Delegated Identity
- [ ] RBAC / ABAC
- [ ] 用户身份透传
- [ ] Service Account 边界
- [ ] Sensitive Tool
- [ ] Human Approval
- [ ] Audit Log
- [ ] Prompt Injection 防护
- [ ] Data Leakage 风险分析

### Workflow + Agent

- [ ] 明确 Workflow / Agent 边界
- [ ] 确定性步骤使用 Workflow
- [ ] 开放决策步骤使用 Agent
- [ ] 高风险写操作加入 Approval

### Model Engineering

- [ ] Model Router
- [ ] Model Fallback
- [ ] Cost Tracking
- [ ] Latency Tracking
- [ ] Prompt Cache
- [ ] 了解 KV Cache
- [ ] 了解 vLLM / SGLang

---

## Phase 5：Production Agent

目标时间：第 10～12 个月

推荐主项目：`projects/finance-agent/`

- [ ] 明确业务问题
- [ ] 明确真实用户
- [ ] 明确数据源
- [ ] 明确权限边界
- [ ] 定义 Tools
- [ ] 定义 Workflow
- [ ] 定义 Agent 决策范围
- [ ] 实现 Runtime
- [ ] 实现 Checkpoint / Resume
- [ ] 接入 RAG
- [ ] 接入 Trace
- [ ] 建立 Eval Dataset
- [ ] 建立业务指标
- [ ] 建立 Human Review
- [ ] 完成生产级架构文档

### 必须量化

- [ ] 人工处理时间
- [ ] Agent 处理时间
- [ ] Task Success Rate
- [ ] Human Intervention Rate
- [ ] Tool Failure Rate
- [ ] 平均 Steps
- [ ] 平均 Token
- [ ] 平均 Cost
- [ ] 高频 Badcase

---

# 三、工作进度跟踪

学习必须和工作经历同步变化。

## AI 工作机会

- [ ] 找到 3 个真实业务 Agent 场景
- [ ] 输出 1 份正式 AI 技术方案
- [ ] 主导 1 个 Agent PoC
- [ ] 推动 1 个真实 AI 项目上线
- [ ] 建立项目 Evaluation 指标
- [ ] 负责 MCP / Tool / 权限其中一个核心模块
- [ ] 成为团队 Agent 技术问题主要负责人之一

## 工作角色变化

逐月检查：

- [ ] 普通 CRUD 编码占比下降
- [ ] 架构设计占比提升
- [ ] 业务分析占比提升
- [ ] AI 方案占比提升
- [ ] Code Review 占比提升
- [ ] Coding Agent 使用比例提升
- [ ] 开始负责跨系统 AI 架构问题

---

# 四、每周进度模板

复制下面模板，每周追加一次。

```markdown
## Week XX：YYYY-MM-DD ～ YYYY-MM-DD

### 本周目标

- [ ] 
- [ ] 
- [ ] 

### 实际完成

- 
- 
- 

### 代码产出

- Commit / PR：
- Demo：
- 文档：

### 学到的关键点

1. 
2. 
3. 

### 遇到的问题 / Badcase

- 

### 工作中的实际应用

- 

### 本周时间投入

- 编码：h
- 阅读：h
- 总计：h

### 下周优先级

1. 
2. 
3. 
```

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

# 六、季度验收

## Q1 验收

- [ ] 能独立实现 Agent Loop
- [ ] 能解释 Runtime 状态机
- [ ] 有 Checkpoint / Resume Demo
- [ ] 工作中找到真实 AI 场景

## Q2 验收

- [ ] 掌握 Context Engineering
- [ ] 完整实现 RAG 链路
- [ ] 建立 Eval Dataset
- [ ] 能定位 Agent Badcase
- [ ] 至少一个 AI PoC

## Q3 验收

- [ ] MCP / Tool / Permission 形成完整理解
- [ ] 能设计企业级 Agent 权限链路
- [ ] 能设计 Workflow + Agent
- [ ] 推动真实 AI 项目上线

## Q4 验收

- [ ] 有生产级 Agent 项目
- [ ] 有量化业务指标
- [ ] 有完整架构文档
- [ ] 有 Evaluation 报告
- [ ] 能按大厂高级 Agent 岗位标准讨论系统设计

---

# 七、学习过滤器

每次准备学习一个新东西前先问：

1. 它解决什么真实问题？
2. 是否属于 Runtime / Context / Eval / Enterprise Integration？
3. 是否能用于当前项目？
4. 如果只是某个新框架的 API，是否真的值得投入？

如果四个问题都答不上来，降低优先级。

---

# 八、年度最终状态

目标不是“学完 AI”，而是达到：

> 能独立设计并落地一个生产级企业 Agent，从业务问题、Workflow、Agent Runtime、Tool、权限、Context、RAG、Evaluation 到上线指标形成完整闭环。
