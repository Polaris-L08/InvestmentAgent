from runtime.middleware.base import Middleware


class MiddlewarePipeline:

    def __init__(self):

        self.middlewares: list[Middleware] = []

    def add(
        self,
        middleware
    ):

        self.middlewares.append(
            middleware
        )

    async def execute(
        self,
        context,
        final_handler
    ):

        async def call_next(index):

            if index == len(
                self.middlewares
            ):

                return await final_handler(
                    context
                )

            middleware = (
                self.middlewares[index]
            )

            return await middleware.process(
                context,
                lambda ctx:
                    call_next(index + 1)
            )

        return await call_next(0)