import argparse
from datetime import datetime
from strategies.bs4_scraper import BeautifulSoupScraper
from parsers.html_parser_base import HTMLParserBase
from parsers.wikipedia_parser import WikipediaParser
from exporters.multi_exporter import MultiExporter
from core.services.scraper_service import ScraperService
from core.services.logger_service import LoggerService
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="CrawlForge - modular web scraper")
    parser.add_argument("url", help="URL à scraper")
    parser.add_argument("--out", default="output/output", help="Préfixe pour CSV/JSON")
    parser.add_argument("--wiki", action="store_true", help="Parser spécifique Wikipedia")
    args = parser.parse_args()

    logger = LoggerService().get_logger()
    logger.info(f"Démarrage scraping : {args.url}")

    # Génération de fichiers uniques avec timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    Path("output").mkdir(parents=True, exist_ok=True)
    csv_path = f"{args.out}_{timestamp}.csv"
    json_path = f"{args.out}_{timestamp}.json"

    parser_cls = WikipediaParser if args.wiki else HTMLParserBase
    scraper_service = ScraperService(
        scraper_strategy=BeautifulSoupScraper(),
        parser=parser_cls(),
        exporter=MultiExporter(csv_path, json_path)
    )

    scraper_service.run(args.url)
    logger.info(f"Scraping terminé -> {csv_path} + {json_path}")

if __name__ == "__main__":
    main()
