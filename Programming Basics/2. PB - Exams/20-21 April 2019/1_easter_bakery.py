flour_price_per_kg = float(input())
flour_quantity = float(input())
sugar_quantity = float(input())
eggs_packages = int(input())
yeast_packs = int(input())

total_flour_price = flour_price_per_kg * flour_quantity
sugar_price_per_kg = flour_price_per_kg - flour_price_per_kg * 25 / 100
total_sugar_price = sugar_price_per_kg * sugar_quantity
eggs_package_price = flour_price_per_kg + flour_price_per_kg * 10 / 100
total_eggs_price = eggs_package_price * eggs_packages
yeast_pack_price = sugar_price_per_kg - sugar_price_per_kg * 80 / 100
total_yeast_price = yeast_pack_price * yeast_packs
total_price = total_flour_price + total_sugar_price + total_eggs_price + total_yeast_price

print(f"{total_price:.2f}")
