from abc import ABC
import pandas as pd


class BaseModel(ABC):
    def __init__(self):
        pass

    def train(self, data: pd.DataFrame) -> None:
        """
        Method to train model. Dataset consider columns: name_1, name_2, is_duplicate
        :param data:
        :return:
        """
        pass

    def predict(self, company_name: str, company_from_db: pd.DataFrame, k: int = 5) -> list[tuple]:
        """

        :param company_name: company
        :param company_from_db: df of company names
        :param k: k top relevant company names
        :return: list with tuples.
        """
        pass
