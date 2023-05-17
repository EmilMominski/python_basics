number = int(input())
left_sum = 0
right_sum = 0

for i in range(0, number * 2):
    variable = int(input())
    if i < number:
        left_sum = left_sum + variable
    else:
        right_sum = right_sum + variable
difference = abs(left_sum - right_sum)

if difference == 0:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")
