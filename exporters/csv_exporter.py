# exporters/csv_exporter.py
import csv

class CSVExporter:
    def __init__(self, filename):
        self.filename = filename

    def export(self, data):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(data.keys())
            writer.writerow(data.values())
