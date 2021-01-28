def shaw_field(lst):
    if len(lst) != 9:
        print("Функция shaw_field() работает только со списком из 9-ти элементов!")
    else:
        print('  -----------\n',
            '|', lst[0], '|', lst[1], '|', lst[2], '|\n',
            ' -----------\n',
            '|', lst[3], '|', lst[4], '|', lst[5], '|\n',
            ' -----------\n',
            '|', lst[6], '|', lst[7], '|', lst[8], '|\n',
            ' -----------\n')
'''
 -----------
| x | 2 | o |
 -----------
| 4 | x | o |
 -----------
| 7 | 8 | x |
 -----------
'''

player1 = "Моцарт" # input("Игрок 1, представьтесь:")
player2 = "Сальери" # input("Игрок 2, представьтесь:")
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pl1_steps = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
pl2_steps = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

i = 9
while i > 0:

    if i % 2 == 1:
        player = player1
        simbol = 'X'
    else:
        player = player2
        simbol = 'O'

    i -= 1

    cell = int(input('Игрок ' + player + ' введите номер клетки: '))

    if cell in field:
        field[cell-1] = simbol
        if simbol == 'X':
            for lot in range(len(pl1_steps)):
                for num in range(len(pl1_steps[lot])):
                    if pl1_steps[lot][num] == cell:
                        pl1_steps[lot][num] = simbol
            # print(pl1_steps)
        elif simbol == 'O':
            for lot in range(len(pl2_steps)):
                for num in range(len(pl2_steps[lot])):
                    if pl2_steps[lot][num] == cell:
                        pl2_steps[lot][num] = simbol
            # print(pl2_steps)

        if ['X', 'X', 'X'] in pl1_steps:
            print("Победил игрок " + player1 + ' !!!')
            break
        elif ['O', 'O', 'O'] in pl2_steps:
            print("Победил игрок " + player2 + ' !!!')
            break

    elif 1 <= cell <= 9:
        i += 1
        print('Клетка уже занята, введите другой номер')
    else:
        i += 1
        print('Некорректный ввод, введите номер свободной клетки.')

    shaw_field(field)

shaw_field(field)