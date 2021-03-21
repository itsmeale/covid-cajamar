from typing import Dict

from pydantic import BaseSettings


class Settings(BaseSettings):
    ibge_code_cajamar: int = 3509205

    covid_data_dataset: Dict = {
        "path": "data/raw/covid_data.csv",
        "columns": [
            "nome_munic",
            "codigo_ibge",
            "datahora",
            "obitos",
            "obitos_mm7d",
            "casos",
            "casos_mm7d",
            "letalidade",
        ],
    }

    covid_data_pre_disease_dataset: Dict = {
        "path": "data/raw/covid_data_pre_disease.csv.zip",
        "columns": [
            "codigo_ibge",
            "nome_munic",
            "data_inicio_sintomas",
            "idade",
            "obito",
            "diagnostico_covid19",
        ],
    }

    interim_covid_data_dataset: Dict = {"path": "data/interim/covid_data.csv"}

    interim_covid_data_pre_disease_dataset: Dict = {
        "path": "data/interim/covid_data_pre_disease.csv"
    }


settings = Settings()
