while True:
    price = float(input('Enter product price: '))
    if price == 0:
        break
    discount_price = price * 0.9
    print('Discount price:', discount_price)