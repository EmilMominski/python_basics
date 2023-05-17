# Read User's Input
cpu_price_usd = float(input())
gpu_price_usd = float(input())
ram_price_usd = float(input())
ram_count = int(input())
discount = float(input())

# Logic
cpu_price = cpu_price_usd * 1.57
cpu_discounted = cpu_price - cpu_price * discount
gpu_price = gpu_price_usd * 1.57
gpu_discounted = gpu_price - gpu_price * discount
ram_price = ram_price_usd * ram_count * 1.57
price = cpu_discounted + gpu_discounted + ram_price

# Print Output
print(f"Money needed - {price:.2f} leva.")
