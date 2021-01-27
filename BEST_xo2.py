def win_check(lst):
    flag = False
    for i in range(3):
        if lst[i*3] == lst[i*3 + 1] == lst[i*3 + 2]:
            flag = True
            break
        elif lst[i] == lst[i + 3] == lst[i + 6]:
            flag = True
            break
    if lst[0] == lst[4] == lst[8] or lst[2] == lst[4] == lst[6]:
        flag = True
    return flag


def field_print(lst):
    print(\
        '\n\t --- --- ---\n' + \
        '\t| ' + lst[0] + ' | ' + lst[1] + ' | ' + lst[2] + ' |\n' + \
        '\t --- --- ---\n' + \
        '\t| ' + lst[3] + ' | ' + lst[4] + ' | ' + lst[5] + ' |\n' + \
        '\t --- --- ---\n' + \
        '\t| ' + lst[6] + ' | ' + lst[7] + ' | ' + lst[8] + ' |\n' + \
        '\t --- --- ---\n\n')



print("=" * 43 + \
      "\nВы начали новый матч игры 'крестики-нолики'\n" + \
      "=" * 43 + '\n' + \
      " " * 10 + "Игроки, представтесь")
pl1 = input('Игрок 1, введите имя: ')
pl2 = input('Игрок 2, введите имя: ')
print(f'''
    Игрок {pl1}, вы играете крестиками, игрок {pl2} - ноликами
Вам нужно поочерёдно вводить номера клеток поля, чтобы записать в них свой символ.
Если собрано три в ряд, вы победили. Игра началась!
    ''')
field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
remaining_cells = 9


is_somebody_won = False
while remaining_cells:
    field_print(field)
    if remaining_cells % 2 == 1:
        simbol = 'x'
        name = pl1
    else:
        simbol = 'o'
        name = pl2

    n = input(name + ', введите номер клетки: ')

    # проверка
    if n in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        if n in field:
            field[int(n) - 1] = simbol
            remaining_cells -= 1
            if remaining_cells == 0:
                print("Draw")
        else:
            print("Ошибка ввода, попробуйте ещё раз\nЭта клетка уже занята!")
            continue
    else:
        print("Ошибка ввода, попробуйте ещё раз\nМожно использовать только цифры 1-9")
        continue

    if win_check(field):
        is_somebody_won = True
        break


if is_somebody_won:
    print("=" * 43 + "\n\t\tПобедил %s!" % (name))
else:
    print("=" * 43 + "\n\t\tНичья")