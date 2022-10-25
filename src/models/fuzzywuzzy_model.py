import pandas as pd
from fuzzywuzzy import fuzz

from models.base_model import BaseModel

from pydantic_models import Predict


class FuzzyWuzzyModel(BaseModel):
    def __init__(self):
        super().__init__()

    def predict(self, company_name: str, db_companies: pd.DataFrame, k: int) -> list[Predict]:
        db_companies["fuzz"] = db_companies.name_1_upd.apply(lambda x: fuzz.token_set_ratio(x, company_name))
        db_companies = db_companies.sort_values("fuzz", ascending=False).reset_index(drop=True)
        df_predict = db_companies.loc[:k - 1, ["name_1", "fuzz"]]
        df_predict.loc[:, "probability"] = df_predict.fuzz / 100

        predictions = [
            Predict(company_name=row["name_1"], probability=row["fuzz"] / 100) for _, row in df_predict.iterrows()
        ]

        return predictions
