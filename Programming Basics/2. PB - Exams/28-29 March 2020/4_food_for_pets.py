# Read User's Input
days = int(input())
amount_of_food = float(input())

# Logic
total_food_eaten_by_dog = 0
total_food_eaten_by_cat = 0
biscuit = 0

for i in range(1, days + 1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())
    if i % 3 == 0:
        biscuit += (food_eaten_by_dog + food_eaten_by_cat) * 10 / 100
    total_food_eaten_by_dog += food_eaten_by_dog
    total_food_eaten_by_cat += food_eaten_by_cat

total_eaten_food = total_food_eaten_by_dog + total_food_eaten_by_cat
percent_eaten_food = total_eaten_food * 100 / amount_of_food
percent_eaten_food_by_dog = total_food_eaten_by_dog * 100 / total_eaten_food
percent_eaten_food_by_cat = total_food_eaten_by_cat * 100 / total_eaten_food

# Print Output
print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_food_by_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_food_by_cat:.2f}% eaten from the cat.")
