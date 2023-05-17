egg_size = input()      # Large, Medium or Small
egg_colour = input()        # Red, Green or Yellow
quantity = int(input())

expenses = 0
if egg_size == "Large":
    if egg_colour == "Red":
        expenses += 16
    elif egg_colour == "Green":
        expenses += 12
    elif egg_colour == "Yellow":
        expenses += 9
elif egg_size == "Medium":
    if egg_colour == "Red":
        expenses += 13
    elif egg_colour == "Green":
        expenses += 9
    elif egg_colour == "Yellow":
        expenses += 7
elif egg_size == "Small":
    if egg_colour == "Red":
        expenses += 9
    elif egg_colour == "Green":
        expenses += 8
    elif egg_colour == "Yellow":
        expenses += 5
expenses *= quantity
expenses -= expenses * 35 / 100

print(f"{expenses:.2f} leva.")
