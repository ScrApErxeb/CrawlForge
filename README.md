# CrawlForge

**CrawlForge** est un framework de scraping web modulaire, flexible et extensible, conçu pour respecter les principes **SOLID**, les **design patterns** et une **architecture logicielle propre**.

## 🚀 Fonctionnalités
- **Architecture modulaire** : facile à étendre avec de nouvelles stratégies (BS4, Selenium, API…)
- **Respect de SOLID** : code maintenable et évolutif
- **Multiples sorties** : export vers CSV, JSON, bases de données, etc.
- **Parsers interchangeables** : HTML, JSON, XML…
- **Tests unitaires** intégrés dès le départ

## 🏗 Architecture du projet
CrawlForge/
│
├── core/ # Cœur métier
│ ├── interfaces/ # Interfaces (Strategy, Parser, Exporter)
│ ├── services/ # Services principaux
│ ├── models/ # Modèles de données
│ └── exceptions.py # Exceptions custom
│
├── strategies/ # Méthodes de scraping (BS4, Selenium…)
├── parsers/ # Différents parseurs
├── exporters/ # Exporteurs (CSV, JSON, DB…)
├── config/ # Configurations
├── tests/ # Tests unitaires et d'intégration
└── main.py # Point d’entrée

bash
Copy code

## 📦 Installation
```bash
git clone https://github.com/<ton_user>/CrawlForge.git
cd CrawlForge
pip install -r requirements.txt
🔧 Utilisation simple
python
Copy code
from strategies.bs4_scraper import BeautifulSoupScraper
from parsers.html_parser import HTMLParser
from exporters.csv_exporter import CSVExporter
from core.services.scraper_service import ScraperService

scraper = ScraperService(
    scraper_strategy=BeautifulSoupScraper(),
    parser=HTMLParser(),
    exporter=CSVExporter("output.csv")
)

scraper.run("https://example.com")
🧪 Tests
bash
Copy code
pytest
🤝 Contribution
Les contributions sont les bienvenues !

Forkez le projet

Créez votre branche (git checkout -b feature/ma-feature)

Committez (git commit -m 'Ajout de ma feature')

Poussez (git push origin feature/ma-feature)

Ouvrez une Pull Request

📜 Licence
MIT License
