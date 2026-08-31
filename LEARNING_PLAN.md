# 12 个月 Agent 学习与工作规划

开始日期：2026-08-31

职业目标：

> 高级后端 / 开发组长 → Agent 后端 / AI 应用架构 → AI Application Tech Lead

核心原则：不从高级后端降维成初级 AI 开发，而是把已有的软件工程、分布式系统、业务建模、权限治理和团队协作经验迁移到 Agent 时代。

---

## 一、能力优先级

### P0：必须形成生产级能力

- Agent 核心机制：ReAct、Plan & Execute、Tool Calling、Structured Output、Stop Condition
- Agent Runtime：State、Checkpoint、Retry、Resume、Cancel、Timeout、Long-running Task
- Context Engineering：上下文构建、裁剪、压缩、缓存、Tool Result 管理
- Evaluation：Dataset、Regression、Task Success Rate、Badcase、Prompt / Model 对比
- Observability：Trace、Metrics、Token、Latency、Cost

### P1：形成企业级竞争力

- MCP / Tool / Skills
- Workflow + Agent
- RAG：Hybrid Search、Rerank、Metadata / Permission Filter
- Agent Security：IAM、Delegated Identity、Tool Permission、Audit
- Human-in-the-loop
- Model Router / Fallback / Cost Control
- Sandbox 基础

### P2：理解并能在需要时使用

- Multi-Agent / SubAgent
- A2A
- Computer Use
- vLLM / SGLang
- KV Cache / Prompt Cache
- Transformer / Attention 基础

### P3：暂不重点投入

- CUDA
- 从零训练大模型
- 深度 PyTorch
- RLHF / DPO / GRPO
- 纯算法研究

Python 已有基础，不单独安排学习阶段；在项目中按需补 FastAPI、Pydantic、asyncio、pytest、SQLAlchemy 等。

---

# 二、0～2 个月：Agent Core + Runtime

## 学习目标

真正理解一个 Agent 是如何运行的，而不是只会调用 LangChain / LangGraph。

### 1. 最小 Agent Loop

自行实现：

```text
User
 ↓
LLM
 ↓
Tool Call
 ↓
Tool Result
 ↓
LLM
 ↓
Answer
```

逐步加入：

- Max Steps
- Timeout
- Retry
- Tool Error
- Structured Output
- Stop Condition
- State

### 2. Agent Runtime

实现基本执行模型：

```text
Task
 ↓
Executor
 ↓
Step
 ↓
Checkpoint
 ↓
Tool
 ↓
Persist
 ↓
Next Step
```

至少支持：

- CREATED / RUNNING / WAITING_TOOL / WAITING_HUMAN / SUCCESS / FAILED / CANCELLED
- Checkpoint
- Retry
- Resume
- Cancel
- Timeout
- Tool 幂等
- 异常分类
- 长任务执行

## 代码产出

目录建议：

```text
labs/
├── agent-loop/
└── agent-runtime/
```

### 必做 Demo

- `agent-loop`：不依赖复杂框架的最小 Agent
- `agent-runtime`：支持 Checkpoint + Resume

### 学习完成标准

能够回答：

- Agent 和 Workflow 的边界是什么？
- Agent 为什么需要 State？
- 第 13 步失败为什么不能从第 1 步重跑？
- Retry 应该在哪一层做？
- Tool 如何保证幂等？
- Runtime 为什么比 Prompt 更重要？

## 工作目标

- 主动参与公司 Agent / AI 技术方案讨论
- 识别至少 3 个真实业务 Agent 场景
- 争取负责一个 PoC 的技术方案
- 减少普通 CRUD，自身更多承担架构、任务拆分、Review

---

# 三、3～4 个月：Context + RAG

## 学习目标

从“Prompt Engineering”升级到“Context Engineering”。

重点理解上下文组成：

```text
System Prompt
+ User Message
+ Conversation
+ Task State
+ Tool Result
+ RAG Context
+ User Memory
+ Business Context
```

## Context Engineering

掌握：

- Context Window 管理
- Dynamic Context
- Context Compression
- Summary
- Tool Result Compression
- Prompt Caching
- Long-running Agent 上下文管理
- Context Overflow

## Memory

区分：

- Conversation Memory
- User Memory
- Task Memory
- Business Memory

重点理解：

