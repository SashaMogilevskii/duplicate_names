from transliterate import translit

list_words = ['Ltd.', 'Co.,', 'Inc.', 'International', 'De', 'Industries', 'Trading', 'Logistics', '&',
              'Rubber', 'Co.', 'Private', 'Sa', 'Pvt.,', 'India', 'Llc', 'Cv', 'S.A.', 'Ltda', 'S', 'Mexico',
              'Products', 'Industrial', 'Corporation', 'Imp.', 'A', 'Exp.', 'C.V.', 'Ltd.', 'Co.,', 'International',
              'Inc.', 'De', 'Industries', 'Trading', 'Logistics', '&', 'Rubber', 'Co.', 'Private', 'Sa', 'Pvt.',
              'India', 'Llc', 'Cv', 'Ltda', 'S.A.', 'S', 'Mexico', 'Products', 'Corporation', 'Industrial', 'Imp.',
              'A', 'Exp.', 'C.V.', 'A/S']
rus_letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
               "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


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


def update_company_names(company_name):
    """
    Function, which include 3 function:
    1. convert_string_to_english
    2. drop_popular_words
    3. replace_symbols
    """

    company_name = convert_string_to_english(company_name)
    company_name = drop_popular_words(company_name)
    company_name = replace_symbols(company_name)

    return company_name
