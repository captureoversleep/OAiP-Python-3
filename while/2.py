valid_promo='life'
while True:
    promo = input('Enter your promocode: ')
    if promo == valid_promo:
        print('Promocode has been accepted!')
        break
    print('Promocode is invalid!')