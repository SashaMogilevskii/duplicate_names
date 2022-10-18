from fastapi import FastAPI

from models.fuzzywuzzy_model import FuzzyWuzzyModel
from scripts.detection import Detection
from scripts.script import Preprocessing

preprocessing = Preprocessing()
fuzzy_wuzzy_model = FuzzyWuzzyModel()
detection = Detection(preprocessing=preprocessing, fuzzy_wuzzy_model=fuzzy_wuzzy_model)

app = FastAPI()


@app.post("/match_companies")
async def route(company_name: str) -> list[tuple[str, float]]:
    check_name = detection.check_name(company_name)
    if check_name:
        return [(company_name, 1)]

    else:
        print("Company not found, perhaps you meant:")
        list_similar_names = detection.predict_names(company_name)
    return list_similar_names
