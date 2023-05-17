# Data Input
budget = float(input())
season = input()    # Summer or Winter

# Logic
class_type = str()
car_type = str()
price = 0
if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price += budget * 35 / 100
    elif season == "Winter":
        car_type = "Jeep"
        price += budget * 65 / 100
elif 100 < budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price += budget * 45 / 100
    elif season == "Winter":
        car_type = "Jeep"
        price += budget * 80 / 100
elif budget > 500:
    class_type = "Luxury class"
    car_type = "Jeep"
    price += budget * 90 / 100

# Print Output
print(f"{class_type}")
print(f"{car_type} - {price:.2f}")