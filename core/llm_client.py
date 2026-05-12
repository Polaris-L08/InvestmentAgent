import os

import httpx
from openai import OpenAI, AsyncOpenAI
from core.messages import Message


class LLMClient:

    def __init__(self, api_key: str|None, model: str|None, url: str|None, timeout: int = 60):
        self.model = os.getenv("LLM_MODEL_ID")

        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url=url,
            timeout=timeout
        )

    async def chat(self, messages, tools=None):
        response = (
            await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": m.role,
                        "content": m.content
                    }
                    for m in messages
                ],
                tools=tools
            )
        )

        return response

    async def stream_chat(
            self,
            messages,
            tools=None
    ):
        stream = (
            await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": m.role,
                        "content": m.content
                    }
                    for m in messages
                ],
                tools=tools,
                stream=True
            )
        )

        async for chunk in stream:
            yield chunk
