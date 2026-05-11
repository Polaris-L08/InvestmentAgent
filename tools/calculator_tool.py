from core.tool_result import ToolResult
from core.tools import BaseTool


class CalculatorTool(BaseTool):

    name = "calculator"

    description = "Perform basic math calculations"

    def run(self, expression: str):
        try:
            result = eval(expression)

            return ToolResult(
                success=True,
                content= result
            )
        except Exception as e:

            return ToolResult(
                success=False,
                content= str(e)
            )

    def schema(self):

        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "Math expression"
                        }
                    },
                    "required": ["expression"]
                }
            }
        }