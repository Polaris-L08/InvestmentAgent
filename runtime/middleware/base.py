from abc import ABC
from abc import abstractmethod


class Middleware(ABC):

    @abstractmethod
    async def process(
        self,
        context,
        next_handler
    ):
        pass