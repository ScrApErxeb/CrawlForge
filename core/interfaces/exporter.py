from abc import ABC, abstractmethod
from typing import Any, Dict

class IExporter(ABC):
    @abstractmethod
    def export(self, data: Dict[str, Any]) -> None:
        """Exporte les données (CSV, JSON, DB, etc.)."""
        raise NotImplementedError
