# Read User's Input
actor_name = input()
academy_points = float(input())
jury_count = int(input())

# Logic
total_points = academy_points
flag = True
for _ in range(jury_count):
    jury_name = input()
    jury_points = float(input())
    total_points += len(jury_name) * jury_points / 2
    if total_points > 1250.5:
        flag = False
        break

# Print Output
if not flag:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = abs(total_points - 1250.5)
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
