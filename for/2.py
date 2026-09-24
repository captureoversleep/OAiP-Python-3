numb = int(input('Введите число: '))
result = 0

for i in range(1, 11):
    result = numb * i
    print(numb, 'x', i, '=', result)