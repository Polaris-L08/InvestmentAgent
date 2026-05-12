import json

from core.events import RuntimeEvent
from core.messages import Message
from core.state import AgentState
from core.tool_validator import ToolValidator


class SimpleAgent:

    def __init__(
        self,
        llm_client,
        tool_registry,
        memory_manager
    ):
        self.llm = llm_client
        self.tool_registry = tool_registry
        self.memory_manager = memory_manager

    def emit_event(self,
                   event_type,
                   data):
        event = RuntimeEvent(
            type=event_type,
            data=data
        )
        print(event.model_dump_json())

    async def run(self, user_input: str):

        state = AgentState()

        state.messages.extend([
            Message(
                role="system",
                content="You are a helpful AI investment assistant."
            ),
            Message(
                role="user",
                content=user_input
            )
        ])

        tool_validator = ToolValidator()

        while not state.finished:

            # Iteration Protection
            if state.iteration_count >= state.max_iterations:
                state.error = (
                    "Max iterations exceeded"
                )
                break

            state.iteration_count += 1

            self.emit_event(
                "llm_start",
                {
                    "iteration": state.iteration_count
                }
            )

            try:
                trimmed_messages  = self.memory_manager.trim_messages(state.messages)

                response = await self.llm.chat(
                    messages=trimmed_messages ,
                    tools=self.tool_registry.get_tool_schemas()
                )

                msg = response.choices[0].message

                # Tool Calling
                if msg.tool_calls:

                    state.messages.append(
                        Message(
                            role="assistant",
                            content=msg.content or ""
                        )
                    )

                    for tool_call in msg.tool_calls:

                        tool_name = tool_call.function.name

                        args = json.loads(
                            tool_call.function.arguments
                        )

                        tool = self.tool_registry.get_tool(
                            tool_name
                        )

                        if not tool:
                            continue

                        self.emit_event(
                            "tool_start",
                            {
                                "tool": tool_name,
                                "args": args
                            }
                        )

                        # Tool Parameter Validation
                        tool_validator.validate(
                            tool,
                            args
                        )
                        result = await tool.run(**args)

                        self.emit_event(
                            "tool_end",
                            {
                                "tool": tool_name,
                                "success": result.success
                            }
                        )

                        if result.success:
                            tool_content = str(result.content)
                        else:
                            tool_content = f"Tool Error: {result.error}"

                        state.messages.append(
                            Message(
                                role="tool",
                                content=tool_content,
                                tool_call_id=tool_call.id,
                                name=tool_name
                            )
                        )

                    continue

                # Final Answer
                state.finished = True
                return msg.content
            except Exception as e:
                state.error = str(e)
                self.emit_event(
                    "runtime_error",
                    {
                        "error": str(e)
                    }
                )
                break
        return f"Agent failed: {state.error}"