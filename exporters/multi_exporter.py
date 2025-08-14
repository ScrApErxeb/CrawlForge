from exporters.csv_exporter import CSVExporter
from exporters.json_exporter import JSONExporter
from typing import Dict, Any, List

class MultiExporter:
    """Export CSV + JSON en un seul run"""
    def __init__(self, csv_path: str, json_path: str):
        self.csv = CSVExporter(csv_path)
        self.json = JSONExporter(json_path)

    def export(self, data: Dict[str, Any]):
        self.csv.export(data)
        self.json.export(data)

    def export_all(self, results: List[Dict[str, Any]]):
        """Export toutes les URLs en un seul CSV et JSON"""
        # JSON
        import json
        with open(self.json.path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        # CSV
        import pandas as pd
        rows = []
        for data in results:
            row = {
                "title": data.get("title", ""),
                "meta_description": data.get("meta_description", ""),
                "h1": " | ".join(data.get("headings", {}).get("h1", [])),
                "h2": " | ".join(data.get("headings", {}).get("h2", [])),
                "h3": " | ".join(data.get("headings", {}).get("h3", [])),
            }
            rows.append(row)
        df = pd.DataFrame(rows)
        df.to_csv(self.csv.path, index=False, encoding="utf-8")
