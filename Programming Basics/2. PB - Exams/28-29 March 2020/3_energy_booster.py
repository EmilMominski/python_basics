fruit = input()     # Watermelon, Mango, Pineapple, or Raspberry
set_size = input()      # small or big
sets_amount = int(input())

price = 0
if set_size == "small":
    if fruit == "Watermelon":
        price += 56
    elif fruit == "Mango":
        price += 36.66
    elif fruit == "Pineapple":
        price += 42.1
    elif fruit == "Raspberry":
        price += 20
    price *= 2
elif set_size == "big":
    if fruit == "Watermelon":
        price += 28.7
    elif fruit == "Mango":
        price += 19.6
    elif fruit == "Pineapple":
        price += 24.8
    elif fruit == "Raspberry":
        price += 15.2
    price *= 5
total_price = price * sets_amount
if 400 <= total_price <= 1000:
    total_price -= total_price * 15 / 100
elif total_price > 1000:
    total_price -= total_price * 50 / 100

print(f"{total_price:.2f} lv.")
