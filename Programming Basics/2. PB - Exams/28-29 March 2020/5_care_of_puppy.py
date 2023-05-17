# Read User's Input
purchased_food = int(input())
eaten_food = input()

# Logic
food_counter = 0

while eaten_food != "Adopted":
    digit = int(eaten_food)
    food_counter += digit
    eaten_food = input()

difference = abs(food_counter - purchased_food * 1000)

# Print Output
if purchased_food * 1000 >= food_counter:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")
