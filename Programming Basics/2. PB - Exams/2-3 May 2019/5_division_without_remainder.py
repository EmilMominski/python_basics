number = int(input())
counter_2 = 0
counter_3 = 0
counter_4 = 0

for i in range(number):
    digit = int(input())
    if digit % 2 == 0:
        counter_2 += 1
    if digit % 3 == 0:
        counter_3 += 1
    if digit % 4 == 0:
        counter_4 += 1

p2 = counter_2 * 100 / number
p3 = counter_3 * 100 / number
p4 = counter_4 * 100 / number

print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
