from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class SeleniumScraper:
    def __init__(self, headless=True, timeout=10):
        self.timeout = timeout
        options = Options()
        if headless:
            options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def fetch(self, url):
        self.driver.get(url)
        time.sleep(2)  # petit wait pour JS simple
        return self.driver.page_source

    def close(self):
        self.driver.quit()
