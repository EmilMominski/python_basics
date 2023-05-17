# Read User's Input
drink = input()     # Espresso, Cappuccino, or Tea
sugar = input()     # Without, Normal, or Extra
drinks_quantity = int(input())

# Logic
price = 0
if drink == "Espresso":
    if sugar == "Without":
        price = 0.9 - 0.9 * 35 / 100
    elif sugar == "Normal":
        price += 1
    elif sugar == "Extra":
        price += 1.2
    if drinks_quantity >= 5:
        price = price - price * 25 / 100
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1 - 35 / 100
    elif sugar == "Normal":
        price += 1.2
    elif sugar == "Extra":
        price += 1.6
elif drink == "Tea":
    if sugar == "Without":
        price = 0.5 - 0.5 * 35 / 100
    elif sugar == "Normal":
        price += 0.6
    elif sugar == "Extra":
        price += 0.7
total_price = price * drinks_quantity
if total_price > 15:
    total_price = total_price - total_price * 20 / 100

# Print Output
print(f"You bought {drinks_quantity} cups of {drink} for {total_price:.2f} lv.")
