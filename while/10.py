discount = '0%'

while True:
    cat_input = input('Введите категорию товара (stop для выхода): ')
    if cat_input.lower() == 'мясные изделия':
        discount = '10%'
        break
    elif cat_input.lower() == 'напитки':
        discount = '30%'
        break
    elif cat_input == 'stop':
        print('Остановлено, скидок нет!')
        break
if discount != '0%':
    print('Ваша скидка:', discount)