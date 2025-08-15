from parsers.html_parser_base import HTMLParserBase
from bs4 import BeautifulSoup
from typing import Dict, Any, List

class WikipediaParser(HTMLParserBase):
    """Parser spécifique pour Wikipedia FR"""
    def __init__(self, headings: List[str] = None):
        self.headings_to_extract = headings or ["h1", "h2", "h3"]

    def parse(self, raw: str) -> Dict[str, Any]:
        soup = BeautifulSoup(raw, "html.parser")
        result = super().parse(raw)

        # H2/H3 spécifiques Wikipedia
        def extract_wiki_headings(level: str):
            headings = []
            for h in soup.find_all(level):
                # priorité sur mw-headline
                span = h.find("span", class_="mw-headline")
                if span and span.get_text(strip=True):
                    headings.append(span.get_text(strip=True))
                else:
                    # sinon texte direct du h2
                    text = h.get_text(strip=True)
                    if text:
                        headings.append(text)
            return headings

        result["headings"]["h2"] = extract_wiki_headings("h2")
        result["headings"]["h3"] = extract_wiki_headings("h3")
        return result
