# Monster Fight Game
# Based on tutorial: https://www.youtube.com/watch?v=kDdTgxv2Vv0
# Author: Andrzej Kocielski
# Created: 02-08-2020
# ------------------------------


game_running = True

while game_running == True:

    new_round = True

    # assign player's variables to a dictionary (in the above sequence)
    player = {"name": "Mighty Player", "attack": 10, "heal": 16, "health": 100}
    # print(player["name"])

    # assign monster's variables to a dictionary (in the above sequence)
    monster = {"name": "Terrible Monster",
               "attack": 12, "heal": 0, "health": 130}

    while new_round == True:

        # Interface / Menu
        print("Select your action:")
        print("-"*19)
        print("1) Attack")
        print("2) Heal")
        print()
        print("Q) Quit game")

        player_choice = input()
        print()

        # the game logic

        player_won = False
        monster_won = False

        if player_choice == "1":
            print("Attacking...")
            monster["health"] = monster["health"] - player["attack"]
            if player["health"] <= 0 or monster["health"] <= 0:
                player_won = True

            else:
                player["health"] = player["health"] - monster["attack"]
                if player["health"] <= 0 or monster["health"] <= 0:
                    print("Player won!")
                    monster_won = True

            print("Player health: ", player["health"])
            print("Monster health: ", monster["health"])
            print()

        elif player_choice == "2":
            print("Healing...")

        elif player_choice == "q" or player_choice == "Q":
            print("Thanks for playing")
            new_round = False
            game_running = False
            # break

        else:
            print("Invalid input")

        if player_won == True or monster_won == True:
            new_round = False


# -----
# if __name__ == "__main__":
#     # execute only if run as a script
#     main()
