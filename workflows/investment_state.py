from pydantic import BaseModel


class InvestmentState(BaseModel):

    query: str

    news: str = ""

    analysis: str = ""

    risk: str = ""

    final_report: str = ""