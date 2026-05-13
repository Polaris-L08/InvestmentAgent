class Retriever:

    def __init__(
        self,
        embedder,
        vector_store
    ):

        self.embedder = embedder

        self.vector_store = vector_store

    async def retrieve(
        self,
        query: str,
        top_k=3
    ):

        query_embedding = (
            await self.embedder.embed(
                query
            )
        )

        return self.vector_store.search(
            query_embedding,
            top_k
        )
