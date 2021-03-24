import os

from covid_cajamar.extraction.extractors import (CovidDataExtractor,
                                                 CovidDataPreDiseaseExtractor)


class DataExtractionPipeline:
    def download_data(self):
        os.system("make download_data")

    def extract_data(self):
        CovidDataExtractor().extract()
        CovidDataPreDiseaseExtractor().extract()

    def run(self):
        self.download_data()
        self.extract_data()


if __name__ == "__main__":
    DataExtractionPipeline().run()
