# Read User's Input
month = input()     # May, June, July, August, September and October
nights = int(input())
studio_price = 0
apartment_price = 0

# Logic
if month == "May" or month == "October":
    studio_price = nights * 50
    apartment_price = nights * 65
    if 7 < nights <= 14:
        studio_price -= studio_price * 5 / 100
    elif nights > 14:
        studio_price -= nights * 50 * 30 / 100
        apartment_price -= apartment_price * 10 / 100

elif month == "June" or month == "September":
    studio_price = nights * 75.2
    apartment_price = nights * 68.7
    if nights > 14:
        studio_price -= studio_price * 20 / 100
        apartment_price -= apartment_price * 10 / 100

elif month == "July" or month == "August":
    studio_price = nights * 76
    apartment_price = nights * 77
    if nights > 14:
        apartment_price -= apartment_price * 10 / 100

# Print Output
print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
