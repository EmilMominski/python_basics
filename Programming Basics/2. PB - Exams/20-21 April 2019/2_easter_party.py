guests = int(input())
price_per_guest = float(input())
budget = float(input())

price = price_per_guest
if 10 <= guests <= 15:
    price -= price * 15 / 100
elif 15 < guests <= 20:
    price -= price * 20 / 100
elif guests > 20:
    price -= price * 25 / 100
else:
    price = price
price *= guests
cake_price = budget * 10 / 100
price += cake_price
difference = abs(price - budget)

if budget >= price:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")
