from pydantic import BaseModel


class EvaluationResult(BaseModel):

    passed: bool

    score: float

    issues: list[str]