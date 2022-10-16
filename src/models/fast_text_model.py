import pandas as pd
from polyfuzz import PolyFuzz

from base_model import BaseModel

train_words = ["apple", "apples", "appl", "recal", "house", "similarity"]
unseen_words = ["apple", "apples", "mouse"]

# Fit
model = PolyFuzz("TF-IDF")
model.fit(train_words)

# Transform
results = model.transform(unseen_words)


class TfIdfMolel(BaseModel):
    def __init__(self):
        super().__init__()
        self.model = PolyFuzz("TF-IDF")

    def train(self, data: pd.DataFrame) -> None:
        self.model.fit(train_words)