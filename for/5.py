gl = 'аеёиоуыыэюя'
string = input('Введите строку: ')
gl_count = 0

for ch in string:
    if ch.lower() in gl:
        gl_count += 1

print(gl_count)