# Data Input
resting_days = int(input())

# Logic
flag = True
working_days = 365 - resting_days
play_time = working_days * 63 + resting_days * 127
difference = abs(30000 - play_time)
h = difference // 60
m = difference % 60
if play_time < 30000:
    flag = False

# Print Output
if flag:
    print("Tom will run away")
    print(f"{h} hours and {m} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")
