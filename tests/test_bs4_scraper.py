def test_bs4_scraper():
    from strategies.bs4_scraper import BeautifulSoupScraper
    scraper = BeautifulSoupScraper()
    html = scraper.fetch("https://python.land")
    assert "<html" in html

def test_selenium_scraper():
    from strategies.selenium_scraper import SeleniumScraper
    scraper = SeleniumScraper(headless=True)
    html = scraper.fetch("https://python.land")
    assert "<html" in html
    scraper.close()
