class ReflectionRuntime:

    def __init__(
            self,
            generator_agent,
            critic_agent,
            reflection_memory
    ):

        self.generator = (
            generator_agent
        )

        self.critic = (
            critic_agent
        )

        self.memory = (
            reflection_memory
        )

    async def run(
            self,
            task: str,
            max_retry=3
    ):

        # feedback = ""

        for i in range(max_retry):

            answer = await (
                self.generator.run(task)
            )

            critique = await (
                self.critic.critique(
                    answer
                )
            )

            evaluation = await (
                self.critic.evaluate(
                    answer
                )
            )

            if evaluation.passed:
                return answer

            # feedback = (
            #         "\nFix these issues:\n"
            #         + "\n".join(evaluation.issues)
            # )
            task += f"""

                        Previous critique:
                        {critique}

                        Fix the issues above.
                        """

        return answer
