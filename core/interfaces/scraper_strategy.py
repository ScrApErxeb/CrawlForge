from abc import ABC, abstractmethod

class IScraperStrategy(ABC):
    @abstractmethod
    def fetch(self, url: str) -> str:
        """Retourne le HTML brut (ou contenu) de l'URL."""
        raise NotImplementedError
