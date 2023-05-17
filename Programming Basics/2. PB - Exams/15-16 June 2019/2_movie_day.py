shooting_time = int(input())
scenes_count = int(input())
scene_duration = int(input())

preparation_time = shooting_time * 15 / 100
time_required = scenes_count * scene_duration + preparation_time
difference = abs(time_required - shooting_time)

if shooting_time >= time_required:
    print(f"You managed to finish the movie on time! You have {round(difference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(difference)} minutes.")
