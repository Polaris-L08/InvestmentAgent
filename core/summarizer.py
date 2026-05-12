class SimpleSummarizer:
    """"
    A simple summarizer that truncates the content to a given length.
    """

    def summarize(
        self,
        content: str,
        max_length: int = 500
    ):

        if len(content) <= max_length:
            return content

        return (
            content[:max_length]
            + "..."
        )