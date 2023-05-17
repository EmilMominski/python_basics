# Read User's Input
steps_text = input()
total_steps = 0
difference = 0
flag = True

# Logic
while steps_text != "Going home":
    steps_digit = int(steps_text)
    total_steps += steps_digit
    if total_steps >= 10000:
        flag = False
        break
    steps_text = input()
if steps_text == "Going home":
    steps_home = int(input())
    total_steps += steps_home
    if total_steps >= 10000:
        flag = False
    else:
        flag = True
difference = abs(total_steps - 10000)
# Print Output
if not flag:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
