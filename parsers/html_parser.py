from bs4 import BeautifulSoup
from typing import Dict, Any

class HTMLParser:
    def parse(self, raw: str) -> Dict[str, Any]:
        soup = BeautifulSoup(raw, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else None
        h1 = soup.find("h1")
        return {
            "title": title,
            "h1": h1.get_text(strip=True) if h1 else None,
        }
