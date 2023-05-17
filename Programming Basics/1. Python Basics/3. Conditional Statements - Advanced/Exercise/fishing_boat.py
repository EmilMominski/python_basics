# Read User's Input
budget = int(input())
season = input()    # Spring, Summer, Autumn, Winter
fishermen = int(input())
rent = 0

# Logic
if season == "Spring":
    rent = 3000
    if fishermen <= 6:
        rent -= rent * 10 / 100
    elif fishermen <= 11:
        rent -= rent * 15 / 100
    else:
        rent -= rent * 25 / 100
elif season == "Summer" or season == "Autumn":
    rent = 4200
    if fishermen <= 6:
        rent -= rent * 10 / 100
    elif fishermen <= 11:
        rent -= rent * 15 / 100
    else:
        rent -= rent * 25 / 100
elif season == "Winter":
    rent = 2600
    if fishermen <= 6:
        rent -= rent * 10 / 100
    elif fishermen <= 11:
        rent -= rent * 15 / 100
    else:
        rent -= rent * 25 / 100
if season != "Autumn" and fishermen % 2 == 0:
    rent -= rent * 5 / 100
difference = abs(rent - budget)

# Print Output
if rent <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
