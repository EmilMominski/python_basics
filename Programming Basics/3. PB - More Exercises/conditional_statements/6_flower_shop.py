# Data Input
import math
m_amount = int(input())
z_amount = int(input())
roses_amount = int(input())
cactus_amount = int(input())
present_price = float(input())

# Logic
m_price = m_amount * 3.25
z_price = z_amount * 4
roses_price = roses_amount * 3.5
cactus_price = cactus_amount * 8
total_price = m_price + z_price + roses_price + cactus_price
price_after_tax = total_price * (1 - 5 / 100)
difference = abs(present_price - price_after_tax)

# Print Output
if price_after_tax >= present_price:
    difference = math.floor(difference)
    print(f"She is left with {difference} leva.")
else:
    difference = math.ceil(difference)
    print(f"She will have to borrow {difference} leva.")
