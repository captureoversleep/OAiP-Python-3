attempt = 1
valid_promo = 'fresh'

while attempt <= 3:
    promo = input('Enter your promo: ')
    if promo == valid_promo:
        print('Successful! Promocode activated on', attempt, 'attempt')
        break
    attempt += 1
    print('Invalid promo!')
