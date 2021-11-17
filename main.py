def input_game():
    print("Please enter a game number.")
    while True:
        try:
            game_id = int(input("> "))
            return game_id
        except ValueError:
            print("Invalid game id")


def get_game_file():
    game_id = input_game()
    return open("./game_" + str(game_id) + ".txt", "w")


def create_game():
    game_file = get_game_file()

    print("Please enter a home team name.")
    h_team_name = input("> ")
    game_file.write(h_team_name + '\n')

    print("Please enter a visiting team name.")
    v_team_name = input("> ")
    game_file.write(v_team_name + '\n')

    print("Game created")
    game_file.close()


def enter_scores():
    pass

def print_game():
    pass

def main():
    while True:
        print("Please choose one of the following by typing a number:")
        print("(1) Create game")
        print("(2) Enter scores")
        print("(3) Print game")
        print("(4) Exit")
        choice = input("> ")
        if choice == "1":
            create_game()
        elif choice == "2":
            enter_scores()
        elif choice == "3":
            print_game()
        elif choice == "4":
            return
        else:
            print("Invalid choice!")


main()
