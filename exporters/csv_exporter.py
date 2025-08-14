import csv
from pathlib import Path
from typing import Dict, Any

class CSVExporter:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def export(self, data: Dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)

        # Récupération des headings et transformation en string
        headings = data.get("headings", {})
        h1 = " | ".join(headings.get("h1", []))
        h2 = " | ".join(headings.get("h2", []))
        h3 = " | ".join(headings.get("h3", []))

        # Gestion None pour meta_description
        meta_description = data.get("meta_description") or ""

        # Écriture CSV
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "meta_description", "h1", "h2", "h3"])
            writer.writerow([
                data.get("title") or "",
                meta_description,
                h1,
                h2,
                h3
            ])
