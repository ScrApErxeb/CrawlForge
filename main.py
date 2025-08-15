import argparse
import asyncio
from pathlib import Path
from strategies.parallel_scraper import ParallelScraper
from parsers.wikipedia_parser import WikipediaParser
from exporters.multi_exporter import MultiExporter
import logging
from datetime import datetime

# --- Logging ---
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger("CrawlForge")

# --- Arguments CLI ---
parser = argparse.ArgumentParser(description="CrawlForge V1.3 - Parallel Web Scraper")
parser.add_argument("urls", nargs="+", help="Liste des URLs à scraper")
parser.add_argument("--out", default="output/", help="Répertoire de sortie")
parser.add_argument("--max", type=int, default=5, help="Nombre max de tâches parallèles")
parser.add_argument("--strategy", choices=["auto", "bs4", "selenium"], default="auto")
parser.add_argument("--headings", default="h1,h2,h3", help="Balises à récupérer")
args = parser.parse_args()

# --- Préparation paths ---
out_dir = Path(args.out)
out_dir.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_path = out_dir / f"crawl_{timestamp}.csv"
json_path = out_dir / f"crawl_{timestamp}.json"

# --- Exporter ---
exporter = MultiExporter(str(csv_path), str(json_path))

# --- Parser ---
parser_obj = WikipediaParser(headings=args.headings.split(","))

# --- Scraper ---
use_selenium = args.strategy in ["selenium", "auto"]
scraper = ParallelScraper(
    urls=args.urls,
    parser=parser_obj,
    exporter=exporter,
    use_selenium=use_selenium,
    max_concurrent=args.max,
    cache_dir="cache/"
)

# --- Run ---
asyncio.run(scraper.run_all())
logger.info(f"Scraping terminé pour {len(args.urls)} URLs -> CSV: {csv_path} | JSON: {json_path}")
