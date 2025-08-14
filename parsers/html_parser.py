# parsers/html_parser.py
from bs4 import BeautifulSoup

class HTMLParser:
    def parse(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        return {"title": soup.title.string if soup.title else None}
