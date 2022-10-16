from transliterate import translit
from configs.config import list_words, rus_letters


class Preprocessing:
    popular_words = list_words
    rus_letters = rus_letters

    @staticmethod
    def convert_str_to_eng(company_name: str, language_code: str = "ru") -> str:
        """
        The function checks the string and translates to English,
        and delete 'OOO' and other abbreviation iin Russian names
        """

        if any([i in rus_letters for i in company_name]):
            company_name = company_name.replace("ООО", "")
            company_name = company_name.replace("ОАО", "")
            company_name = company_name.replace("АО", "")
            company_name = company_name.replace("ГК", "")

            return translit(company_name, language_code=language_code, reversed=True)

        return company_name

    @staticmethod
    def replace_symbols(company_name: str) -> str:
        """
        Delete all symbols in name_company
        """

        update_name = ""

        for ch in company_name:
            if ch.isalnum():
                update_name += ch
            else:
                update_name += " "

        update_name = update_name.strip()
        update_name = " ".join(update_name.split())

        return update_name

    def drop_popular_words(self, company_name: str) -> str:
        """
        Drop popular words from company_name
        """

        update_name = []
        company_name = company_name.replace(",", " ")

        update_name = [word for word in company_name.split() if word not in self.popular_words]
        return " ".join(update_name)

    def preproccessing_name(self, company_name: str) -> str:
        """
        Function, which include 3 function:
        1. convert_string_to_english
        2. drop_popular_words
        3. replace_symbols
        """

        company_name = self.convert_str_to_eng(company_name)
        company_name = self.drop_popular_words(company_name)
        company_name = self.replace_symbols(company_name)
        return company_name
