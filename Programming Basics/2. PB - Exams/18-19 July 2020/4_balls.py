# Read User's Input
import math
number = int(input())

# Logic
points = 0
red_counter = 0
orange_counter = 0
yellow_counter = 0
white_counter = 0
black_counter = 0
other_colour_counter = 0

for i in range(number):
    colour = input()
    if colour == "red":
        red_counter += 1
        points += 5
    elif colour == "orange":
        orange_counter += 1
        points += 10
    elif colour == "yellow":
        yellow_counter += 1
        points += 15
    elif colour == "white":
        white_counter += 1
        points += 20
    elif colour == "black":
        black_counter += 1
        points = math.floor(points - points / 2)
    else:
        other_colour_counter += 1
        points = points

# Print Output
print(f"Total points: {points}")
print(f"Red balls: {red_counter}")
print(f"Orange balls: {orange_counter}")
print(f"Yellow balls: {yellow_counter}")
print(f"White balls: {white_counter}")
print(f"Other colors picked: {other_colour_counter}")
print(f"Divides from black balls: {black_counter}")
