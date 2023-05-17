hour = int(input())
minutes = int(input())

new_time_minutes = minutes + 15

if new_time_minutes >= 60:
    hour = hour + 1
    new_time_minutes = new_time_minutes - 60

if hour >= 24:
    hour = hour - 24

if new_time_minutes < 10:
    print(f"{hour}:0{new_time_minutes}")
else:
    print(f"{hour}:{new_time_minutes}")
