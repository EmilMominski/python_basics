# Data Input
vegetable_price_per_kilo = float(input())
fruit_price_per_kilo = float(input())
vegetable_kilos = int(input())
fruit_kilos = int(input())

# Logic
vegetables = vegetable_price_per_kilo * vegetable_kilos
fruit = fruit_price_per_kilo * fruit_kilos
total = (vegetables + fruit) / 1.94

# Print Output
print(f"{total:.2f}")
