# Data Input
n = int(input())
part_of_the_day = input()    # day or night

# Logic
price = 0
if n < 20:
    price = 0.7
    if part_of_the_day == "day":
        price += n * 0.79
    elif part_of_the_day == "night":
        price += n * 0.9
elif 20 <= n < 100:
    price += n * 0.09
elif n >= 100:
    price += n * 0.06

# Print Output
print(f"{price:.2f}")