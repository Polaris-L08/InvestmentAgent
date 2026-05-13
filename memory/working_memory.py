class WorkingMemory:
    """
    当前认知空间
        当前任务
        当前工具结果
        当前推理链
    """

    def __init__(
        self,
        max_items=10
    ):

        self.max_items = max_items

        self.items = []

    def add(
        self,
        memory_item
    ):

        self.items.append(memory_item)

        if len(self.items) > self.max_items:

            self.items.pop(0)

    def get_all(self):

        return self.items