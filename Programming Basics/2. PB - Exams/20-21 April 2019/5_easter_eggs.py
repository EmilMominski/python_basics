import sys
coloured_eggs_quantity = int(input())

max_count = -sys.maxsize
red_eggs_counter = 0
orange_eggs_counter = 0
blue_eggs_counter = 0
green_eggs_counter = 0
colour = ""

for i in range(coloured_eggs_quantity):
    egg_colour = input()        # red, orange, blue or green
    if egg_colour == "red":
        red_eggs_counter += 1
    elif egg_colour == "orange":
        orange_eggs_counter += 1
    elif egg_colour == "blue":
        blue_eggs_counter += 1
    elif egg_colour == "green":
        green_eggs_counter += 1
if red_eggs_counter > max_count:
    max_count = red_eggs_counter
    colour = "red"
if orange_eggs_counter > max_count:
    max_count = orange_eggs_counter
    colour = "orange"
if blue_eggs_counter > max_count:
    max_count = blue_eggs_counter
    colour = "blue"
if green_eggs_counter > max_count:
    max_count = green_eggs_counter
    colour = "green"

print(f"Red eggs: {red_eggs_counter}")
print(f"Orange eggs: {orange_eggs_counter}")
print(f"Blue eggs: {blue_eggs_counter}")
print(f"Green eggs: {green_eggs_counter}")
print(f"Max eggs: {max_count} -> {colour}")
