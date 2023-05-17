budget = float(input())
fuel = float(input())
day = input()       # Saturday or Sunday

fuel_cost = fuel * 2.1
tour_guide = 100
price = fuel_cost + tour_guide
if day == "Saturday":
    price -= price * 10 / 100
elif day == "Sunday":
    price -= price * 20 / 100
difference = abs(price - budget)
if budget >= price:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")
