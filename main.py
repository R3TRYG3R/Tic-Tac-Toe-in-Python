field = [["###"],
         ["###"],
         ["###"]]

first_row = field[0][0]
second_row = field[1][0]
third_row = field[2][0]
updated_row_list = []

user1 = [] # name, side
user2 = [] # name, side
game_logic = True

def names():
    logic_True = True
    while logic_True:
        name1 = input("player1 enter your name: ").strip()
        if name1 == "":
            print("Enter correct value!")
            continue
        else:
            while True:
                name2 = input("player2 enter your name: ").strip()
                if name2 == "":
                    print("Enter correct value!")
                    continue
                else:
                    print(f"Good luck {name1} and {name2}!")
                    user1.append(name1), user2.append(name2)
                    logic_True = False
                    break

def choosing_sides():
    while True:
        side_user1 = input(f"\n{user1[0]} choose ur side(X | O): ").strip().lower()
        if side_user1 == "x":
            print(f"Good choice! {user2[0]} will play with O")
            user1.append(side_user1)
            user2.append("o")
            break
        elif side_user1 == "o":
            print(f"Good choice! {user2[0]} will play with X")
            user1.append(side_user1)
            user2.append("x")
            break
        else:
            print("Enter correct value!")
            continue

def show_details():
    global game_logic
    print(f"\nLet's go through the details, it means:\n"
          "------------------------------------------\n"
          f"{user1[0]} will play with - {user1[1]}\n"
          f"{user2[0]} will play with - {user2[1]}\n"
          "------------------------------------------\n")
    while True:
        start_game = input("Want to start the game? YES|NO\n").strip().lower()
        if start_game == "yes":
            print("Okay, Lets go!")
            game_logic = True
            break
        elif start_game == "no":
            print("Okay, Bye!")
            game_logic = False
            break

def show_field():
    print("\n------------------------------")
    print(f"""\n\t\t\t{first_row}
\t\t\t{second_row}
\t\t\t{third_row}""")
    print("\n------------------------------")

def clear_field():
    global first_row,second_row,third_row
    first_row = "###"
    second_row = "###"
    third_row = "###"

def start_game():
    global user1_choice_X, user1_choice_Y, user2_choice_X, user2_choice_Y, user1_first_choice, user1_second_choice, user2_first_choice, user2_second_choice
    while game_logic:
        user1_first_choice = True
        while user1_first_choice:
            try:
                user1_choice_X = int(input(f"\n{user1[0]} enter the coordinates(X) where you want to place {user1[1]} :").strip())
            except ValueError:
                print("Enter correct variable!")
                continue
            if user1_choice_X == 1 or user1_choice_X == 2 or user1_choice_X == 3:
                user1_first_choice = False
            else:
                print("Enter correct value!")
                continue
        user1_second_choice = True
        while user1_second_choice:
            try:
                user1_choice_Y = int(input(f"{user1[0]} enter the coordinates(Y) where you want to place {user1[1]} :").strip())
            except ValueError:
                print("Enter correct variable!")
                continue
            if user1_choice_Y == 1 or user1_choice_Y == 2 or user1_choice_Y == 3:
                user1_second_choice = False
                user1_coordinates(user1_choice_X, user1_choice_Y)
            else:
                print("Enter correct value!")
                continue
        user2_first_choice = True
        while user2_first_choice and game_logic == True:
            try:
                user2_choice_X = int(input(f"\n{user2[0]} enter the coordinates(X) where you want to place {user2[1]} :").strip())
            except ValueError:
                print("Enter correct variable!")
                continue
            if user2_choice_X == 1 or user2_choice_X == 2 or user2_choice_X == 3:
                user2_first_choice = False
            else:
                print("Enter correct value!")
                continue
        user2_second_choice = True
        while user2_second_choice and game_logic == True:
            try:
                user2_choice_Y = int(input(f"{user2[0]} enter the coordinates(Y) where you want to place {user2[1]} :").strip())
            except ValueError:
                print("Enter correct variable!")
                continue
            if user2_choice_Y == 1 or user2_choice_Y == 2 or user2_choice_Y == 3:
                user2_second_choice = False
                user2_coordinates(user2_choice_X, user2_choice_Y)
            else:
                print("Enter correct value!")
                continue

