from abc import ABC, abstractmethod
from typing import List

class IScrapCarta(ABC):
    @abstractmethod
    def get_cartas(self, input: str) -> List:
        pass
