rent = float(input())

cake_price = rent * 20 / 100
drinks_price = cake_price - cake_price * 45 / 100
clown_price = rent / 3
budget = rent + cake_price + drinks_price + clown_price

print(budget)
