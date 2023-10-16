from abc import ABC, abstractmethod
from typing import List

class IScrapTafMetar(ABC):
    @abstractmethod
    def get_taf_metar(self, input: str) -> List:
        pass
