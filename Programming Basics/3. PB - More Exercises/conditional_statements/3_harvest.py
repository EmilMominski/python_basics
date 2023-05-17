# Data Input
import math
x = int(input())
y = float(input())
z = int(input())
workers_count = int(input())

# Logic and Print Output
liters_produced = x * y * 40 / (2.5 * 100)
liters_needed = z - liters_produced
if liters_needed > 0:
    liters_needed = math.floor(liters_needed)

    print(f"It will be a tough winter! More {liters_needed} liters wine needed.")

else:
    wine_per_worker = math.ceil(abs(liters_needed / workers_count))
    print(f"Good harvest this year! Total wine: {int(liters_produced)} liters.")
    print(f"{int(abs(liters_needed))} liters left -> {wine_per_worker} liters per person.")
