# Data Input
annual_fee = int(input())

# Logic
shoes = annual_fee * (1 - 40 / 100)
clothing = shoes * (1 - 20 / 100)
ball = clothing / 4
extras = ball / 5
total = annual_fee + shoes + clothing + ball + extras

# Print Output
print(f"{total:.2f}")
