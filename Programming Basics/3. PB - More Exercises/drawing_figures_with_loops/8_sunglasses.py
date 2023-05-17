number = int(input())

# printing the top part
print(number * 2 * "*", end="")
print(number * " ", end="")
print(number * 2 * "*")

# printing the middle part
for row in range(number - 2):
    print("*", end="")
    for slash in range(number * 2 - 2):
        print("/", end="")
    print("*", end="")
    if row == (number - 1) // 2 - 1:
        print(number * "|", end="")
    else:
        print(number * " ", end="")
    print("*", end="")
    for slash in range(number * 2 - 2):
        print("/", end="")
    print("*", end="")
    print()

# printing the bottom part
print(number * 2 * "*", end="")
print(number * " ", end="")
print(number * 2 * "*")
