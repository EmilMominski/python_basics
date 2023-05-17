# Data Input
height_house = float(input())    # x
length_house = float(input())    # y
height_roof = float(input())    # h

# Logic
green_area = 2 * height_house * (height_house + length_house) - 2 * 1.2 - 2 * 1.5 ** 2
green_paint = green_area / 3.4
red_area = height_house * (2 * length_house + height_roof)
red_paint = red_area / 4.3

# Print Output
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
