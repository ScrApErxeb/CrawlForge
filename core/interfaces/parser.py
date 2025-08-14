from abc import ABC, abstractmethod
from typing import Any, Dict

class IParser(ABC):
    @abstractmethod
    def parse(self, raw: str) -> Dict[str, Any]:
        """Transforme le contenu brut en données structurées."""
        raise NotImplementedError
