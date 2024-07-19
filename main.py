#Code written by Aki

field = [["###"],
         ["###"],
         ["###"]]

def get_row_field():
    return "".join(field[0]), "".join(field[1]), "".join(field[2])


def display_field():
    first_row, second_row, third_row = get_row_field()
    print("\n------------------------------")
    print(f"\n\t\t\t{first_row}\n\t\t\t{second_row}\n\t\t\t{third_row}")
    print("\n------------------------------")


def clear_field():
    global field
    field = [["###"], ["###"], ["###"]]


def input_valid_coordinate(prompt):
    while True:
        try:
            coordinate = int(input(prompt).strip())
            if 1 <= coordinate <= 3:
                return coordinate
            else:
                print("Введите значение от 1 до 3.")
        except ValueError:
            print("Введите правильное числовое значение.")


def player_turn(player, symbol):
    x = input_valid_coordinate(f"\n{player} введите координаты (X) для {symbol}: ") - 1
    y = input_valid_coordinate(f"{player} введите координаты (Y) для {symbol}: ") - 1
    if field[y][0][x] == "#":
        field[y][0] = field[y][0][:x] + symbol + field[y][0][x + 1:]
        display_field()
    else:
        print("Место уже занято, пропуск хода.")


def check_winner():
    first_row, second_row, third_row = get_row_field()
    rows = [first_row, second_row, third_row]
    columns = ["".join([first_row[i], second_row[i], third_row[i]]) for i in range(3)]
    diagonals = [first_row[0] + second_row[1] + third_row[2], first_row[2] + second_row[1] + third_row[0]]
    lines = rows + columns + diagonals
    for line in lines:
        if line == "xxx" or line == "ooo":
            return True
    return not any("#" in row for row in rows)


def start_game():
    while True:
        player1 = input("Игрок 1, введите ваше имя: ").strip()
        player2 = input("Игрок 2, введите ваше имя: ").strip()
        if player1 == "" or player2 == "":
            print("Введите ваше имя!")
            continue
        else:
            print(f"Удачи, {player1} и {player2}!")
            break

    while True:
        side = input(f"{player1}, выберите сторону (X или O): ").strip().lower()
        if side in ["x", "o"]:
            side1, side2 = ("x", "o") if side == "x" else ("o", "x")
            break
        else:
            print("Введите правильное значение (X или O).")

    print(f"{player1} играет за {side1}, {player2} играет за {side2}")
    display_field()

    current_player, current_side = player1, side1
    while True:
        player_turn(current_player, current_side)
        if check_winner():
            print(f"Игра окончена! Победитель: {current_player}")
            break
        current_player, current_side = (player2, side2) if current_player == player1 else (player1, side1)

    while True:
        choice = input("Хотите сыграть снова? (yes/no): ").strip().lower()
        if choice == "yes":
            clear_field()
            start_game()
            break
        elif choice == "no":
            print("\nGood luck! (👉ﾟヮﾟ)👉")
            break
        else:
            print("Введите правильное значение!")
            continue

start_game()
