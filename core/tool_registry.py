from typing import Dict
from core.tools import BaseTool


class ToolRegistry:

    def __init__(self):
        self.tools: Dict[str, BaseTool] = {}

    def register(self, tool: BaseTool):
        self.tools[tool.name] = tool

    def get_tool(self, name: str):
        return self.tools.get(name)

    def get_tool_schemas(self):

        return [
            tool.schema()
            for tool in self.tools.values()
        ]