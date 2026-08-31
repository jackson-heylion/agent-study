from __future__ import annotations

from typing import Any

from models import AgentResponse


def call_llm(messages: list[dict[str, Any]], tools: list[dict[str, Any]]) -> AgentResponse:
    """调用你选择的模型，并转换成统一 AgentResponse。

    第一版要求：
    - 只在这里依赖具体模型 SDK。
    - main.py 不应该知道 OpenAI / Anthropic / 其他供应商响应结构。
    - 如果模型返回普通文本，转换为 final_answer。
    - 如果模型返回 Tool Call，转换为 tool_calls。

    推荐先任选一个你手头最方便调用的模型完成，不需要同时兼容多个供应商。
    """
    raise NotImplementedError
