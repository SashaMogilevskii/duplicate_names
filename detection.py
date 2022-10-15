from script import *
import pandas as pd

def check(company_name):
    """
    Check company_name in SQL_base
    :param company_name:
    :return: True or False
    """

    data = pd.read_csv('data/data_v2_10_oct.csv')

    return company_name in data.name_1.unique()


def predict_names(company_names):
    """
    model - predict
    :param company_names:
    :return:
    """
    update_names = update_company_names(company_names)
    print(f'Company: {company_names}, update_name: {update_names}')
    predictions = [('Volga', 0.8231), ('Ivanko', 0.65), ('Fresqo', 0.65)]

    return predictions
