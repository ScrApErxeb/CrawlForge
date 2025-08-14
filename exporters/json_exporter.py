import json
from pathlib import Path
from typing import Any, Dict

class JSONExporter:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def export(self, data: Dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
