'''

  0  |  1  |  2 
-----------------
  3  |  4  |  5  
-----------------
  6  |  7  |  8  

Задачи:
Алгоритм проверки победителя
    Совпадение элементов с подряд идущими одинаковыми символами (0-2, 3-5, 6-8)
    Совпадение элементов с индексами, различающимися на 3
    Совпадение элементов с индексами, различающимися последовательно на 4 или 2
    В случае победы возвращатся индекс победителя, иначе - 0
Проверка корректности хода
Отрисовка поля не экране

Алгоритм проекта:
Задаём исходные параметры
    Исходное состояние поля
    Индекс игрока
Считываем ходы и каждый раз проверяем победителя
    Считывание хода
    Проверка корректности хода
    Алгорим проверки победителя
Вывод результата
        '''

def correct_move(arr):
    m = input()
    if m.isnumeric():
        m = int(m)
    else:
        print("Выйди и зайди нормально!")
        correct_move(arr)
    if m < 1 or m > 9:
        print("Выйди и зайди нормально!")
        correct_move(arr)
    elif type(arr[m-1]) != int:
        print("Выйди и зайди нормально!")
        correct_move(arr)
    else:
        if player:
            arr[m-1] = 'o'
        else:
            arr[m-1] = 'x'
    return arr

def winner_check(arr):
    for i in range(3):
        if arr[i*3] == arr[i*3+1] == arr[i*3+2]:
            return 1 if arr[i*3] == 'x' else 2
        elif arr[i] == arr[i+3] == arr[i+6]:
            return 1 if arr[i*3] == 'x' else 2
    if arr[0] == arr[4] == arr[8] or arr[2] == arr[4] == arr[6]:
        return 1 if arr[4] == 'x' else 2
    return 0

def show(arr):
    for i, el in enumerate(arr, 1):
        print(el, end=' ')
        if not i%3:
            print()

field = [i for i in range(1, 10)]
player = False
player1 = input("Введите имя: ")
player2 = input("Введите имя: ")
winner = 0

show(field)

for i in range(9):
    field = correct_move(field)
    show(field)
    player = not player
    winner = winner_check(field)
    if winner:
        break

if not winner:
    print("Ничья!")
else:
    if winner == 1:
        print("Выиграл " + player1)
    else:
        print("Выиграл " + player2)
