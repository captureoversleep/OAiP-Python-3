price_total = 0
price = -1
while price != 0:
    price = int(input('Enter product price (0 for stop): '))
    price_total += price
print('Total price:', price_total)