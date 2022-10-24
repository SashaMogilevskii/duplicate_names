import pickle
from abc import ABC
import pandas as pd

from pydantic_models import Predict


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

    def predict(self, company_name: str, db_companies: pd.DataFrame, k: int) -> list[Predict]:
        """

        :param company_name: company
        :param db_companies: df of company names
        :param k: k top relevant company names
        :return: list with tuples.
        """
        pass

    @staticmethod
    def load_model(path: str):
        with open(path, "rb") as f:
            model = pickle.load(f)
        return model
