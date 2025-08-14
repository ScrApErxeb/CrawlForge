import csv
from pathlib import Path
from typing import Dict, Any

class CSVExporter:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def export(self, data: Dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(data.keys()))
            writer.writeheader()
            writer.writerow(data)
