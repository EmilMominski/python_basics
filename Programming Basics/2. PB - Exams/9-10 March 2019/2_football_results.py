# Data Input
first_game_result = input()
second_game_result = input()
third_game_result = input()

# Logic
won = 0
lost = 0
drawn = 0
if first_game_result[0] > first_game_result[2]:
    won += 1
elif first_game_result[0] < first_game_result[2]:
    lost += 1
else:
    drawn += 1
if second_game_result[0] > second_game_result[2]:
    won += 1
elif second_game_result[0] < second_game_result[2]:
    lost += 1
else:
    drawn += 1
if third_game_result[0] > third_game_result[2]:
    won += 1
elif third_game_result[0] < third_game_result[2]:
    lost += 1
else:
    drawn += 1

# Print Output
print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")
