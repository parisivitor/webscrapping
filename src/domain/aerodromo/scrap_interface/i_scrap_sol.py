from abc import ABC, abstractmethod
from typing import List

class IScrapSol(ABC):
    @abstractmethod
    def get_hour_sunset_sunrise(input: str) -> List:
        pass
