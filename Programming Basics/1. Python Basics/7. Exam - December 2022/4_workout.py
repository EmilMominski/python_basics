import math
days = int(input())
distance = float(input())

total_distance = distance
total = distance
for i in range(days):
    daily = int(input())
    total_distance += total_distance * daily / 100
    total += total_distance

difference = abs(total - 1000)

if total >= 1000:
    print(f"You've done a great job running {math.ceil(difference)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(difference)} more kilometers")
