# Read User's Input
import sys
player_name = input()
goals_scored = int(input())

# Logic
max_goals = -sys.maxsize
while player_name != "END":
    if goals_scored > max_goals:
        max_goals = goals_scored
        best_player = player_name
    if goals_scored >= 10:
        break
    player_name = input()
    if player_name == "END":
        continue
    goals_scored = int(input())

# Print Output
print(f"{best_player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
