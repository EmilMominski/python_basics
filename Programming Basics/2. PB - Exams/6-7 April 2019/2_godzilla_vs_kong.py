# Data Input
budget = float(input())
actors = int(input())
price_for_clothing_per_actor = float(input())

#Logic
decoration = budget * 10 / 100
price_for_clothing = actors * price_for_clothing_per_actor
if actors > 150:
    price_for_clothing -= price_for_clothing * 10 / 100
expences = decoration + price_for_clothing
difference = budget - expences

#Print Output
if difference < 0:
    difference = abs(difference)
    print(f"Not enough money!\nWingard needs {difference:.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {difference:.2f} leva left.")

