# Monster Fight Game
# Based on tutorial: https://www.youtube.com/watch?v=kDdTgxv2Vv0
# Author: Andrzej Kocielski
# Created: 02-08-2020
# ------------------------------

# -----
# assign player's variables to a dictionary (in the above sequence)
player = {"name": "Mighty Player", "attack": 10, "heal": 16, "health": 100}
# print(player["name"])

# assign monster's variables to a dictionary (in the above sequence)
monster = {"name": "Terrible Monster", "attack": 12, "heal": 0, "health": 130}

# -----
# Interface / Menu
print("Select your action:")
print("1) Attack")
print("2) Heal")

player_choice = input()
print()

if player_choice == "1":
    print("Attacking...")
    monster["health"] = monster["health"] - player["attack"]
    player["health"] = player["health"] - monster["attack"]
    print("Player health: ", player["health"])
    print("Monster health: ", monster["health"])
    print()

elif player_choice == "2":
    print("Healing...")
else:
    print("Invalid input")


# -----
# if __name__ == "__main__":
#     # execute only if run as a script
#     main()
