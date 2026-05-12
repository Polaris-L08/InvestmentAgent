
class ToolValidator:
    """
    Validates tool arguments.
    """

    def validate(
        self,
        tool,
        args: dict
    ):

        for p in tool.parameters:

            if (
                p.required
                and p.name not in args
            ):

                raise ValueError(
                    f"Missing parameter: {p.name}"
                )