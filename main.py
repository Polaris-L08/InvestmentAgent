import asyncio
import os

from dotenv import load_dotenv

from core.llm_client import LLMClient
from core.memory import MemoryManager
from core.tool_registry import ToolRegistry

from agents.simple_agent import SimpleAgent

from tools.calculator_tool import CalculatorTool

load_dotenv()


async def main():
    registry = ToolRegistry()

    registry.register(
        CalculatorTool()
    )

    llm = LLMClient(
        api_key=os.getenv("LLM_API_KEY"),
        model=os.getenv("LLM_MODEL_ID"),
        url=os.getenv("LLM_BASE_URL"),
        # 可能与connection error有关，需要进行类型转换
        timeout=int(os.getenv("LLM_TIMEOUT", 60))
    )

    memory = MemoryManager()

    agent = SimpleAgent(
        llm_client=llm,
        tool_registry=registry,
        memory_manager=memory
    )

    result = await agent.run(
        "What is 25 * 48 + 1024?"
    )

    print(result)


asyncio.run(main())