def user1_coordinates(x, y):
    global first_row, second_row, third_row, updated_row_list
    x -= 1
    y -= 1
    if 0 <= x <= 2 and y == 0:
        counter = 0
        for symbol in first_row:
            if x == counter:
                if symbol == "#":
                    updated_row_list.append(f"{user1[1]}")
                elif symbol == f"{user2[1]}":
                    print(f"\nU can't change {user2[0]} symbol!")
                    print("You will miss this turn! Do not do that :)")
                    updated_row_list.append(f"{user2[1]}")
                elif symbol == user1[1]:
                    print("\nThere is already such a symbol in this place!"
                          "\nP.S be more careful next time ;)")
                    updated_row_list.append(f"{user1[1]}")
            elif symbol == "o":
                updated_row_list.append("o")
            elif symbol == "x":
                updated_row_list.append("x")
            else:
                updated_row_list.append("#")
            counter += 1
        first_row = "".join(updated_row_list)
        updated_row_list = []
        show_field()
        check_winner()
    if 0 <= x <= 2 and y == 1:
        counter = 0
        for symbol in second_row:
            if x == counter:
                if symbol == "#":
                    updated_row_list.append(f"{user1[1]}")
                elif symbol == f"{user2[1]}":
                    print(f"\nU can't change {user2[0]} symbol!")
                    print("You will miss this turn! Do not do that :)")
                    updated_row_list.append(f"{user2[1]}")
                elif symbol == user1[1]:
                    print("\nThere is already such a symbol in this place!"
                          "\nP.S be more careful next time ;)")
                    updated_row_list.append(f"{user1[1]}")
            elif symbol == "o":
                updated_row_list.append("o")
            elif symbol == "x":
                updated_row_list.append("x")
            else:
                updated_row_list.append("#")
            counter += 1
        second_row = "".join(updated_row_list)
        updated_row_list = []
        show_field()
        check_winner()
    if 0 <= x <= 2 and y == 2:
        counter = 0
        for symbol in third_row:
            if x == counter:
                if symbol == "#":
                    updated_row_list.append(f"{user1[1]}")
                elif symbol == f"{user2[1]}":
                    print(f"\nU can't change {user2[0]} symbol!")
                    print("You will miss this turn! Do not do that :)")
                    updated_row_list.append(f"{user2[1]}")
                elif symbol == user1[1]:
                    print("\nThere is already such a symbol in this place!"
                          "\nP.S be more careful next time ;)")
                    updated_row_list.append(f"{user1[1]}")
            elif symbol == "o":
                updated_row_list.append("o")
            elif symbol == "x":
                updated_row_list.append("x")
            else:
                updated_row_list.append("#")
            counter += 1
        third_row = "".join(updated_row_list)
        updated_row_list = []
        show_field()
        check_winner()

