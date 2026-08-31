# Lesson 01：亲手实现最小 Agent Loop

> Week 01 · 2026-08-31 ～ 2026-09-06

## 本周唯一目标

不依赖 LangGraph / Dify / AutoGen 等编排框架，亲手实现一个最小 Agent Loop，并真正理解：

1. 模型为什么决定调用 Tool？
2. Tool Result 为什么要重新放回 Context？
3. Agent 为什么本质上是一个受约束的循环？
4. 循环什么时候应该停止？
5. Tool 出错时谁负责处理？

本周先不做 Checkpoint、Resume、Memory、RAG、Multi-Agent。

---

# 1. 先建立正确心智模型

LLM 本身不会真的执行函数。

所谓 Tool Calling，本质上是模型输出一段结构化的“调用意图”：

```text
User
  ↓
LLM
  ↓
"我要调用 get_order(order_id=123)"
  ↓
你的程序执行 get_order
  ↓
得到 Tool Result
  ↓
把 Tool Result 放回 Context
  ↓
再次调用 LLM
  ↓
Final Answer / Next Tool Call
```

所以最小 Agent 的核心不是 Prompt，而是下面这个循环：

```python
while not done:
    response = call_llm(context, tools)

    if response.has_tool_call:
        result = execute_tool(response.tool_call)
        context.append(response.tool_call)
        context.append(result)
    else:
        return response.final_answer
```

真正需要你理解的是：

> **LLM 负责决策，程序负责执行和控制。**

---

# 2. Agent 与普通 LLM 调用的区别

普通 LLM：

```text
Input → Model → Output
```

Agent：

```text
Input
 ↓
Model
 ↓
Decision
 ├── Final Answer → End
 └── Tool Call
        ↓
      Execute
        ↓
      Observation
        ↓
      Model
        ↓
       ...
```

因此 Agent 至少包含四个角色：

| 角色 | 职责 |
|---|---|
| Model | 做决策 |
| Context | 保存当前已知信息 |
| Tool Registry | 告诉模型有哪些能力 |
| Runtime Loop | 控制执行、停止和异常 |

后面学习 Runtime、Context、MCP、Evaluation，实际上都是在扩展这四部分。

---

# 3. Tool Definition 到底是什么

Tool Definition 通常至少包括：

```json
{
  "name": "get_order",
  "description": "根据订单号查询订单信息",
  "parameters": {
    "type": "object",
    "properties": {
      "order_id": {
        "type": "string"
      }
    },
    "required": ["order_id"]
  }
}
```

这里要意识到：

- `name`：模型输出的调用目标
- `description`：模型决定“什么时候该调用它”的重要依据
- `parameters`：约束模型应该提供什么参数
- JSON Schema：只是接口契约，不是实际函数

真正的实现仍然在你的程序里：

```python
def get_order(order_id: str) -> dict:
    ...
```

## 思考题

同一个 Tool，如果把 description 从：

> 查询订单

改成：

> 当用户询问具体订单状态、金额、支付状态时调用；不要用于查询门店营业数据

模型行为会不会变化？为什么？

---

# 4. 第一版只做两个 Tool

不要一开始做天气、浏览器、MCP 等复杂能力。

本周使用两个纯本地 Tool：

## calculator

```text
calculator(expression)
```

示例：

```text
用户：123 * 456 等于多少？
```

Agent 应调用 calculator，而不是让模型心算。

## get_order

使用 Mock 数据：

```python
ORDERS = {
    "A001": {
        "status": "PAID",
        "amount": 128.5,
        "shop": "广州天河店"
    },
    "A002": {
        "status": "REFUNDED",
        "amount": 88.0,
        "shop": "广州番禺店"
    }
}
```

示例：

```text
用户：A002 为什么没有完成交易？
```

模型应该先调用 `get_order`，再根据结果回答。

---

# 5. 本周代码结构

在：

```text
labs/agent-loop/
```

完成：

```text
agent-loop/
├── README.md
├── main.py
├── llm.py
├── tools.py
└── models.py
```

建议职责：

## `models.py`

定义最少几个数据结构：

```python
ToolCall
ToolResult
AgentResponse
```

不要过度设计。

## `tools.py`

