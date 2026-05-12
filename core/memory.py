from core.messages import Message


class MemoryManager:

    def __init__(
        self,
        max_messages: int = 20
    ):

        self.max_messages = max_messages

    def score_message(
            self,
            message: Message
    ) -> float:
        """
        Scores a message based on its content.
        """
        score = 0
        if message.role == "system":
            score += 100
        if message.role == "tool":
            score += 2

        if len(message.content) > 500:
            score -= 1

        importance = (
            message.metadata.get(
                "importance",
                0
            )
        )

        score += importance
        return score

    def trim_messages(
        self,
        messages: list[Message]
    ) -> list[Message]:
        """
        Trims the messages to the maximum number of messages.
        """

        if len(messages) <= self.max_messages:
            return messages

        # 构建【Score each message】列表
        scored = [
            (
                self.score_message(m),
                i,
                m
            )
            for i,m in enumerate(messages)
        ]

        #
        scored.sort(
            key=lambda x: x[0],
            reverse=True
        )

        # 取指定数量的消息
        selected = scored[:self.max_messages]
        # 按索引排序（还原顺序）
        selected.sort(
            key=lambda x: x[1]
        )
        # 返回消息
        return [x[2] for x in selected]