# Data Input
first_player_name = input()
second_player_name = input()

# Logic
flag = True
first_player_score = 0
second_player_score = 0
first_player = (input())
while first_player != "End of game":
    first_player_card = int(first_player)
    second_player_card = int(input())
    if first_player_card == second_player_card:
        flag = False
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            winner = first_player_name
            winner_score = first_player_score
        elif first_player_card < second_player_card:
            winner = second_player_name
            winner_score = second_player_score
        break
    elif first_player_card > second_player_card:
        first_player_score += first_player_card - second_player_card
    elif first_player_card < second_player_card:
        second_player_score += second_player_card - first_player_card
    first_player = input()
# Print Output
if not flag:
    print("Number wars!")
    print(f"{winner} is winner with {winner_score} points")
else:
    print(f"{first_player_name} has {first_player_score} points")
    print(f"{second_player_name} has {second_player_score} points")