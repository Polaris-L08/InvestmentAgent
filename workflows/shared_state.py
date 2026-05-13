from pydantic import BaseModel, Field


class SharedState(BaseModel):
    query: str

    plan: list[str] = Field(default_factory=list)

    research_result: str = ""

    quant_result: str = ""

    risk_result: str = ""

    final_report: str = ""