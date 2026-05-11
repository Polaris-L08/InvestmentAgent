from abc import ABC, abstractmethod
from typing import Any

from core.tool_result import ToolResult


class BaseTool(ABC):

    name: str
    description: str

    @abstractmethod
    def run(self, **kwargs) -> ToolResult:
        pass

    @abstractmethod
    def schema(self) -> dict:
        pass