> 哪些数据应该进数据库，哪些适合向量检索，哪些不应该被抽象成 Memory。

## RAG

完成完整链路：

```text
Document
 ↓
Parse / Clean
 ↓
Chunk
 ↓
Embedding
 ↓
Hybrid Retrieval
 ↓
Rerank
 ↓
Permission Filter
 ↓
Context
 ↓
LLM
```

重点：

- Chunk Strategy
- BM25 + Vector Hybrid Search
- Query Rewrite
- Rerank
- Metadata Filter
- Permission Filter
- Citation
- Retrieval Evaluation

## 代码产出

```text
labs/
├── context-engineering/
└── rag/
```

## 学习完成标准

能够回答：

- Tool 返回几万字怎么处理？
- Context 太长怎么裁剪？
- Summary 会丢信息怎么办？
- Long Context 和 RAG 如何选？
- RAG 为什么搜不到？
- Hybrid Search 为什么通常比纯向量检索稳定？
- RAG 权限过滤应该在哪一层做？

## 工作目标

- 把现有一个真实业务流程拆成 Workflow / Agent / Tool / RAG 四层
- 输出一份内部 AI 技术方案
- 明确真实业务指标，而非只验证 Demo 能跑

---

# 四、5～6 个月：Evaluation + Observability

## 学习目标

从“感觉效果不错”升级到“可量化、可回归、可定位”。

## Evaluation

建立最小 Eval Framework：

```text
Dataset
 ↓
Run Agent
 ↓
Collect Trace
 ↓
Evaluate
 ↓
Compare Version
```

指标至少包括：

- Task Success Rate
- Tool Success Rate
- Accuracy
- Recall
- Hallucination Rate
- Steps
- Tokens
- Latency
- Cost
- Human Intervention Rate

支持：

- Prompt v1 vs v2
- Model A vs Model B
- RAG Strategy A vs B
- Regression Test

## Observability

Trace 结构至少覆盖：

```text
Task
 ├─ LLM
 ├─ Tool
 ├─ Retrieval
 ├─ LLM
 ├─ Tool
 └─ LLM
```

每一步记录：

- Input / Output
- Model
- Prompt Version
- Tool
- Duration
- Token
- Cost
- Error

## 代码产出

```text
labs/
└── evaluation/
```

至少建立 30～100 条测试集。

## 学习完成标准

能够回答：

- 为什么这个 Agent 失败？
- 是 Prompt、Model、Tool、RAG 还是 Context 问题？
- Prompt 更新后如何证明没有退化？
- 怎么衡量 Agent ROI？
- 如何找到高频 Badcase？

## 工作目标

- 真实项目开始建立效果指标
- Agent 项目必须有业务成功率 / 人工介入率 / 耗时变化
- 争取推动第一个生产级 AI 场景上线

---

# 五、7～9 个月：Enterprise Integration

## 学习目标

把 Agent 从 Demo 变成企业系统的一部分。

## MCP / Tool / Skills

重点不只是“会写 MCP Server”，而是：

```text
User
 ↓
Agent
 ↓
Tool / MCP
 ↓
Enterprise API
 ↓
IAM
 ↓
Resource
```

掌握：

- Tool Registry
- Tool Schema
- Tool Version
- MCP
- Skills
- Tool Timeout
- Tool Retry
- Tool Idempotency
- Tool Permission

## Security

重点研究：

- Delegated Identity
- RBAC / ABAC
- 用户身份透传
- Agent Service Account 边界
- Sensitive Tool
- Human Approval
- Audit Log
- Prompt Injection
- Data Leakage

核心原则：

> Agent 有权限，不代表用户有权限。

## Workflow + Agent

明确：

```text
确定性业务规则 → Workflow
开放性决策 → Agent
关键写操作 → Human Approval
```

## Model Engineering

了解：

- Model Router
- Fallback
- Cost / Latency
- Prompt Cache
- KV Cache
- vLLM / SGLang 基础

## 工作目标

争取让自己在团队中的角色从：

> 开发组长

逐步变成：

> 后端技术负责人 + AI 应用负责人

主动承担：

- Agent 架构
- MCP / Tool 体系
- 权限治理
- Evaluation
- AI 项目选型
- ROI 判断

---

# 六、10～12 个月：生产级 Agent 项目

