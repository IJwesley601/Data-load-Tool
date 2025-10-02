

markdown
# 🚀 Pokémon API Pipeline avec DLT et DuckDB

Ce projet permet d’extraire des données depuis l’API publique [PokéAPI](https://pokeapi.co/), puis de les charger dans une base **DuckDB** grâce à [DLT (Data Load Tool)](https://dlthub.com/).


## 📌 Fonctionnalités
- Récupération de plusieurs ressources de la PokéAPI (`pokemon`, `berry`, `location`).
- Chargement automatique dans une base DuckDB locale.
- Mode `merge` activé : 
  - ✅ Ajout des nouvelles lignes
  - ✅ Mise à jour des données si elles changent
  - ✅ Pas de doublons

---

## 🛠️ Installation et configuration

### 1. Cloner le projet
bash:
git clone https://github.com/IJwesley601/Data-load-Tool.git
cd pokemon-pipeline


### 2. Créer un environnement virtuel

Linux / Mac :

bash:
python3 -m venv venv
source venv/bin/activate


Windows (PowerShell) :

powershell:
python -m venv venv
.\venv\Scripts\activate


### 3. Installer les dépendances

bash:
pip install -r requirements.txt


---

## ▶️ Lancer le pipeline

Exécuter le script Python :

bash:
python rest_api_pipeline.py


Après exécution :

* Une base DuckDB sera créée dans ton dossier (`.dlt/pokemon_api.duckdb` par défaut).
* Tu pourras explorer la base avec DuckDB.


## 🔍 Explorer la base DuckDB

Tu peux interroger la base DuckDB directement en ligne de commande :

bash : 
duckdb .dlt/pokemon_api.duckdb || duckdb ./pokemon_api.duckdb


Puis exécuter des requêtes SQL, par exemple :

sql:
SELECT * FROM poke_dataset__pokemon LIMIT 10;
SELECT * FROM poke_dataset__berry LIMIT 5;


---

## ⏰ Exécution planifiée

Si tu veux exécuter le pipeline **tous les jours à minuit**, tu peux utiliser `cron` (Linux/Mac) ou le planificateur de tâches (Windows).

### Exemple avec cron (Linux) :

bash:
crontab -e


Ajouter la ligne suivante :


0 0 * * * /usr/bin/python3 /chemin/vers/rest_api_pipeline.py >> pipeline.log 2>&1


Cela exécutera ton pipeline **tous les jours à minuit** et enregistrera les logs dans `pipeline.log`.

---


## ✅ Résumé

* Installe les dépendances avec `pip install -r requirements.txt`.
* Lance le pipeline avec `python rest_api_pipeline.py`.
* Explore les données directement avec DuckDB.
* Optionnel : planifie une exécution automatique tous les jours.

🎉 Tu as maintenant un pipeline ETL complet et reproductible avec DLT et DuckDB !

