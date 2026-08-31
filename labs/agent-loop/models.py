from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any]
    call_id: str | None = None


@dataclass
class ToolResult:
    name: str
    success: bool
    output: Any = None
    error: str | None = None
    call_id: str | None = None


@dataclass
class AgentResponse:
    final_answer: str | None = None
    tool_calls: list[ToolCall] = field(default_factory=list)
