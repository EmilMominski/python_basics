days = int(input())
hours = int(input())

total_fee = 0
for i in range(1, days + 1):
    fee_per_day = 0
    for j in range(1, hours + 1):
        fee_per_hour = 0
        if i % 2 == 0 and j % 2 != 0:
            fee_per_hour += 2.5
        elif i % 2 != 0 and j % 2 == 0:
            fee_per_hour += 1.25
        else:
            fee_per_hour += 1
        fee_per_day += fee_per_hour
    print(f"Day: {i} - {fee_per_day:.2f} leva")
    total_fee += fee_per_day
print(f"Total: {total_fee:.2f} leva")
