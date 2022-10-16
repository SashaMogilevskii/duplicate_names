import pandas as pd

from scr.scripts.script import Preprocessing
from fuzzywuzzy import fuzz

class Detection():

    list_company_in_base = pd.read_csv('data/database.csv').name_1.unique()
    data = pd.read_csv('data/database.csv')

    @classmethod
    def check_name(cls, company_name):
        """
        Check company_name in SQL_base
        :param company_name:
        :return: True or False
        """

        return company_name in cls.list_company_in_base

    @classmethod
    def predict_names(cls, company_names, k=7):
        """
        model - predict
        :param company_names:
        :return:
        """
        data = cls.data

        ## baseline
        update_names = Preprocessing.preproccessing(company_names)

        data['fuzz'] = data.apply(lambda x: fuzz.partial_ratio(x.name_1_upd, update_names), axis=1)
        df_company = data.sort_values('fuzz', ascending=False)[["name_1", 'fuzz']][:k]
        list_company = []

        for i, row in df_company.iterrows():
            list_company.append([row["name_1"], row['fuzz'] / 100])

        print(f'Company: {company_names}, update_name: {update_names}')

        return list_company
