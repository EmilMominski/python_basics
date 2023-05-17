number = int(input())

for i in range(number + 1):
    print((number - i) * " ", end="")
    print(i * "*", end="")
    print(" | ", end="")
    print(i * "*", end="")
    print((number - i) * " ")
    