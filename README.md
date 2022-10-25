# Matching Of Duplicate Company Names


## Installation

``` shell
# apt install required packages:
sudo apt update
sudo apt install -y zip htop pipenv
  
# clone repo:
git clone https://github.com/SashaMogilevskii/duplicate_names.git

# go to the folder:
cd duplicate_names

# create virtualenv:
pipenv install

# activate virtualenv:
pipenv shell

# run main.py:
pipenv run python main.py

```


## Contributors

1. Шакиров Ренат
2. Набатчиков Илья
3. Могилевский Саша

``` shell
For contributing please use linterts and hooks the following commands:

black .
pre-commit run --all-files
 ```


## Tree

``` shell
.gitattributes
.gitignore
.pre-commit-config.yaml
LICENSE
Pipfile
Pipfile.lock
README.md
pylama.ini
pyproject.toml
mypy.ini
data
   |-- data.csv
   |-- data_v2_10_oct.csv
   |-- data_v2_19_oct.csv
   |-- database.csv
models
   |-- __init__.py
   |-- catboost.pkl
   |-- tfidf1.pkl
notebooks
   |-- Baseline.ipynb
   |-- Baseline_model.ipynb
   |-- Baseline_model_10_20_CatBoost_unique.ipynb
   |-- Baseline_model_19_10(TF-IDF)).ipynb
   |-- Baseline_model_19_10.ipynb
   |-- Bert_model.ipynb
   |-- EDA  & Transform data(19_10).ipynb
   |-- EDA  & Transform data.ipynb
   |-- Model_10_22_CatBoost_unique.ipynb
src
   |-- configs
   |   |-- config.py
   |-- main.py
   |-- models
   |   |-- __init__.py
   |   |-- base_model.py
   |   |-- catboost_model.py
   |   |-- fuzzywuzzy_model.py
   |-- preprocessing.py
   |-- pydantic_models.py
   |-- services
   |   |-- __init__.py
   |   |-- detection.py
```