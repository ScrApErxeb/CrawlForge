# html_parser.py
from bs4 import BeautifulSoup
from typing import Dict, Any
from parsers.html_parser_base import HTMLParserBase

class HTMLParser(HTMLParserBase):
    """Parser HTML avec support mw-headline style Wikipedia"""
    def parse(self, raw: str) -> Dict[str, Any]:
        base_result = super().parse(raw)
        soup = BeautifulSoup(raw, "html.parser")

        def extract_headings(level: str):
            result = []
            for h in soup.find_all(level):
                span = h.find("span", class_="mw-headline")
                if span and span.get_text(strip=True):
                    result.append(span.get_text(strip=True))
            return result

        base_result["headings"]["h2"] = extract_headings("h2")
        base_result["headings"]["h3"] = extract_headings("h3")
        return base_result