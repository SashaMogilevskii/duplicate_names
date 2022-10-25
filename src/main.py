from fastapi import FastAPI, Query

from configs.config import models_paths, rus_letters, list_words
from models.fuzzywuzzy_model import FuzzyWuzzyModel
from models.catboost_model import CatBoostModel
from pydantic_models import Predict
from services.detection import Detection
from preprocessing import Preprocessing

preprocessing = Preprocessing(list_words=list_words, rus_letters=rus_letters)
fuzzy_wuzzy_model = FuzzyWuzzyModel()
catboost_model = CatBoostModel(tf_idf_path=models_paths['tfidf'], catboost_path=models_paths['catboost'])
detection = Detection(preprocessing=preprocessing, fuzzy_wuzzy_model=fuzzy_wuzzy_model, catboost_model=catboost_model)

app = FastAPI()


@app.post("/match_companies")
async def route(
        company_name: str,
        k: int,
        model: str = Query(description="Choose model: catboost or fuzzy_wuzzy")
) -> list[Predict]:
    list_similar_names = detection.match_companies(company_name=company_name, k=k, model=model)
    return list_similar_names
