from workflows.workflow_base_state import WorkflowBaseState


class InvestmentState(WorkflowBaseState):

    query: str

    news: str = ""

    analysis: str = ""

    risk: str = ""

    final_report: str = ""