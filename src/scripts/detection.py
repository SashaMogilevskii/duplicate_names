import pandas as pd

from models.fuzzywuzzy_model import FuzzyWuzzyModel
from scripts.script import Preprocessing


class Detection:
    def __init__(self, preprocessing: Preprocessing, fuzzy_wuzzy_model: FuzzyWuzzyModel):
        self.data = pd.read_csv("../data/database.csv")
        self.list_company_in_base = self.data.name_1.unique()
        self.preprocessing = preprocessing
        self.models: dict[str, FuzzyWuzzyModel] = {"fuzzy_wuzzy": fuzzy_wuzzy_model}

    def check_name(self, company_name: str) -> bool:
        """
        Check company_name in SQL_base
        :param company_name:
        :return: True or False
        """

        return company_name in self.list_company_in_base

    def predict_names(self, company_names: str, model="fuzzy_wuzzy", k: int = 7) -> list[tuple[str, float]]:
        """
        model - predict
        :param k:
        :param company_names:
        :return:
        """
        data = self.data.copy()

        # baseline
        company_name = self.preprocessing.preproccessing_name(company_names)

        predicts = self.models[model].predict(company_name=company_name, db_companies=data, k=k)
        print(f"company_name: {company_name}, predicts: {predicts}")

        return predicts
