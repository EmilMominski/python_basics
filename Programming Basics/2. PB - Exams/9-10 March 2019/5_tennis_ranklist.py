# Data Input
import math
tournament_count = int(input())
initial_score = int(input())

# Logic
current_score = 0
won_tournaments = 0
for i in range(tournament_count):
    result = input()    # W, F or SF
    if result == "W":
        won_tournaments += 1
        current_score += 2000
    elif result == "F":
        current_score += 1200
    elif result == "SF":
        current_score += 720
score = current_score + initial_score
average_score = math.floor(current_score / tournament_count)
average_percent = won_tournaments * 100 / tournament_count

# Print Output
print(f"Final points: {score}")
print(f"Average points: {average_score}")
print(f"{average_percent:.2f}%")