budget = float(input())

current_budget = budget
equipment_counter = 0
total_equipment_counter = 0
expenses = 0
difference = 0

flag = True
while True:
    equipment_title = input()
    if equipment_title == "Stop":
        break
    equipment_price = float(input())

    equipment_counter += 1
    total_equipment_counter += 1
    if equipment_counter == 3:
        equipment_price = equipment_price / 2
        equipment_counter = 0
    if equipment_price > current_budget:
        difference = equipment_price - current_budget
        flag = False
        break
    current_budget -= equipment_price
    expenses += equipment_price

if flag:
    print(f"You bought {total_equipment_counter} products for {expenses:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {difference:.2f} leva!")
