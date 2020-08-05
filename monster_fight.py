# Monster Fight Game
# Author: Andrzej Kocielski
# Created: 02-08-2020
# Based on tutorial by Manuel Lorenz: https://www.youtube.com/watch?v=kDdTgxv2Vv0
# ------------------------------

# -----
# importing libraries
from random import randint


# -----
# game main code block
def main():

    game_running = True

    # set fights counter
    fight_counter = 0

    # initiate empty list of game results
    game_stats = []

    # the outer 'while' loop
    while game_running == True:

        # increment fight counter
        fight_counter = fight_counter + 1

        # set a round counter
        round_counter = 0

        new_round = True

        # assign player's variables to a dictionary (in the above sequence)
        player = {"name": "Mighty Player",
                  "attack": 10, "heal": 36, "health": 60}
        # print(player["name"])

        # assign monster's variables to a dictionary (in the above sequence)
        monster = {"name": "Terrible Monster",
                   "attack_min": 10, "attack_max": 20, "heal": 0, "health": 70}

        # the inner 'while' loop
        while new_round == True:

            # increment round counter
            round_counter = round_counter + 1

            # Interface / Menu
            print("Select your action:")
            print("-"*19)
            print("1) Attack")
            print("2) Heal")
            print("3) Show stats")
            print()
            print("Q) Quit game")

            player_choice = input()
            print()

            # the game logic

            player_won = False
            monster_won = False

            # Choice 1 - player attacks
            if player_choice == "1":
                print("Player attacks...")
                monster["health"] = monster["health"] - player["attack"]
                # check if monster defeated
                if player["health"] <= 0 or monster["health"] <= 0:
                    round_result = {"fight": fight_counter,
                                    "name": player["name"], "health": player["health"], "rounds": round_counter}
                    game_stats.append(round_result)
                    end_game(player["name"], round_counter, round_result)
                    player_won = True

                # monster retaliates
                else:
                    print("Monster retaliates...")
                    player["health"] = player["health"] - \
                        calculate_monster_attack(
                            monster["attack_min"], monster["attack_max"])
                    # check if player defeated
                    if player["health"] <= 0 or monster["health"] <= 0:
                        round_result = {"fight": fight_counter,
                                        "name": player["name"], "health": player["health"], "rounds": round_counter}
                        game_stats.append(round_result)
                        end_game(monster["name"], round_counter, round_result)
                        monster_won = True

            # Choice 2 - player heals onself
            elif player_choice == "2":
                print("Healing...")
                player["health"] = player["health"] + player["heal"]

                # monster retalites
                print("Monster retaliates...")
                player["health"] = player["health"] - \
                    calculate_monster_attack(
                        monster["attack_min"], monster["attack_max"])
                # check if player defeated
                if player["health"] <= 0 or monster["health"] <= 0:
                    round_result = {"fight": fight_counter,
                                    "name": player["name"], "health": player["health"], "rounds": round_counter}
                    game_stats.append(round_result)
                    end_game(player["name"], round_counter, round_result)
                    monster_won = True

            # Choice 3 - show the game stats
            elif player_choice == "3":
                for game_stat in game_stats:
                    print(game_stat)

            # Choice Q - quittint the game
            elif player_choice == "q" or player_choice == "Q":
                print("Thanks for playing")
                # first (inner) 'while' loop exit
                new_round = False
                # second (outer) 'while' loop exit
                game_running = False

            # in case of hitting a wrong key
            else:
                print("Invalid input")

            # stating the fight summary statistics
            if player_won == False and monster_won == False:
                print("Player health: ", player["health"])
                print("Monster health: ", monster["health"])
                print()

            # end of round condition - inner 'while' loop exit
            if player_won == True or monster_won == True:
                new_round = False


# define random attack strength
def calculate_monster_attack(att_min, att_max):
    return randint(att_min, att_max)
    # return randint(10, 18)


def end_game(winner_name, round_no, stats):
    print(f"{winner_name} won the fight in {round_no} rounds!")
    print(f"{stats}")
    print()


# -----

if __name__ == "__main__":
    # execute only if run as a script
    main()
