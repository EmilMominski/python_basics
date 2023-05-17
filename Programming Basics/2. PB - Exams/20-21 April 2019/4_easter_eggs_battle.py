eggs_quantity_first_player = int(input())
eggs_quantity_second_player = int(input())

remaining_eggs_first_player = eggs_quantity_first_player
remaining_eggs_second_player = eggs_quantity_second_player

while True:
    winner = input()
    if winner == "End":
        print(f"Player one has {remaining_eggs_first_player} eggs left.")
        print(f"Player two has {remaining_eggs_second_player} eggs left.")
        break
    if winner == "one":
        remaining_eggs_second_player -= 1
    elif winner == "two":
        remaining_eggs_first_player -= 1
    if remaining_eggs_first_player == 0:
        print(f"Player one is out of eggs. Player two has {remaining_eggs_second_player} eggs left.")
        break
    if remaining_eggs_second_player == 0:
        print(f"Player two is out of eggs. Player one has {remaining_eggs_first_player} eggs left.")
        break

