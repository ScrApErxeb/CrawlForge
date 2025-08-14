from exporters.csv_exporter import CSVExporter
from exporters.json_exporter import JSONExporter
from typing import Dict, Any

class MultiExporter:
    """Export CSV + JSON en un seul run"""
    def __init__(self, csv_path: str, json_path: str):
        self.csv = CSVExporter(csv_path)
        self.json = JSONExporter(json_path)

    def export(self, data: Dict[str, Any]):
        self.csv.export(data)
        self.json.export(data)
