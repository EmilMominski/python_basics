number = int(input())

for i in range(1, number + 1):
    print((number - i) * " " + "*", end=" ")
    for j in range(0, i - 1):
        print("*", end=" ")
    print()
for i in range(number - 1, 0, -1):
    print((number - i) * " " + "*", end=" ")
    for j in range(1, i):
        print("*", end=" ")
    print()
