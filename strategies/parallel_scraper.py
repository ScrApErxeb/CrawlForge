import logging
import asyncio
import aiohttp
from strategies.bs4_scraper import BeautifulSoupScraper
from strategies.selenium_scraper import SeleniumScraper
from pathlib import Path
import hashlib
import json

# -------------------- Logger --------------------
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger("CrawlForge")

# -------------------- ParallelScraper --------------------
class ParallelScraper:
    def __init__(self, urls, parser, exporter, use_selenium=False, max_concurrent=5, cache_dir="cache/"):
        self.urls = urls
        self.parser = parser
        self.exporter = exporter
        self.use_selenium = use_selenium
        self.max_concurrent = max_concurrent
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cache_path(self, url):
        h = hashlib.md5(url.encode()).hexdigest()
        return self.cache_dir / f"{h}.json"

    async def _fetch_aiohttp(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def _scrape_bs4(self, url):
        cache_file = self._get_cache_path(url)
        if cache_file.exists():
            logger.info(f"Cache found, skipping scrape: {url}")
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)

        logger.info(f"Fetching with aiohttp: {url}")
        async with aiohttp.ClientSession() as session:
            html = await self._fetch_aiohttp(session, url)
        data = self.parser.parse(html)
        self.exporter.export(data)

        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return data

    async def _scrape_selenium(self, url):
        from asyncio import to_thread
        scraper = SeleniumScraper(headless=True)
        logger.info(f"Fetching with Selenium: {url}")
        html = await to_thread(scraper.fetch, url)
        data = self.parser.parse(html)
        self.exporter.export(data)
        scraper.close()
        return data

    async def _worker(self, url):
        logger.info(f"Start scraping: {url}")
        if self.use_selenium:
            data = await self._scrape_selenium(url)
        else:
            data = await self._scrape_bs4(url)
        logger.info(f"Done scraping: {url}")
        return data

    async def run_all(self):
        semaphore = asyncio.Semaphore(self.max_concurrent)

        async def sem_worker(url):
            async with semaphore:
                return await self._worker(url)

        results = await asyncio.gather(*[sem_worker(url) for url in self.urls])
        
        # Export final unique JSON/CSV pour toutes les URLs
        self.exporter.export_all(results)
        
        logger.info(f"All {len(results)} URLs scraped successfully")
        return results
