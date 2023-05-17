# Read User's Input
import math
wall_height = int(input())
wall_width = int(input())
not_painted = int(input())
liters_paint = input()

# Logic
digit_paint = 0
square_meters_wall = wall_height * wall_width
total_square_meters = square_meters_wall * 4
square_meters_to_paint = math.ceil(total_square_meters - total_square_meters * not_painted / 100)

while liters_paint != "Tired!":
    digit_paint = int(liters_paint)
    square_meters_to_paint -= digit_paint
    if square_meters_to_paint < 0:
        print(f"All walls are painted and you have {abs(square_meters_to_paint)} l paint left!")
        break
    elif square_meters_to_paint == 0:
        print("All walls are painted! Great job, Pesho!")
        break
    liters_paint = input()

# Print Output
if square_meters_to_paint > 0:
    print(f"{square_meters_to_paint} quadratic m left.")
