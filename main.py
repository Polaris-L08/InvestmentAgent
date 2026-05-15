import asyncio
import os

from dotenv import load_dotenv

from agents.simple_agent import SimpleAgent
from core.llm_client import LLMClient
from core.memory import MemoryManager
from core.tool_registry import ToolRegistry
from core.workflow import WorkflowGraph, WorkflowNode, WorkflowEdge
from memory.shared_memory import SharedMemory
from runtime.agent_context import AgentContext
from tools.calculator_tool import CalculatorTool
from workflows.investment_state import InvestmentState
from workflows.nodes import research_node, analysis_node, report_node

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

    # result = await agent.run(
    #     "What is 25 * 48 + 1024?"
    # )
    #
    # print(result)
    async for event in agent.run_stream(
        "Explain momentum investing"
    ):
        print(event.model_dump())
        # if event.type == "token":
        #     print(event.data["token"],
        #           end="",
        #           flush=True)


# asyncio.run(main())

# 组装workflow
async def build_workflow():
    graph = WorkflowGraph()

    graph.add_node(
        WorkflowNode(
            "research",
            research_node
        )
    )

    graph.add_node(
        WorkflowNode(
            "analysis",
            analysis_node
        )
    )

    graph.add_node(
        WorkflowNode(
            "report",
            report_node
        )
    )

    graph.add_edge(
        WorkflowEdge(
            "research",
            "analysis"
        )
    )

    graph.add_edge(
        WorkflowEdge(
            "analysis",
            "report"
        )
    )

    graph.set_start("research")

    state = InvestmentState(
        query="Should I invest in NVIDIA?"
    )

    agent_context = AgentContext(
        state=state,
        shared_memory=SharedMemory()
    )

    result = await graph.run(state)

    print(result.final_report)

asyncio.run(build_workflow())