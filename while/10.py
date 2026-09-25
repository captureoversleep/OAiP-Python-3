while True:
    cat_input = input('Введите категорию товара (stop для выхода): ')
    if cat_input.lower() == 'мясные изделия':
        print('Скидка 10%')
    elif cat_input.lower() == 'напитки':
        print('Скидка 30%')
    elif cat_input == 'stop':
        break
    else:
        print('На указанную категорию скидок нет')
