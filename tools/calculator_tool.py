from core.tool_result import ToolResult
from core.tool_schema import ToolParameter
from core.tools import BaseTool


class CalculatorTool(BaseTool):

    name = "calculator"

    description = "Perform basic math calculations"

    parameters = [
        ToolParameter(
            name="expression",
            type="string",
            description="Math expression",
            required=True
        )
    ]

    async def run(self, expression: str):
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
