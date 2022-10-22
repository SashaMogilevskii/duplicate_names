from fastapi import FastAPI, Query

from models.fuzzywuzzy_model import FuzzyWuzzyModel
from models.CatBoost_model import CatBoostModel
from scripts.detection import Detection
from scripts.script import Preprocessing
from typing import Optional

preprocessing = Preprocessing()
fuzzy_wuzzy_model = FuzzyWuzzyModel()
catboost_model = CatBoostModel()
detection = Detection(preprocessing=preprocessing, fuzzy_wuzzy_model=fuzzy_wuzzy_model, cat_boost_model=catboost_model)


app = FastAPI()


@app.post("/match_companies")
async def route(
    company_name: str, k: int, model: Optional[str] = Query(None, description="Choose model: catboost or fuzzy_wuzzy")
) -> list[tuple[str, float]]:
    check_name = detection.check_name(company_name)
    if check_name:
        return [(company_name, 1)]

    else:
        print("Company not found, perhaps you meant:")
        list_similar_names = detection.predict_names(company_name, k=k, model=model)
    return list_similar_names
