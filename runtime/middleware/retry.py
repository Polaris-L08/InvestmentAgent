from runtime.middleware.base import Middleware


class RetryMiddleware(Middleware):

    def __init__(
        self,
        retry_policy
    ):

        self.retry_policy = (
            retry_policy
        )

    async def process(
        self,
        context,
        next_handler
    ):

        return await (
            self.retry_policy.execute(
                lambda:
                    next_handler(context)
            )
        )