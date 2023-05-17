# Read User's Input
import math
tournaments = int(input())
initial_score = int(input())
score = 0
won_tournaments = 0

# Logic
for i in range(0, tournaments):
    tournament_level = input()      # W, F, or SF
    if tournament_level == "W":
        score = score + 2000
        won_tournaments = won_tournaments + 1
    elif tournament_level == "F":
        score = score + 1200
    elif tournament_level == "SF":
        score = score + 720
total_score = initial_score + score
average_score = score / tournaments
won_percent = won_tournaments * 100 / tournaments

# Print Output
print(f"Final points: {total_score}")
print(f"Average points: {math.floor(average_score)}")
print(f"{won_percent:.2f}%")
