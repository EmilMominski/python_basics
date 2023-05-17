number = int(input())
even_power = 0

for i in range(0, number + 1):
    if i % 2 == 0:
        even_power = 2 ** i
        print(even_power)
