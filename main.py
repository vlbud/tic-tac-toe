def start_game():
    """
    
    :return:
    
    """

    d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}   # для того чтобы поле рисовало значение из словаря

    def pole():                                                # подфункция для рисования игрового поля по словарю
        print("-------------")
        print(f"| {d[1]} | {d[2]} | {d[3]} |")
        print("-------------")
        print(f"| {d[4]} | {d[5]} | {d[6]} |")
        print("-------------")
        print(f"| {d[7]} | {d[8]} | {d[9]} |")
        print("-------------")
    player1 = input("Введите имя первого игрока: ")
    b1 = input("Выберите X или O ")
    if b1 not in "XO0ХОxoхо":       # выбирается символ игроком если не входит тогда надо ввести по новому
        b1 = input("Вы выбрали неправильный символ. Выберите X или O ")  # перевыбирается символ
    if b1 in "XxХх":  # если введенный символ похож на х то тогда у первого игрока х у второго 0 если нет то наоборот
        b1 = "X"
        b2 = "O"
    else:
        b1 = "O"
        b2 = "X"
    player2 = input("Введите имя второго игрока: ")
    pole()                                              # рисуется первоначальное поле
    busy_list = []                                      # сюда будут вводиться занятые поля
    flag1 = False                                       # флаг1 станет True, когда определится победитель
    n = 0         # это счетчик чтобы менялась очередность хода и если при n=9 не определится победитель, то будет ничья

    move = [player1, player2]  # список какой игрок будет ходить
    while flag1 is False and n < 9:  # условие игра идет до тех пор пока не определится победитель либо закончится поле
        risunok = [b1, b2]             # список какой символ будет ставить игрок который ходит
        a = input(f"Ходит {move[n %2]}, куда поставить {risunok[n %2]}  ")    # вводится игровое поле куда ходит игрок
        if a.isalpha():                # условие введенное поле должно быть числом
            flag = False
        else:
            flag = True
        while flag is False or int(a) < 1 or int(a) > 9 or a in busy_list:  # вводимое число должно быть в игровом поле
            if a in busy_list:
                a = input("Поле занято, введите другой номер поля  ")
            else:
                a = input("Вы ввели неверное поле, введите номер свободного поля  ")
            for y in a:
                if y.isalpha():
                    a = input("Введите число  ")
                    flag = False
                    break
                else:
                    flag = True
        busy_list.append(a)                 # создается список занятых полей
        d[int(a)] = risunok[n % 2]           # изменяется словарь, по ключу введеного поля на символ который ходил игрок
        n += 1                              # счетчик меняет очередность хода
        pole()                              # рисуется обновленное поле
        if d[1] == d[2] == d[3] or d[4] == d[5] == d[6] or d[7] == d[8] == d[9] or d[1] == d[4] == d[7] or d[2] == d[5] == d[8] or d[3] == d[6] == d[9] or d[1] == d[5] == d[9] or d[3] == d[5] == d[7]:
            flag1 = True                    # это условие если определяется победитель

    if n == 9 and flag1 is False:           # это условие при котором наступает ничья
        print("Ничья")
    else:
        print(f'Поздравляем, победил {move[(n-1)%2]}')
        print("Игра окончена")


if __name__ == "__main__":
    start_game()
