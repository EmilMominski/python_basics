# Data Input
months = int(input())

# Logic
total_electricity_bill = 0
total_water_bill = months * 20
total_internet_bill = months * 15
total_others_bill = 0
for i in range(months):
    electricity_bill = float(input())
    total_electricity_bill += electricity_bill
    total_others_bill += (electricity_bill + 35) + \
                         (electricity_bill + 35) * 20 / 100
average_bill = (total_electricity_bill + total_water_bill + total_internet_bill + total_others_bill) / months

# Print Output
print(f"Electricity: {total_electricity_bill:.2f} lv")
print(f"Water: {total_water_bill:.2f} lv")
print(f"Internet: {total_internet_bill:.2f} lv")
print(f"Other: {total_others_bill:.2f} lv")
print(f"Average: {average_bill:.2f} lv")
