# Read User's Input
over_weighted_price = float(input())
luggage_weight = float(input())
days_before_departure = int(input())
pieces_of_luggage = int(input())
luggage_price = 0

# Logic
if luggage_weight < 10:
    luggage_price += over_weighted_price * 20 / 100
    if days_before_departure < 7:
        luggage_price += luggage_price * 40 / 100
    elif days_before_departure <= 30:
        luggage_price += luggage_price * 15 / 100
    elif days_before_departure > 30:
        luggage_price += luggage_price * 10 / 100
elif luggage_weight <= 20:
    luggage_price += over_weighted_price * 50 / 100
    if days_before_departure < 7:
        luggage_price += luggage_price * 40 / 100
    elif days_before_departure <= 30:
        luggage_price += luggage_price * 15 / 100
    elif days_before_departure > 30:
        luggage_price += luggage_price * 10 / 100
elif luggage_weight > 20:
    luggage_price += over_weighted_price
    if days_before_departure < 7:
        luggage_price += luggage_price * 40 / 100
    elif days_before_departure <= 30:
        luggage_price += luggage_price * 15 / 100
    elif days_before_departure > 30:
        luggage_price += luggage_price * 10 / 100
total_luggage_price = luggage_price * pieces_of_luggage

# Print Output
print(f" The total price of bags is: {total_luggage_price:.2f} lv.")
