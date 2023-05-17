# Data Input
import math
days = int(input())
food_in_kilos = int(input())
dog_food_in_kilos = float(input())
cat_food_in_kilos = float(input())
turtle_food_in_grams = float(input())

# Logic
dog_food_needed = dog_food_in_kilos * days
cat_food_needed = cat_food_in_kilos * days
turtle_food_needed = turtle_food_in_grams * days / 1000
food_needed = dog_food_needed + cat_food_needed + turtle_food_needed
difference = abs(food_in_kilos - food_needed)

# Print Output
if food_in_kilos > food_needed:
    difference = math.floor(difference)
    print(f"{difference} kilos of food left.")
else:
    difference = math.ceil(difference)
    print(f"{difference} more kilos of food are needed.")