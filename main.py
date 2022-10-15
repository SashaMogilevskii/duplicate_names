from detection import predict_names, check


def main():
    print('Connect...... 1...2.... 3')
    company_name = input('Please write name_company:.. ')

    print(f'Name company: {company_name}')
    check_name = check(company_name)

    if check_name:
        print('Company found!')

    else:
        print('Company not found, perhaps you meant:')
        print('-------------------------')

        list_similar_names = predict_names(company_name)
        for name, probability in list_similar_names:
            print(f'Company: {name}, probability {probability:.2f}')

        print('-------------------------')
        # мб здесь нужно добавить что если нет совпадений добавить название компании в бд?

if __name__ == "__main__":
    main()

    print('Successful')
