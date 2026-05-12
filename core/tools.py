from abc import ABC, abstractmethod

from core.tool_result import ToolResult


class BaseTool(ABC):

    name: str
    description: str
    parameters: list = []

    @abstractmethod
    async def run(self, **kwargs) -> ToolResult:
        pass

    def schema(self):
        properties = {}

        required = []

        for p in self.parameters:
            properties[p.name] = {
                "type": p.type,
                "description": p.description
            }

            if p.required:
                required.append(p.name)

        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required
                }
            }
        }