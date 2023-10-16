from abc import ABC, abstractmethod
from typing import List

class IScrapCarta(ABC):
    @abstractmethod
    def get_cartas(input: str) -> List:
        pass
