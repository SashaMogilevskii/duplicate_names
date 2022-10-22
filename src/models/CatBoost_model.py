import pandas as pd
import pickle

from catboost import CatBoostClassifier

from models.base_model import BaseModel


model = CatBoostClassifier()  # parameters not required.
model.load_model("./models/modelCatBoost.cbm")
tf_idf = pickle.load(open("./models/tfidf1.pkl", "rb"))


class CatBoostModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.tfidf = tf_idf
        self.model = model

    def predict(self, company_name: str, db_companies: pd.DataFrame, k: int = 5) -> list[tuple[str, float]]:
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
            .loc[:k, ["name_1", "probability"]]
        )
        predictions = []

        for i, row in name_data.iterrows():
            predictions.append((row["name_1"], row["probability"] / 100))

        return predictions
