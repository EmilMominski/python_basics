# Read User's Input
age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
saved_money = 0
even_age = 0
brother_deduction = 0
toys_count = 0

# Logic
for i in range(1, age + 1):
    if i % 2 == 0:
        even_age = even_age + 1
        saved_money = saved_money + even_age * 10
        brother_deduction = brother_deduction + 1
    else:
        toys_count = toys_count + 1
toys_profit = toys_count * toy_price
total_saved_money = toys_profit + saved_money - brother_deduction
difference = abs(total_saved_money - washing_machine_price)

# Print Output
if total_saved_money >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
