import requests
from core.interfaces.scraper_strategy import IScraperStrategy

class BeautifulSoupScraper(IScraperStrategy):
    def __init__(self, timeout: int = 15, headers: dict | None = None) -> None:
        self.timeout = timeout
        self.headers = headers or {"User-Agent": "CrawlForge/0.1 (+https://github.com/your-user/CrawlForge)"}

    def fetch(self, url: str) -> str:
        resp = requests.get(url, timeout=self.timeout, headers=self.headers)
        resp.raise_for_status()
        return resp.text
