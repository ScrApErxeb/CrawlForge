from bs4 import BeautifulSoup
from typing import Dict, Any

class HTMLParser:
    def parse(self, raw: str) -> Dict[str, Any]:
        soup = BeautifulSoup(raw, "html.parser")

        title = soup.title.string.strip() if soup.title and soup.title.string else ""

        # Meta description fallback
        meta_desc = ""
        tag = soup.find("meta", attrs={"name": "description"})
        if tag and "content" in tag.attrs:
            meta_desc = tag["content"].strip()
        else:
            # fallback sur premier paragraphe
            p = soup.find("p")
            if p and p.get_text(strip=True):
                meta_desc = p.get_text(strip=True)

        # Headings
        def extract_headings(level: str):
            headings = []
            for h in soup.find_all(level):
                span = h.find("span", class_="mw-headline")
                if span and span.get_text(strip=True):
                    headings.append(span.get_text(strip=True))
            return headings

        headings = {
            "h1": [h.get_text(strip=True) for h in soup.find_all("h1")],
            "h2": extract_headings("h2"),
            "h3": extract_headings("h3")
        }

        return {
            "title": title,
            "meta_description": meta_desc,
            "headings": headings
        }
