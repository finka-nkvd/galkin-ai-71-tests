num = int(input('введите номер задания '))
if num == 1:
    type = int(input('введите тип данных (1-гб, 2-мб, 3-кб, 4-б, 5-биты, только цифру) '))
    if type == 1:
        n = int(input('введите количество гб '))
        mb = n * 1024
        kb = mb * 1024
        b = kb * 1024
        bit = b * 8
        print(mb, kb, b, bit, sep = '\n')
    elif type == 2:
        n = int(input('введите количество мб '))
        gb = n / 1024
        kb = n * 1024
        b = kb * 1024
        bit = b * 8
        print(gb, kb, b, bit, sep = '\n')
    elif type == 3:
        n = int(input('введите количество кб '))
        b = n * 1024
        bit = b * 8
        mb = n / 1024
        gb = mb / 1024

        print(gb, mb, b, bit, sep = '\n')
    elif type == 4:
        n = int(input('введите количество б '))
        bit = n * 8
        kb = n / 1024
        mb = kb / 1024
        gb = mb / 1024
        print(gb, mb, kb, bit, sep = '\n')
    elif type == 5:
        n = int(input('введите количество бит '))
        b = n / 8
        kb = b / 1024
        mb = kb / 1024
        gb = kb / 1024
        print(gb, mb, kb, b, sep = '\n')

elif num == 2:
    listiki = int(input('введите количество страниц '))
    print(listiki*64*112*5*2)
elif num == 3:
    weather = input('введите погоду ')
    if weather == 'ветренно':
        deg = input('тепло ли на улице ')
        if deg == 'да':
            print('одень ветровку')
        elif deg == 'нет':
            print('одень куртку')
    elif weather == 'солнечно':
        deg = input('тепло ли на улице ')
        if deg == 'да':
            print('одень майку')
        elif deg == 'нет':
            print('одень жилетку')
    elif weather == 'дождливо':
        deg = input('тепло ли на улице ')
        if deg == 'да':
            print('одень дождевик')
        elif deg == 'нет':
            print('одень куртку')
    elif weather == 'снежно':
            print('одень пуховик')










