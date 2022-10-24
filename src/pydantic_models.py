from pydantic import BaseModel


class Predict(BaseModel):
    company_name: str
    probability: float
