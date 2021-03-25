from covid_cajamar.extraction.extractors import (CovidDataExtractor,
                                                 CovidDataPreDiseaseExtractor)

if __name__ == "__main__":
    covid_data_extractor = CovidDataExtractor()
    covid_data_extractor.extract()

    covid_data_pre_disease_extractor = CovidDataPreDiseaseExtractor()
    covid_data_pre_disease_extractor.extract()
