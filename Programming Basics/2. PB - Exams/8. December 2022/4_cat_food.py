cats_amount = int(input())

group1_counter = 0
group2_counter = 0
group3_counter = 0
total_food_amount = 0

for i in range(cats_amount):
    food = float(input())
    if 100 <= food < 200:
        group1_counter += 1
    elif 200 <= food < 300:
        group2_counter += 1
    elif 300 <= food < 400:
        group3_counter += 1
    total_food_amount += food
price = total_food_amount / 1000 * 12.45

print(f"Group 1: {group1_counter} cats.")
print(f"Group 2: {group2_counter} cats.")
print(f"Group 3: {group3_counter} cats.")
print(f"Price for food per day: {price:.2f} lv.")
