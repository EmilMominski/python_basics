# Read User's Input
budget = float(input())
days = int(input())
price_per_day = float(input())
extras = int(input())

# Logic
if days <= 7:
    price = price_per_day * days
else:
    price = price_per_day * days - price_per_day * days * 5 / 100
total_price = price + extras * budget / 100

# Print Output
if total_price <= budget:
    print(f"Ivanovi will be left with {budget - total_price:.2f} leva after vacation.")
else:
    print(f"{total_price - budget:.2f} leva needed.")
