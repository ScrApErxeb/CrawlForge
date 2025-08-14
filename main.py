import argparse
from strategies.bs4_scraper import BeautifulSoupScraper
from parsers.html_parser import HTMLParser
from exporters.csv_exporter import CSVExporter
from core.services.scraper_service import ScraperService

def main() -> None:
    parser = argparse.ArgumentParser(description="CrawlForge - minimal run")
    parser.add_argument("url", help="URL à scraper")
    parser.add_argument("--out", default="output/output.csv", help="Fichier CSV de sortie")
    args = parser.parse_args()

    service = ScraperService(
        scraper_strategy=BeautifulSoupScraper(),
        parser=HTMLParser(),
        exporter=CSVExporter(args.out)
    )
    service.run(args.url)
    print(f"✅ Export terminé -> {args.out}")

if __name__ == "__main__":
    main()
