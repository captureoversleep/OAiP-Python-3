cl_count = 0
while True:
    input('Enter your card number: ')
    if cl_count >= 3:
            print('Discounts are over!')
            break
    print("Congratulations! You receive 10% discount")
    cl_count += 1