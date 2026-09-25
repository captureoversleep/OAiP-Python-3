while True:
    time = int(input('What current hour? : '))
    if time >= 10 and time <24:
        print('We are open!')
    else:
        break
print('We are closed! Working hours: from 10 to 24.')