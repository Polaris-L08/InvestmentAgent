from openai import OpenAI
from core.messages import Message


class LLMClient:

    def __init__(self, api_key: str, model: str):

        self.model = model

        self.client = OpenAI(
            api_key=api_key
        )

    def chat(self, messages, tools=None):

        response = self.client.chat.completions.create(
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

        return response