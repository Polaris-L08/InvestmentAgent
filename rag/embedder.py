from openai import AsyncOpenAI


class OpenAIEmbedder:

    def __init__(
        self,
        api_key,
        model="text-embedding-v1"
    ):

        self.client = AsyncOpenAI(
            api_key=api_key
        )

        self.model = model

    async def embed(
        self,
        text: str
    ):

        response = (
            await self.client.embeddings.create(
                model=self.model,
                input=text,
                dimensions=1536
            )
        )

        return (
            response
            .data[0]
            .embedding
        )