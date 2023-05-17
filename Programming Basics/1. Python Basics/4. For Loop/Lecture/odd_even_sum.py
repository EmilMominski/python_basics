number = int(input())
even_sum = 0
odd_sum = 0

for i in range(0, number):
    variable = int(input())
    if i % 2 == 0:
        even_sum = even_sum + variable
    else:
        odd_sum = odd_sum + variable
difference = abs(even_sum - odd_sum)

if difference == 0:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {difference}")
