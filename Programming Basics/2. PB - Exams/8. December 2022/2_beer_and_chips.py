import math
name = input()
budget = float(input())
beer_bottles = int(input())
chips_packs = int(input())

beer_price = beer_bottles * 1.2
price_per_chips_pack = beer_price * 45 / 100
chips_price = math.ceil(price_per_chips_pack * chips_packs)
total_price = beer_price + chips_price
difference = abs(total_price - budget)

if budget >= total_price:
    print(f"{name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{name} needs {difference:.2f} more leva!")
