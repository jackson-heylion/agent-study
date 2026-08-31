from __future__ import annotations

from typing import Any

from llm import call_llm
from tools import TOOL_DEFINITIONS, execute_tool


MAX_STEPS = 8


def run_agent(user_input: str) -> str:
    messages: list[dict[str, Any]] = [
        {"role": "user", "content": user_input},
    ]

    # TODO: 完成真正的 Agent Loop。
    #
    # 要求：
    # 1. 最多执行 MAX_STEPS。
    # 2. 每轮调用 call_llm。
    # 3. final_answer 非空时立即结束。
    # 4. tool_calls 非空时逐个 execute_tool。
    # 5. 把模型的 Tool Call 和 Tool Result 正确回灌 messages/context。
    # 6. Tool 失败不能让整个进程直接崩溃。
    # 7. 达到 MAX_STEPS 时明确失败，而不是无限循环。
    #
    # 注意：具体供应商的 message/tool_result 格式可以在 llm.py 中做适配，
    # 不要让本文件被某个模型 SDK 的返回结构污染。
    raise NotImplementedError


if __name__ == "__main__":
    while True:
        text = input("You> ").strip()
        if text.lower() in {"exit", "quit"}:
            break
        if not text:
            continue

        try:
            print("Agent>", run_agent(text))
        except Exception as exc:
            print("Agent error>", exc)
