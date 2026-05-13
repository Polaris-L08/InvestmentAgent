from agents.base_agent import BaseAgent
from evaluation.evaluation_result import EvaluationResult


class CriticAgent(BaseAgent):

    async def critique(
        self,
        answer: str
    ):

        critique = f"""
        Review the following answer
        and identify problems:

        {answer}
        """

        return critique

    async def evaluate(
            self,
            answer: str
    ):
        issues = []

        if len(answer) < 50:
            issues.append("Answer is too short")

        score = 1.0

        if issues:
            score -= 0.5

        return EvaluationResult(
            passed=(score > 0.7),
            score=score,
            issues=issues
        )
