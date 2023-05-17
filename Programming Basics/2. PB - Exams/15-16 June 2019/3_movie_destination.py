budget = float(input())
destination = input()       # Dubai, Sofia, London
season = input()        # Summer or Winter
days = int(input())

price_per_day = 0
if season == "Winter":
    if destination == "Dubai":
        price_per_day += 45000
    elif destination == "Sofia":
        price_per_day += 17000
    elif destination == "London":
        price_per_day += 24000
elif season == "Summer":
    if destination == "Dubai":
        price_per_day += 40000
    elif destination == "Sofia":
        price_per_day += 12500
    elif destination == "London":
        price_per_day += 20250
price_for_all_days = price_per_day * days
if destination == "Dubai":
    total_price = price_for_all_days - price_for_all_days * 30 / 100
elif destination == "Sofia":
    total_price = price_for_all_days + price_for_all_days * 25 / 100
else:
    total_price = price_for_all_days
difference = abs(budget - total_price)
if budget >= total_price:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
