# Lab 01：Minimal Agent Loop

配套课程：[`lessons/01-agent-loop.md`](../../lessons/01-agent-loop.md)

## 目标

亲手实现一个不依赖 Agent 编排框架的最小 Agent Loop。

## 本 Lab 只做

- Tool Calling
- Tool Result 回灌
- 多轮 Agent Loop
- Max Steps
- Unknown Tool
- 参数错误
- Tool Exception
- Final Answer

## 不做

- LangGraph
- MCP
- RAG
- Memory
- Checkpoint
- Resume
- Web UI

## 推荐文件

```text
labs/agent-loop/
├── README.md
├── main.py
├── llm.py
├── tools.py
└── models.py
```

## 两个 Tool

### calculator

```python
calculator(expression: str) -> str
```

### get_order

Mock 数据：

```python
ORDERS = {
    "A001": {
        "status": "PAID",
        "amount": 128.5,
        "shop": "广州天河店",
    },
    "A002": {
        "status": "REFUNDED",
        "amount": 88.0,
        "shop": "广州番禺店",
    },
}
```

## 验收 Case

- [ ] 普通问答不调用 Tool
- [ ] `123 * 456 + 789` 调用 calculator
- [ ] 查询 A001 调用 get_order
- [ ] A002 能基于 REFUNDED 做解释
- [ ] A999 不导致 Agent 崩溃
- [ ] “A001 金额乘以 3”完成两次 Tool 调用链
- [ ] 达到 MAX_STEPS 时安全停止
- [ ] Unknown Tool 有明确错误处理
- [ ] Tool 参数错误有明确错误处理

## 约束

核心代码尽量控制在 100～300 行。

如果为了这个 Lab 写出了 Tool Framework、Plugin Framework、DI Container 等抽象，说明过度设计了。

## 提交建议

完成后提交：

```text
feat: implement minimal agent loop
```

并在 `PROGRESS.md` 的 Week 01 中记录：

- 实际耗时
- 代码 Commit
- 3 个最重要的理解
- 至少 1 个 Badcase
