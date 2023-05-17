# Data Input
chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()    # Spring, Summer, Autumn or Winter
holidays = input()    # Y or N

# Logic
price = 0
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
if season == "Spring" or season == "Summer":
    chrysanthemums_price += chrysanthemums * 2
    roses_price += roses * 4.1
    tulips_price += tulips * 2.5
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price += chrysanthemums * 3.75
    roses_price += roses * 4.5
    tulips_price += tulips * 4.15
if holidays == "Y":
    chrysanthemums_price += chrysanthemums_price * 15 / 100
    roses_price += roses_price * 15 / 100
    tulips_price += tulips_price * 15 / 100
price = chrysanthemums_price + roses_price + tulips_price
if tulips > 7 and season == "Spring":
    price -= price * 5 / 100
if roses >= 10 and season == "Winter":
    price -= price * 10 / 100
if chrysanthemums + roses + tulips > 20:
    price -= price * 20 / 100
price += 2

# Print Output'
print(f"{price:.2f}")