负责：

```text
Tool定义
Tool注册
Tool实际执行
```

## `llm.py`

只包装具体模型 SDK。

目标是让 Agent Loop 不直接依赖供应商返回结构。

例如：

```python
def call_llm(messages, tools) -> AgentResponse:
    ...
```

## `main.py`

这里只保留 Agent Loop。

伪代码：

```python
messages = [user_message]

for step in range(MAX_STEPS):
    response = call_llm(messages, tools)

    if response.final_answer:
        print(response.final_answer)
        break

    for tool_call in response.tool_calls:
        result = execute_tool(tool_call)
        messages.append(...)
        messages.append(...)
else:
    raise RuntimeError("max steps exceeded")
```

---

# 6. 必须自己处理的 5 个问题

不要直接交给框架。

## 6.1 Max Steps

必须限制最大循环次数，例如：

```python
MAX_STEPS = 8
```

思考：

> 如果没有 Max Steps，模型不断调用 Tool 会发生什么？

## 6.2 Unknown Tool

模型要求调用一个不存在的 Tool：

```text
delete_all_orders
```

你的 Runtime 怎么处理？

推荐：把明确错误作为 Tool Result 返回给模型，而不是直接程序崩溃。

## 6.3 Bad Arguments

例如：

```json
{
  "order": 123
}
```

但 Tool 需要的是：

```json
{
  "order_id": "A001"
}
```

要区分：

- Schema Validation Error
- Tool Business Error

## 6.4 Tool Exception

Tool 自己抛异常时，不要让整个进程直接退出。

先捕获并形成统一结果。

## 6.5 Stop Condition

第一版本只允许两种停止：

```text
1. Model 返回 Final Answer
2. 达到 MAX_STEPS
```

后面 Runtime 阶段再加入：

```text
Timeout / Cancel / Waiting Human / Fatal Error
```

---

# 7. 本周测试 Case

至少跑完下面 6 个 Case。

## Case 1：无需 Tool

```text
用户：用一句话解释什么是 Agent。
```

期望：直接回答。

## Case 2：Calculator

```text
用户：123 * 456 + 789 等于多少？
```

期望：调用 calculator。

## Case 3：单 Tool

```text
用户：订单 A001 当前是什么状态？
```

期望：调用 get_order。

## Case 4：Tool Result 后继续推理

```text
用户：A002 为什么没有完成正常交易？
```

期望：查询订单，再解释 REFUNDED。

## Case 5：不存在的数据

```text
用户：查询订单 A999。
```

期望：Tool 返回业务错误，Agent 能正常解释，而不是崩溃。

## Case 6：复合任务

```text
用户：A001 的订单金额乘以 3 是多少？
```

期望执行类似：

```text
get_order(A001)
→ 获得 amount=128.5
→ calculator("128.5 * 3")
→ Final Answer
```

这个 Case 很重要，因为它开始体现“循环”而不是单次 Function Calling。

---

# 8. 本周不要做什么

- 不要接数据库
- 不要接 Redis
- 不要接 MCP
- 不要上 LangGraph
- 不要做 Web UI
- 不要做 RAG
- 不要做 Memory
- 不要抽象通用 Agent Framework

目标只有：

> **100～300 行核心代码，把 Agent Loop 搞明白。**

---

# 9. 完成标准

本周结束前，你应该能不看资料回答：

1. Function Calling 和 Agent 有什么区别？
2. 为什么 Tool Calling 并不代表模型执行了 Tool？
3. Tool Result 为什么必须回灌 Context？
4. Agent Loop 为什么一定需要 Stop Condition？
5. Max Steps 属于 Prompt 层还是 Runtime 层？
6. Tool Schema 和实际 Tool 实现是什么关系？
7. Model、Tool、Runtime 三者分别负责什么？
8. Case 6 为什么至少需要两轮模型决策？

如果这些问题说不清楚，不进入 Agent Runtime。

---

# 10. 完成后的下一课

Lesson 02：**从 Agent Loop 到 Agent Runtime**

会加入：

```text
Task State
Step
Checkpoint
Retry
Error Classification
Resume
```

重点问题：

> Agent 执行到第 13 步失败，系统应该如何恢复？
