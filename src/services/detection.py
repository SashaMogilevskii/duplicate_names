import pandas as pd

from models.fuzzywuzzy_model import FuzzyWuzzyModel
from models.catboost_model import CatBoostModel
from preprocessing import Preprocessing
from pydantic_models import Predict


class Detection:
    def __init__(self, preprocessing: Preprocessing, fuzzy_wuzzy_model: FuzzyWuzzyModel, catboost_model: CatBoostModel):
        self.data = pd.read_csv("../data/database.csv")
        self.list_company_in_base = self.data.name_1.unique()
        self.preprocessing = preprocessing
        self.models: dict[str, FuzzyWuzzyModel | CatBoostModel] = {
            "fuzzy_wuzzy": fuzzy_wuzzy_model,
            "catboost": catboost_model
        }

    def check_name(self, company_name: str) -> bool:
        """
        Check company_name in SQL_base
        :param company_name:
        :return: True or False
        """

        return company_name in self.list_company_in_base

    def predict_names(self, company_names: str, model="fuzzy_wuzzy", k: int = 7) -> list[Predict]:
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

    def match_companies(self, company_name: str, k: int, model: str) -> list[Predict]:
        check_name = self.check_name(company_name)
        if check_name:
            return [Predict(company_name=company_name, probility=1)]

        else:
            print("Company not found, perhaps you meant:")
            list_similar_names = self.predict_names(company_name, k=k, model=model)
        return list_similar_names
