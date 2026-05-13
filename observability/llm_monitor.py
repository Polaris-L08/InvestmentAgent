class LLMMonitor:

    def track(
        self,
        prompt_tokens,
        completion_tokens,
        latency
    ):

        total = (
            prompt_tokens
            + completion_tokens
        )

        return {
            "prompt_tokens":
                prompt_tokens,

            "completion_tokens":
                completion_tokens,

            "total_tokens":
                total,

            "latency":
                latency
        }