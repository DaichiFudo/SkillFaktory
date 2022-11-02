def wel_screen():
    print("\n Приветствуем вас!", "\n     это игра", "\n крестики - нолики")
    print(" \n форма ввода: a - строка ", "\n              b - столбец", "\n\n Да победит хитрейший!")


field = [[" "] * 3 for i in range(3)]
count = 0


def play_field():
    print()
    print("    | 0 | 1 | 2 | ")
    for i in range(3):
        str_inf = f"  {i} | {' | '.join(field[i])} | "
        print(str_inf)
    print()


def request():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Необходимо ввести 2 координаты! ")
            continue

        a, b = cords

        if not (a.isdigit()) or not (b.isdigit()):
            print(" Необходимо ввести числа! ")
            continue

        a, b = int(a), int(b)

        if 0 > a or a > 2 or 0 > b or b > 2:
            print(" Не придумывай новых координат! ")
            continue

        if field[a][b] != " ":
            print(" Не мухлюё! ")
            continue

        return a, b


def validate():
    win_coordinate = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                      ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                      ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_coordinate:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Победил X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победил 0!!!")
            return True
    return False


wel_screen()

while True:
    count += 1
    play_field()
    if count % 2 == 1:
        print(" Ход крестика!")
    else:
        print(" Ход нолика!")

    a, b = request()

    if count % 2 == 1:
        field[a][b] = "X"
    else:
        field[a][b] = "0"

    if validate():
        break

    if count == 9:
        print(" Ничья!")
        break
