cat_count=0
while True:
    cat=input('Enter your category (end for exit): ')
    if cat == 'end':
        break
    cat_count += 1
print('Total category count:', cat_count)