## 推荐项目：财务异常分析 Agent

业务问题示例：

> 为什么某门店昨天对账差异 832 元？

Agent 链路：

```text
识别门店 / 营业日
 ↓
查询营业日报
 ↓
查询支付账单
 ↓
查询退款
 ↓
查询订单
 ↓
查询异常记录
 ↓
查询历史案例
 ↓
分析原因
 ↓
输出证据与结论
```

应覆盖：

- Agent Runtime
- Workflow
- Tool Calling
- MCP
- RAG
- Context
- State
- Checkpoint
- Retry
- Resume
- Trace
- Evaluation
- Permission
- Human Review

## 项目质量要求

不能只做到“能跑”。

至少要回答：

- 任务成功率多少？
- 哪些场景容易失败？
- 人工处理时间降低多少？
- Agent 平均执行几步？
- 平均 Token / Cost？
- 人工介入率多少？
- Tool 调用失败怎么恢复？
- 是否存在越权风险？

## 最终产出

```text
projects/
└── finance-agent/
    ├── README.md
    ├── architecture.md
    ├── eval.md
    ├── src/
    └── tests/
```

---

# 七、工作规划

## 0～3 个月

目标：成为团队中能够回答 Agent 技术问题的人。

- 参与 AI 技术调研
- 做 Agent PoC
- 输出架构方案
- 识别实际业务场景
- 使用 Coding Agent 承担更多重复编码
- 自己重点做需求理解、架构、Review、风险控制

## 3～6 个月

目标：推动至少一个真实 AI 业务上线。

优先场景：

1. 财务异常分析
2. 合同审查
3. IAM 权限诊断
4. 工单分析
5. 门店异常诊断

项目必须具备：

- 真实用户
- 真实数据
- 真实权限
- 真实业务指标

## 6～12 个月

目标：从后端负责人扩展为 AI 应用负责人。

理想工作占比：

| 工作 | 占比 |
|---|---:|
| 业务 / 需求判断 | 20% |
| 架构设计 | 25% |
| AI 方案 | 20% |
| 技术 Review | 15% |
| 项目推进 | 10% |
| 自己写核心代码 | 10% |

逐步减少：

- 普通 Controller
- Mapper
- CRUD
- DTO
- 简单 Bug
- 重复接口

---

# 八、每周投入

建议每周 8～10 小时，不单独学习 Python。

| 时间 | 内容 |
|---|---|
| 周一 1h | Agent Core / Runtime |
| 周二 1h | Runtime / Context |
| 周三 1h | Eval / RAG / Tool |
| 周四 1h | 大厂技术文章 / 源码 |
| 周五 0.5h | 总结 |
| 周六 3h | 项目实践 |
| 周日 2h | 项目 + 复盘 |

学习投入比例：

- 50% 写代码
- 20% 架构思考
- 15% 官方文档 / 源码
- 10% 理论
- 5% 行业资讯

---

# 九、12 个月验收标准

一年后至少拥有：

## 1. 一个 Agent Runtime 项目

包含：

- Tool Registry
- State
- Checkpoint
- Retry
- Resume
- Trace
- Evaluation
- Model Router
- Permission

## 2. 一个真实业务 Agent 项目

最好具备量化指标：

```text
人工处理时间：20 min → 3 min
任务成功率：xx%
人工介入率：xx%
月执行量：xxxxx
平均成本：xx / task
```

## 3. 面试能力

能够独立讨论：

- Agent Runtime 设计
- Long-running Agent
- Context Engineering
- Eval / Badcase
- Tool 幂等与重试
- Workflow vs Agent
- Agent 权限
- RAG Evaluation
- Model Router
- Agent Cost / Latency

---

# 十、目标岗位关键词

未来看机会时重点搜索：

- AI Agent 研发工程师
- Agent 后端研发
- Agent Platform Engineer
- Agent Runtime Engineer
- Agent Infra
- Harness Engineer
- AI Application Engineer
- AI Application Tech Lead
- AI 应用架构师

不以以下方向为主要目标：

- 大模型训练
- RL / Post-training
- CUDA / 推理内核
- 纯算法研究

最终定位：

> 一个懂业务、懂复杂后端系统、懂 Agent Runtime 和 AI 工程化，并能把企业 AI 产品真正落地的高级软件工程师 / 技术负责人。
