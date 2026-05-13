import numpy as np


class InMemoryVectorStore:

    def __init__(self):

        self.vectors = []

    def add(
        self,
        chunk,
        embedding
    ):

        self.vectors.append({
            "chunk": chunk,
            "embedding": embedding
        })

    def similarity(
        self,
        a,
        b
    ):

        a = np.array(a)
        b = np.array(b)

        return (
            np.dot(a, b)
            /
            (
                np.linalg.norm(a)
                *
                np.linalg.norm(b)
            )
        )

    def search(
        self,
        query_embedding,
        top_k=3
    ):

        scored = []

        for item in self.vectors:

            score = self.similarity(
                query_embedding,
                item["embedding"]
            )

            scored.append(
                (score, item["chunk"])
            )

        scored.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        return scored[:top_k]