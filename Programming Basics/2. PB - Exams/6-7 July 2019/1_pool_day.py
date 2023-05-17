import math

people = int(input())
entrance_fee = float(input())
chair_price = float(input())
umbrella_price = float(input())

total_entrance_fee = people * entrance_fee
total_umbrella_price = math.ceil(people / 2) * umbrella_price
total_chair_price = math.ceil(75 * people / 100) * chair_price
total = total_entrance_fee + total_umbrella_price + total_chair_price

print(f"{total:.2f} lv.")
