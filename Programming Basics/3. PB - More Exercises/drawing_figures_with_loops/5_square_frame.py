number = int(input())

for row in range(1, number + 1):
    if row == 1 or row == number:
        print("+", end="")
        print((number - 2) * " -", end="")
        print(" +", end="")
    else:
        print("|", end="")
        print((number - 2) * " -", end="")
        print(" |", end="")
    print()
