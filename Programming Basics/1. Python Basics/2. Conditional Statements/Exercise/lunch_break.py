import math

title = input()
duration_of_series = int(input())
break_duration = int(input())

time_to_eat_lunch = break_duration / 8
time_to_rest = break_duration / 4
remaining_time = break_duration - time_to_eat_lunch - time_to_rest
difference = math.ceil(abs(remaining_time - duration_of_series))

if remaining_time >= duration_of_series:
    print(f"You have enough time to watch {title} and left with "
          f"{difference} minutes free time.")
elif remaining_time < duration_of_series:
    print(f"You don't have enough time to watch {title}, you need "
          f"{difference} more minutes.")
