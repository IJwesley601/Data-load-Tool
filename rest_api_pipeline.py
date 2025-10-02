import dlt
from dlt.sources.rest_api import rest_api_source

# Définition de la source REST API
# Ici, nous consommons l'API publique de Pokémon : https://pokeapi.co/api/v2/
# Nous configurons DLT pour charger plusieurs ressources (pokemon, berry, location)
# et utiliser le mode "merge" (upsert) pour éviter les doublons ou mettre à jour les données modifiées.
source = rest_api_source(
    {
        "client": {
            # Base URL de l'API cible
            "base_url": "https://pokeapi.co/api/v2/"
        },
        "resource_defaults": {
            # Configuration par défaut pour chaque endpoint
            "endpoint": {
                "params": {
                    "limit": 1000,  # On récupère 1000 enregistrements par appel
                },
            },
        },
        "resources": [
            {
                "name": "pokemon",             # Nom de la ressource
                "primary_key": "name",         # Clé primaire (unique par Pokémon)
                "write_disposition": "merge",  # Mode "merge" : met à jour si le Pokémon existe déjà
            },
            "berry",      # Autres ressources de l'API
            "location",
        ],
    }
)

# Définition du pipeline DLT
# Le pipeline est nommé "pokemon_api" et stocke les données dans une base DuckDB.
pipeline = dlt.pipeline(
    pipeline_name="pokemon_api",  # Nom interne du pipeline
    destination="duckdb",         # Destination : DuckDB (base de données locale)
    dataset_name="poke_dataset"   # Nom du dataset dans DuckDB
)

if __name__ == "__main__":
    # Exécution du pipeline : 
    # - Récupère les données depuis l'API
    # - Les charge dans DuckDB en respectant la configuration ci-dessus
    pipeline.run(source)
