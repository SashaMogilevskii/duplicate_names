from scripts.detection import Detection
from scripts.script import Preprocessing

preprocessing = Preprocessing()
detection = Detection(preprocessing=preprocessing)


def main():
    print('Connect...... 1...2.... 3')
    company_name = input('Please write name_company:.. ')
    check_name = detection.check_name(company_name)

    print(f'Name company: {company_name}')

    if check_name:
        print('Company found!')

    else:
        print('Company not found, perhaps you meant:')
        print('-------------------------')

        list_similar_names = detection.predict_names(company_name)
        for name, probability in list_similar_names:
            print(f'Company: {name}, probability {probability:.2f}')

        print('-------------------------')
        # мб здесь нужно добавить что если нет совпадений добавить название компании в бд?


if __name__ == "__main__":
    main()

    print('Successful')
