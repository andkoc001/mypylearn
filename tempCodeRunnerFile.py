
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

