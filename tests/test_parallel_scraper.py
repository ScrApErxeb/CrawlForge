import pytest
from parsers.html_parser_base import HTMLParserBase
from exporters.multi_exporter import MultiExporter
from strategies.parallel_scraper import ParallelScraper
from pathlib import Path

def test_parallel_scraper(tmp_path):
    urls = [
        "https://python.land/virtual-environments/virtualenv",
        "https://fr.wikipedia.org/wiki/Esthétique"
    ]
    csv_file = tmp_path / "parallel.csv"
    json_file = tmp_path / "parallel.json"
    exporter = MultiExporter(csv_file, json_file)

    scraper = ParallelScraper(
        urls=urls,
        parser=HTMLParserBase(),
        exporter=exporter,
        use_selenium=False,
        max_concurrent=2,
        cache_dir=tmp_path / "cache"
    )

    import asyncio
    results = asyncio.run(scraper.run_all())

    assert len(results) == len(urls)
    for r in results:
        assert "title" in r
        assert "headings" in r
