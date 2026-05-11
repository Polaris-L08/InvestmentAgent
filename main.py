import os

from dotenv import load_dotenv

from core.llm_client import LLMClient
from core.tool_registry import ToolRegistry

from agents.simple_agent import SimpleAgent

from tools.calculator_tool import CalculatorTool


load_dotenv()


registry = ToolRegistry()

registry.register(
    CalculatorTool()
)


llm = LLMClient(
    api_key=os.getenv("LLM_API_KEY"),
    model=os.getenv("LLM_MODEL_ID"),
    url=os.getenv("LLM_BASE_URL")
)


agent = SimpleAgent(
    llm_client=llm,
    tool_registry=registry
)


result = agent.run(
    "What is 25 * 48 + 1024?"
)

print(result)