import math
number = int(input())

# printing the roof
stars = 1
if number % 2 == 0:
    stars += 1
roof_length = math.ceil(number / 2)
for i in range(roof_length):
    padding = (number - stars) // 2
    line = "-" * padding \
        + "*" * stars \
        + "-" * padding
    print(line)
    stars += 2

# printing the body
for i in range(number // 2):
    line = "|" + "*" * (number - 2) + "|"
    print(line)
