from rag.chunk import Chunk

"""
教学版Chunker
真实工业级Chunker是Semantic Chunking
    按段落
    按标题
    按章节
    按语义边界
"""
class SimpleChunker:

    def chunk(
        self,
        document,
        chunk_size=500
    ):

        chunks = []

        text = document.content

        for i in range(
            0,
            len(text),
            chunk_size
        ):

            chunk_text = (
                text[i:i+chunk_size]
            )

            chunks.append(
                Chunk(
                    id=f"{document.id}_{i}",
                    document_id=document.id,
                    content=chunk_text,
                    metadata=document.metadata
                )
            )

        return chunks