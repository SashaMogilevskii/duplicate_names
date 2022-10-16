from fuzzywuzzy import fuzz
from base_model import BaseModel


class FuzzyWuzzyModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.model = fuzz

    def predict(self, company_name_check: str, company_name_from_db: list, k: int = 5) -> list[tuple]:
        prediction = []
        for company_name_from_list in company_name_from_db:
            prediction.append(
                tuple(
                    [
                        company_name_from_list,  # company name
                        self.model.token_set_ratio(company_name_check, company_name_from_list) * 0.01,  # proba
                    ]
                )
            )

        predicted = sorted(prediction, key=lambda x: x[1])

        return predicted[:k]
