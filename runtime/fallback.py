class FallbackModel:

    def __init__(
        self,
        primary_model,
        backup_model
    ):

        self.primary = primary_model

        self.backup = backup_model

    async def generate(
        self,
        prompt
    ):

        try:

            return await (
                self.primary.generate(
                    prompt
                )
            )

        except Exception:

            return await (
                self.backup.generate(
                    prompt
                )
            )