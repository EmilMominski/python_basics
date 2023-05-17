minutes_per_day = int(input())
walks_per_day = int(input())
consumed_calories = int(input())

burned_calories = minutes_per_day * 5 * walks_per_day
enough_calories = consumed_calories / 2
if enough_calories <= burned_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")
