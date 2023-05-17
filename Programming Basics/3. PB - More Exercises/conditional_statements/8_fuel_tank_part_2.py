# Data Input
fuel_type = input()    # Gas, Gasoline or Diesel
fuel_amount = float(input())
card = input()    # Yes or No

# Logic
price = 0
discount = 0
if fuel_type == "Gas":
    price += fuel_amount * 0.93
    if card == "Yes":
        price -= fuel_amount * 0.08
elif fuel_type == "Gasoline":
    price += fuel_amount * 2.22
    if card == "Yes":
        price -= fuel_amount * 0.18
elif fuel_type == "Diesel":
    price += fuel_amount * 2.33
    if card == "Yes":
        price -= fuel_amount * 0.12
if 20 <= fuel_amount <= 25:
    discount = price * 8 / 100
elif fuel_amount > 25:
    discount = price * 10 / 100
price -= discount

# Print Output
print(f"{price:.2f} lv.")
