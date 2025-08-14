from bs4 import BeautifulSoup
from typing import Dict, Any

class HTMLParserBase:
    """Parser générique pour sites HTML"""
    def parse(self, raw: str) -> Dict[str, Any]:
        soup = BeautifulSoup(raw, "html.parser")

        title = soup.title.string.strip() if soup.title and soup.title.string else ""
        meta_desc_tag = soup.find("meta", attrs={"name": "description"})
        meta_desc = meta_desc_tag["content"].strip() if meta_desc_tag and "content" in meta_desc_tag.attrs else ""
        if not meta_desc:
            # fallback premier paragraphe
            p = soup.find("p")
            if p and p.get_text(strip=True):
                meta_desc = p.get_text(strip=True)

        headings = {
            "h1": [h.get_text(strip=True) for h in soup.find_all("h1")],
            "h2": [h.get_text(strip=True) for h in soup.find_all("h2")],
            "h3": [h.get_text(strip=True) for h in soup.find_all("h3")],
        }

        return {
            "title": title,
            "meta_description": meta_desc,
            "headings": headings
        }
