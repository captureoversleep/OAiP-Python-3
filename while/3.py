valid_promo1='life'
valid_promo2='health'
while True:
    promo = input('Enter your promocode: ')
    if promo == valid_promo1 or promo == valid_promo2:
        print('Promocode has been accepted!')
        break
    print('Promocode is invalid! Try again')