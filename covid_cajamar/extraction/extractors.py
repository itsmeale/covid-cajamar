import numpy as np
import pandas as pd

from covid_cajamar.config import settings
from covid_cajamar.interfaces.interfaces import Extractor


class CovidDataExtractor(Extractor):
    @staticmethod
    def _parse_calculated_columns(df: pd.DataFrame) -> pd.DataFrame:
        def transform_to_float(value: str):
            return np.float32(str(value).replace(",", ".").strip())

        temp_df = df.copy()

        columns_to_parse = [
            "casos_mm7d",
            "obitos_mm7d",
            "letalidade",
        ]

        for col in columns_to_parse:
            temp_df[col] = temp_df[col].apply(transform_to_float)

        return temp_df

    def read(self) -> pd.DataFrame:
        return pd.read_csv(
            settings.covid_data_dataset["path"],
            sep=";",
            usecols=settings.covid_data_dataset["columns"],
        )

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        filtered_df = df[df["codigo_ibge"] == settings.ibge_code_cajamar]
        fixed_float_cold_df = CovidDataExtractor._parse_calculated_columns(filtered_df)
        return fixed_float_cold_df

    def write(self, df: pd.DataFrame) -> bool:
        try:
            df.to_csv(settings.interim_covid_data_dataset["path"], index=False)
            return True
        except Exception as e:
            print(e)
            return False

    def extract(self):
        self.write(self.preprocess(self.read()))