def user2_coordinates(x, y):
    global first_row, second_row, third_row, updated_row_list
    x -= 1
    y -= 1
    if 0 <= x <= 2 and y == 0:
        counter = 0
        for symbol in first_row:
            if x == counter:
                if symbol == "#":
                    updated_row_list.append(f"{user2[1]}")
                elif symbol == f"{user1[1]}":
                    print(f"\nU can't change {user1[0]} symbol!")
                    print("You will miss this turn! Do not do that :)")
                    updated_row_list.append(f"{user1[1]}")
                elif symbol == user2[1]:
                    print("\nThere is already such a symbol in this place!"
                          "\nP.S be more careful next time ;)")
                    updated_row_list.append(f"{user2[1]}")
            elif symbol == "x":
                updated_row_list.append("x")
            elif symbol == "o":
                updated_row_list.append("o")
            else:
                updated_row_list.append("#")
            counter += 1
        first_row = "".join(updated_row_list)
        updated_row_list = []
        show_field()
        check_winner()
    if 0 <= x <= 2 and y == 1:
        counter = 0
        for symbol in second_row:
            if x == counter:
                if symbol == "#":
                    updated_row_list.append(f"{user2[1]}")
                elif symbol == f"{user1[1]}":
                    print(f"\nU can't change {user1[0]} symbol!")
                    print("You will miss this turn! Do not do that :)")
                    updated_row_list.append(f"{user1[1]}")
                elif symbol == user2[1]:
                    print("\nThere is already such a symbol in this place!"
                          "\nP.S be more careful next time ;)")
                    updated_row_list.append(f"{user2[1]}")
            elif symbol == "x":
                updated_row_list.append("x")
            elif symbol == "o":
                updated_row_list.append("o")
            else:
                updated_row_list.append("#")
            counter += 1
        second_row = "".join(updated_row_list)
        updated_row_list = []
        show_field()
        check_winner()
    if 0 <= x <= 2 and y == 2:
        counter = 0
        for symbol in third_row:
            if x == counter:
                if symbol == "#":
                    updated_row_list.append(f"{user2[1]}")
                elif symbol == f"{user1[1]}":
                    print(f"\nU can't change {user1[0]} symbol!")
                    print("You will miss this turn! Do not do that :)")
                    updated_row_list.append(f"{user1[1]}")
                elif symbol == user2[1]:
                    print("\nThere is already such a symbol in this place!"
                          "\nP.S be more careful next time ;)")
                    updated_row_list.append(f"{user2[1]}")
            elif symbol == "x":
                updated_row_list.append("x")
            elif symbol == "o":
                updated_row_list.append("o")
            else:
                updated_row_list.append("#")
            counter += 1
        third_row = "".join(updated_row_list)
        updated_row_list = []
        show_field()
        check_winner()

def check_winner():
    global game_logic,user1_first_choice,user1_second_choice, user2_first_choice, user2_second_choice
    side_user1 = user1[1]
    side_user2 = user2[1]

    if first_row.__contains__("#") or second_row.__contains__("#") or third_row.__contains__("#"):
        if first_row == side_user1+side_user1+side_user1 or first_row == side_user2+side_user2+side_user2:
            print(f"\nGame Ended!")
            game_logic = False
        if second_row == side_user1+side_user1+side_user1 or second_row == side_user2+side_user2+side_user2:
            print(f"\nGame Ended!")
            game_logic = False
        if third_row == side_user1+side_user1+side_user1 or third_row == side_user2+side_user2+side_user2:
            print(f"\nGame Ended!")
            game_logic = False
        if first_row[0] == side_user1 and second_row[0] == side_user1 and third_row[0] == side_user1 or first_row[0] == side_user2 and second_row[0] == side_user2 and third_row[0] == side_user2:
            print(f"\nGame Ended!")
            game_logic = False
        if first_row[1] == side_user1 and second_row[1] == side_user1 and third_row[1] == side_user1 or first_row[1] == side_user2 and second_row[1] == side_user2 and third_row[1] == side_user2:
            print(f"\nGame Ended!")
            game_logic = False
        if first_row[2] == side_user1 and second_row[2] == side_user1 and third_row[2] == side_user1 or first_row[2] == side_user2 and second_row[2] == side_user2 and third_row[2] == side_user2:
            print(f"\nGame Ended!")
            game_logic = False
        if first_row[0] == side_user1 and second_row[1] == side_user1 and third_row[2] == side_user1 or first_row[0] == side_user2 and second_row[1] == side_user2 and third_row[2] == side_user2:
            print(f"\nGame Ended!")
            game_logic = False
        if first_row[2] == side_user1 and second_row[1] == side_user1 and third_row[0] == side_user1 or first_row[2] == side_user2 and second_row[1] == side_user2 and third_row[0] == side_user2:
            print(f"\nGame Ended!")
            game_logic = False
    else:
        print("Draw!")
        game_logic = False
        while True:
            continue_the_game = input("\nDo u want to play again?: YES | NO  ").strip().lower()
            if continue_the_game == "yes":
                print("\nGood luck!")
                clear_field()
                game_logic = True
                start_game()
                break
            elif continue_the_game == "no":
                print("\nGood luck!")
                game_logic = False
                break
            else:
                print("Enter correct value!")
                continue

names()
choosing_sides()
show_details()
start_game()
