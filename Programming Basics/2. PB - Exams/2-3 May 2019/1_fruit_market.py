strawberry = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())

strawberry_price = strawberry * strawberry_quantity
raspberry = strawberry / 2
raspberry_price = raspberry * raspberry_quantity
orange = raspberry - raspberry * 40 / 100
orange_price = orange * orange_quantity
banana = raspberry - raspberry * 80 / 100
banana_price = banana * banana_quantity
price = strawberry_price + raspberry_price + orange_price + banana_price

print(f"{price:.2f}")
