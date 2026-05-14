class HookManager:

    def __init__(self):

        self.hooks = {}

    def register(
        self,
        event_name,
        fn
    ):

        self.hooks.setdefault(
            event_name,
            []
        ).append(fn)

    async def trigger(
        self,
        event_name,
        *args,
        **kwargs
    ):

        for fn in self.hooks.get(
            event_name,
            []
        ):

            await fn(
                *args,
                **kwargs
            )