import math
print("Please choose between square, rectangle, circle or triangle: ", end='')
figure = input()    # square, rectangle, circle or triangle
area = 0
if figure == "square":
    length_square = float(input())
    area = length_square * length_square
elif figure == "rectangle":
    length_rectangle = float(input())
    width_rectangle = float(input())
    area = length_rectangle * width_rectangle
elif figure == "circle":
    radius = float(input())
    area = math.pi * radius ** 2
elif figure == "triangle":
    length_triangle = float(input())
    height_triangle = float(input())
    area = length_triangle * height_triangle / 2
print(f"{area:.3f}")
