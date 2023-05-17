destination = input()       # France, Italy or Germany
dates = input()     # 21-23, 24-27, 28-31
stay = int(input())

expenses = 0
if destination == "France":
    if dates == "21-23":
        expenses += 30
    elif dates == "24-27":
        expenses += 35
    elif dates == "28-31":
        expenses += 40
elif destination == "Italy":
    if dates == "21-23":
        expenses += 28
    elif dates == "24-27":
        expenses += 32
    elif dates == "28-31":
        expenses += 39
elif destination == "Germany":
    if dates == "21-23":
        expenses += 32
    elif dates == "24-27":
        expenses += 37
    elif dates == "28-31":
        expenses += 43
expenses *= stay

print(f"Easter trip to {destination} : {expenses:.2f} leva.")
