# Data Input
import math
price_per_single_tennis = float(input())
tennis_amount = int(input())
shoes_amount = int(input())

# Logic
n = tennis_amount * price_per_single_tennis
m = price_per_single_tennis / 6 * shoes_amount
equipment = (n + m) * 20 / 100
total = n + m + equipment
price_to_be_paid_by_djokovic = math.floor(total / 8)
price_to_be_paid_by_sponsors =  math.ceil(total * 7 / 8)

# Print Output
print(f"Price to be paid by Djokovic {price_to_be_paid_by_djokovic}")
print(f"Price to be paid by sponsors {price_to_be_paid_by_sponsors}")
