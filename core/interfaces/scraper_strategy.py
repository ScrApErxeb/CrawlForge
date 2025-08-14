from abc import ABC, abstractmethod

class IScraperStrategy(ABC):
    @abstractmethod
    def fetch(self, url: str) -> str:
        pass