# Data Input
initial_points = 301
current_points = initial_points
player_name = input()
field = input()    # Single, Double or Triple

# Logic
successful_shots = 0
unsuccessful_shots = 0
flag = False
while field != "Retire":
    points = int(input())
    if field == "Single":
        points *=1
    elif field == "Double":
        points *= 2
    elif field == "Triple":
        points *= 3
    current_points -= points
    if current_points >= 0:
        successful_shots += 1
        if current_points == 0:
            flag = True
            break
    else:
        current_points += points
        unsuccessful_shots += 1

    field = input()

# Print Output
if flag:
    print(f"{player_name} won the leg with {successful_shots} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")