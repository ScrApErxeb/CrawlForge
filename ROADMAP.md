# CrawlForge V1.1 Roadmap 🚀

## Objectif
Améliorer les performances, la compatibilité multi-sites et ajouter des fonctionnalités avancées tout en gardant la modularité et la flexibilité de la V1.0.

---

## 1️⃣ Scraping avancé
- Selenium / Playwright pour pages dynamiques (JavaScript)
- Gestion des timeouts et retries pour pages lentes ou instables
- Rotation de User-Agent et respect du `robots.txt`

---

## 2️⃣ Performance
- Multi-threading / Asyncio pour scraper plusieurs URLs en parallèle
- Pool de sessions HTTP pour limiter le temps de connexion
- Cache local des pages pour éviter de scraper plusieurs fois la même URL

---

## 3️⃣ Parsers spécifiques
- Extensions pour sites particuliers :
  - Blogs (WordPress, Medium…)
  - E-commerce (Amazon, Shopify…)
  - Wikipédia déjà intégré
- Système de fallback générique pour tous les sites non reconnus

---

## 4️⃣ Export amélioré
- Export vers base de données (SQLite / PostgreSQL)
- Multi-format : CSV, JSON, JSON Lines, éventuellement Excel
- Historique des scrapes pour éviter l’écrasement des données

---

## 5️⃣ CLI et UX
- Mode batch pour traiter une liste d’URLs
- Option de préfixe + timestamp (déjà intégré)
- Logs détaillés + export de logs vers fichier séparé
- Option pour filtrer H1/H2/H3 ou ne scraper que certaines sections

---

## 6️⃣ Tests & Qualité
- Couverture des tests unitaires pour tous les modules
- Intégration continue (GitHub Actions) : lint + tests + build
- Documentation complète du code et docstrings

---

## 7️⃣ Roadmap long terme
- Système de plugins pour ajouter de nouvelles stratégies de scraping sans toucher le core
- Interface web pour lancer des scrapes depuis un navigateur
- Dashboard pour suivre les résultats, statistiques et historiques

---

**💡 Note :** Avec cette roadmap, CrawlForge devient un outil **pro, rapide et extensible**, prêt pour usage personnel ou open-source.
