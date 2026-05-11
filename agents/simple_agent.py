import json

from core.messages import Message


class SimpleAgent:

    def __init__(
        self,
        llm_client,
        tool_registry
    ):
        self.llm = llm_client
        self.tool_registry = tool_registry

    def run(self, user_input: str):

        messages = [
            Message(
                role="system",
                content="You are a helpful AI investment assistant."
            ),
            Message(
                role="user",
                content=user_input
            )
        ]

        while True:

            response = self.llm.chat(
                messages=messages,
                tools=self.tool_registry.get_tool_schemas()
            )

            msg = response.choices[0].message

            # 1. Tool Calling
            if msg.tool_calls:

                messages.append(
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

                    result = tool.run(**args)

                    messages.append(
                        Message(
                            role="tool",
                            content=str(result),
                            tool_call_id=tool_call.id,
                            name=tool_name
                        )
                    )

                continue

            # 2. Final Answer
            return msg.content