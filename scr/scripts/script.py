from transliterate import translit
from scr.configs.config import list_words, rus_letters


class Preprocessing():

    list_words = list_words
    rus_letters = rus_letters
    # def __init__(self):
    #     self.__list_words = list_words
    #     self.__rus_letters = rus_letters

    @staticmethod
    def convert_string_to_english(company_name):
        """
        The function checks the string and translates to English,
        and delete 'OOO' and other abbreviation iin Russian names
        """

        if any([i in rus_letters for i in company_name]):
            company_name = company_name.replace('ООО', '')
            company_name = company_name.replace('ОАО', '')
            company_name = company_name.replace('АО', '')
            company_name = company_name.replace('ГК', '')

            return translit(company_name, language_code='ru', reversed=True)

        return company_name

    @staticmethod
    def replace_symbols(company_name):
        """
        Delete all symbols in name_company
        """

        update_name = ''

        for ch in company_name:
            if ch.isalnum():
                update_name += ch
            else:
                update_name += ' '

        update_name = update_name.strip()
        update_name = ' '.join(update_name.split())

        return update_name

    @staticmethod
    def drop_popular_words(company_name):
        """
        Drop popular words from company_name
        """

        update_name = []
        company_name = company_name.replace(',', ' ')
        for word in company_name.split():
            if word not in list_words:
                update_name.append(word)

        return ' '.join(update_name)

    @staticmethod
    def preproccessing(company_name):
        """
        Function, which include 3 function:
        1. convert_string_to_english
        2. drop_popular_words
        3. replace_symbols
        """

        company_name = Preprocessing.convert_string_to_english(company_name)
        company_name = Preprocessing.drop_popular_words(company_name)
        company_name = Preprocessing.replace_symbols(company_name)

        return company_name