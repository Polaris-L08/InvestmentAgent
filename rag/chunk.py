from pydantic import BaseModel


class Chunk(BaseModel):
    """
    A chunk of text from a document.
    """

    id: str

    document_id: str

    content: str

    metadata: dict = {}