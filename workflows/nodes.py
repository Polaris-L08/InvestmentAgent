async def research_node(
    state
):

    state.news = (
        f"Research result for: {state.query}"
    )

    return state

async def analysis_node(
    state
):

    state.analysis = (
        f"Analysis based on: {state.news}"
    )

    return state

async def report_node(
    state
):

    state.final_report = f"""
    Query:
    {state.query}

    News:
    {state.news}

    Analysis:
    {state.analysis}
    """

    return state