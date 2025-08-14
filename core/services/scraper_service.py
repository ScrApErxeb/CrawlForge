class ScraperService:
    def __init__(self, scraper_strategy, parser, exporter):
        self.scraper_strategy = scraper_strategy
        self.parser = parser
        self.exporter = exporter

    def run(self, url: str):
        raw_data = self.scraper_strategy.fetch(url)
        parsed_data = self.parser.parse(raw_data)
        self.exporter.export(parsed_data)
        