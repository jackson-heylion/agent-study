from __future__ import annotations

from typing import Any

from models import ToolCall, ToolResult


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


TOOL_DEFINITIONS = [
    {
        "name": "calculator",
        "description": "执行确定性的数学计算；遇到明确算术问题时优先调用，而不是让模型心算。",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {"type": "string"},
            },
            "required": ["expression"],
        },
    },
    {
        "name": "get_order",
        "description": "根据订单号查询订单状态、金额和门店信息。只有涉及具体订单时调用。",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string"},
            },
            "required": ["order_id"],
        },
    },
]


def calculator(expression: str) -> str:
    # TODO: 自己实现一个足够安全的简单计算器。
    # 不建议直接 eval 用户输入；可以先只支持 + - * / 和括号。
    raise NotImplementedError


def get_order(order_id: str) -> dict[str, Any]:
    # TODO: A999 等不存在订单应该怎么表达？
    raise NotImplementedError


def execute_tool(call: ToolCall) -> ToolResult:
    """统一 Tool 执行入口。

    TODO:
    1. Unknown Tool
    2. Bad Arguments
    3. Tool Exception
    4. Business Error
    5. 返回统一 ToolResult
    """
    raise NotImplementedError
