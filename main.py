import argparse
from datetime import datetime
from pathlib import Path
from parsers.html_parser_base import HTMLParserBase
from parsers.wikipedia_parser import WikipediaParser
from exporters.multi_exporter import MultiExporter
from strategies.parallel_scraper import ParallelScraper

def main():
    parser = argparse.ArgumentParser(description="CrawlForge V1.2 - parallel scraping & cache")
    parser.add_argument("urls", nargs="+", help="URLs à scraper")
    parser.add_argument("--out", default="output/output", help="Préfixe pour CSV/JSON")
    parser.add_argument("--wiki", action="store_true", help="Parser spécifique Wikipedia")
    parser.add_argument("--selenium", action="store_true", help="Activer Selenium pour pages dynamiques")
    parser.add_argument("--max", type=int, default=5, help="Nombre de scrapes simultanés")
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    Path("output").mkdir(parents=True, exist_ok=True)
    csv_path = f"{args.out}_{timestamp}.csv"
    json_path = f"{args.out}_{timestamp}.json"

    parser_cls = WikipediaParser if args.wiki else HTMLParserBase
    exporter = MultiExporter(csv_path, json_path)

    scraper = ParallelScraper(
        urls=args.urls,
        parser=parser_cls(),
        exporter=exporter,
        use_selenium=args.selenium,
        max_concurrent=args.max
    )

    import asyncio
    asyncio.run(scraper.run_all())

if __name__ == "__main__":
    main()
