import sys
number = int(input())
min_value = sys.maxsize
max_value = -sys.maxsize

for i in range(0, number):
    variable = int(input())
    if variable < min_value:
        min_value = variable
    if variable > max_value:
        max_value = variable

print(f"Max number: {max_value}")
print(f"Min number: {min_value}")
