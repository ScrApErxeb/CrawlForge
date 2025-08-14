# CrawlForge 🚀

CrawlForge est un **scraper web modulaire et flexible** écrit en Python, respectant les principes SOLID et une architecture extensible.  
Il permet d’extraire les informations principales d’une page web (title, meta description, headings) et de les exporter en **CSV et JSON** simultanément.  

---

## Features

- Extraction de `title`, `meta description`, H1/H2/H3
- Export CSV + JSON simultanément
- Parser modulable : générique ou spécifique (Wikipedia FR)
- Logger centralisé (console + fichier)
- CLI simple et efficace

---

## Installation

```bash
git clone https://github.com/ScrApErxeb/CrawlForge.git
cd CrawlForge
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
