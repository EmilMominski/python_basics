price_per_page = float(input())
price_per_cover_page = float(input())
discount = int(input())
designer_price = float(input())
initial_percent_paid = int(input())

money = 899 * price_per_page + 2 * price_per_cover_page
money -= money * discount / 100
money += designer_price
money -= money * initial_percent_paid / 100

print(f"Avtonom should pay {money:.2f} BGN.")
