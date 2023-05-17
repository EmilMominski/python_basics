# Read User's Input
budget = float(input())
season = input()    # summer or winter
destination_type = ""   # Camp or Hotel
destination = ""    # Bulgaria, Balkans or Europe
price = 0

# Logic
if season == "summer":
    destination_type = "Camp"
    if budget <= 100:
        destination = "Bulgaria"
        price = budget * 30 / 100
    elif budget <= 1000:
        destination = "Balkans"
        price = budget * 40 / 100
    elif budget > 1000:
        destination = "Europe"
        destination_type = "Hotel"
        price = budget * 90 / 100
elif season == "winter":
    destination_type = "Hotel"
    if budget <= 100:
        destination = "Bulgaria"
        price = budget * 70 / 100
    elif budget <= 1000:
        destination = "Balkans"
        price = budget * 80 / 100
    elif budget > 1000:
        destination = "Europe"
        destination_type = "Hotel"
        price = budget * 90 / 100

# Print Output
print(f"Somewhere in {destination}")
print(f"{destination_type} - {price:.2f}")
