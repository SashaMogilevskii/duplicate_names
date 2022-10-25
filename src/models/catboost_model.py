import pandas as pd

from models.base_model import BaseModel

from pydantic_models import Predict


class CatBoostModel(BaseModel):
    def __init__(self, tf_idf_path: str, catboost_path: str):
        super().__init__()
        self.tfidf = self.load_model(tf_idf_path)
        self.model = self.load_model(catboost_path)

    def predict(self, company_name: str, db_companies: pd.DataFrame, k: int) -> list[Predict]:
        db_companies["add_company"] = company_name

        # Transforms name1 in base and company_name in tf_idf
        db_companies_name1 = pd.DataFrame(self.tfidf.transform(db_companies.name_1_upd).toarray())
        data_new_company = pd.DataFrame(self.tfidf.transform(db_companies.add_company).toarray())

        # Create new_data
        name_data = pd.concat([db_companies_name1, data_new_company], axis=1, ignore_index=False)
        name_data.columns = [i for i in range(550 * 2)]

        # Predict is_dublicated
        target = self.model.predict_proba(name_data)[:, 1]

        # Sort and predict top_K
        name_data["probability"] = target
        name_data["name_1"] = db_companies.name_1
        name_data = (
            name_data.sort_values("probability", ascending=False)
            .reset_index(drop=True)
            .loc[:k - 1, ["name_1", "probability"]]
        )

        predictions = [
            Predict(company_name=row["name_1"], probability=row["probability"]) for _, row in name_data.iterrows()
        ]

        return predictions
