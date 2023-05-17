# Read User's Input
football_team = input()
games_played = int(input())

# Logic
win_counter = 0
equal_counter = 0
lost_counter = 0
score = 0
percent_games_won = 0
result = ""
flag = True
if games_played == 0:
    flag = False
else:
    for i in range(games_played):
        result = input()        # W, D, or L
        if result == "W":
            score += 3
            win_counter += 1
        elif result == "D":
            score += 1
            equal_counter += 1
        elif result == "L":
            lost_counter += 1
    percent_games_won = win_counter * 100 / games_played

# Print Output
if not flag:
    print(f"{football_team} hasn't played any games during this season.")
else:
    print(f"{football_team} has won {score} points during this season.")
    print("Total stats:")
    print(f"## W: {win_counter}")
    print(f"## D: {equal_counter}")
    print(f"## L: {lost_counter}")
    print(f"Win rate: {percent_games_won:.2f}%")
