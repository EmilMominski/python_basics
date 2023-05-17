number = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0

for i in range(0, number):
    variable = int(input())
    if variable < 200:
        group_1 = group_1 + 1
    elif variable <= 399:
        group_2 = group_2 + 1
    elif variable <= 599:
        group_3 = group_3 + 1
    elif variable <= 799:
        group_4 = group_4 + 1
    else:
        group_5 = group_5 + 1

percent_1 = group_1 * 100 / number
percent_2 = group_2 * 100 / number
percent_3 = group_3 * 100 / number
percent_4 = group_4 * 100 / number
percent_5 = group_5 * 100 / number

print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")
