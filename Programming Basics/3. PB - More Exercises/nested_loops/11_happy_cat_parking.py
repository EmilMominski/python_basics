# Data Input
days = int(input())
hours_per_day = int(input())

# Logic
total_parking = 0
for i in range(1, days + 1):
    parking_per_day = 0
    for j in range(1, hours_per_day + 1):
        if i % 2 == 0 and j % 2 != 0:
            coefficient = 2.5
        elif i % 2 != 0 and j % 2 == 0:
            coefficient = 1.25
        else:
            coefficient = 1
        parking_per_day += coefficient
    total_parking += parking_per_day
    print(f"Day: {i} - {parking_per_day:.2f} leva")

# Print Output
print(f"Total: {total_parking:.2f} leva")
