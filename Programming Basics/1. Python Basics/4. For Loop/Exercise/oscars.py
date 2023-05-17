actor_name = input()
academy_points = float(input())
jury = int(input())
jury_score = 0
score = academy_points

for i in range(0, jury):
    jury_name = input()
    jury_points = float(input())
    jury_score = len(jury_name) * jury_points / 2
    score = score + jury_score
    if score >= 1250.5:
        print(f"Congratulations, {actor_name} "
          f"got a nominee for leading role with {score:.1f}!")
        break

difference = abs(score - 1250.5)
if score < 1250.5:
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
