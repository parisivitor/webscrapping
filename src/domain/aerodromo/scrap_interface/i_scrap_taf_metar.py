from abc import ABC, abstractmethod
from typing import List

class IScrapTafMetar(ABC):
    @abstractmethod
    def get_taf_metar(input: str) -> List:
        pass
