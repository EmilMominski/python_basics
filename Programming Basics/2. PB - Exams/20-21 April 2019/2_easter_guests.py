import math
guests_quantity = int(input())
budget = int(input())

easter_bread_quantity = math.ceil(guests_quantity / 3)
easter_bread_price = easter_bread_quantity * 4
eggs_quantity = guests_quantity * 2
eggs_price = eggs_quantity * 0.45
price = easter_bread_price + eggs_price
difference = abs(price - budget)

if budget >= price:
    print(f"Lyubo bought {easter_bread_quantity} Easter bread and {eggs_quantity} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")
