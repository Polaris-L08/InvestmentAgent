from pydantic import BaseModel

"""
因为LLM的输出不稳定，Tool System必须成为LLM和代码之间的”安全边界“
"""
class ToolParameter(BaseModel):

    name: str

    type: str

    description: str

    required: bool = True