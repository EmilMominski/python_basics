cake_type = input()
cake_purchased = int(input())
day = int(input())

price = 0
if day <= 15:
    if cake_type == "Cake":
        price += 24
    elif cake_type == "Souffle":
        price += 6.66
    elif cake_type == "Baklava":
        price += 12.6
elif day > 15:
    if cake_type == "Cake":
        price += 28.7
    elif cake_type == "Souffle":
        price += 9.8
    elif cake_type == "Baklava":
        price += 16.98
price *= cake_purchased

if day <= 22:
    if 100 <= price <= 200:
        price -= price * 15 / 100
    elif price > 200:
        price -= price * 25 / 100
    if day <= 15:
        price -= price * 10 / 100

print(f"{price:.2f}")
