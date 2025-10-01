import dlt
from dlt.sources.rest_api import rest_api_source

source = rest_api_source(
    {
    "client": {
        "base_url":"https://pokeapi.co/api/v2/"
    } ,
    "resource_defaults": {
                    "endpoint": {
                        "params": {
                            "limit": 1000,
                        },
                    },
                },
                "resources": [
                                "pokemon",
                                "berry",
                                "location",
                            ],
                        }
)

pipeline = dlt.pipeline(
    pipeline_name="pockemon_api", ##name de pipeline
    destination="duckdb" ##this the database
)

if __name__=="__main__":
    pipeline.run(source)