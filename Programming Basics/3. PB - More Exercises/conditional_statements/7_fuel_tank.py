# Data Input
fuel_type = input()    # Diesel, Gasoline or Gas
liters_in_the_tank = float(input())

# Logic and Print Output
if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
    if liters_in_the_tank >= 25:
        print(f"You have enough {fuel_type}.")
    elif liters_in_the_tank < 25:
        print(f"Fill your tank with {fuel_type}!")
else:
    print("Invalid fuel!")
