import pandas as pd

from script import Preprocessing
from fuzzywuzzy import fuzz


class Detection:
    def __init__(self, preprocessing: Preprocessing):
        self.data = pd.read_csv("data/database.csv")
        self.list_company_in_base = self.data.name_1.unique()
        self.preprocessing = preprocessing

    def check_name(self, company_name: str) -> bool:
        """
        Check company_name in SQL_base
        :param company_name:
        :return: True or False
        """

        return company_name in self.list_company_in_base

    def predict_names(self, company_names: str, k: int = 7) -> list[tuple[str, float]]:
        """
        model - predict
        :param company_names:
        :return:
        """
        data = self.data.copy()

        # baseline
        update_names = self.preprocessing.preproccessing_name(company_names)

        data["fuzz"] = data.apply(lambda x: fuzz.partial_ratio(x.name_1_upd, update_names), axis=1)
        df_company = data.sort_values("fuzz", ascending=False)[["name_1", "fuzz"]][:k]
        list_company = []

        for i, row in df_company.iterrows():
            list_company.append((row["name_1"], row["fuzz"] / 100))

        print(f"Company: {company_names}, update_name: {update_names}")

        return list_company
