import logging
from pathlib import Path

class LoggerService:
    def __init__(self, log_file: str | Path = "crawlforge.log"):
        self.logger = logging.getLogger("CrawlForge")
        self.logger.setLevel(logging.INFO)

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch_formatter = logging.Formatter("[%(levelname)s] %(message)s")
        ch.setFormatter(ch_formatter)

        # File handler
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        fh.setFormatter(fh_formatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger
