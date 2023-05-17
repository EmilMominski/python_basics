kid_counter = 0
adult_counter = 0
while True:
    age = input()
    if age == "Christmas":
        break
    age_digit = int(age)
    if age_digit <= 16:
        kid_counter += 1
    elif age_digit > 16:
        adult_counter += 1
toy_price = kid_counter * 5
pullover_price = adult_counter * 15

print(f"Number of adults: {adult_counter}")
print(f"Number of kids: {kid_counter}")
print(f"Money for toys: {toy_price}")
print(f"Money for sweaters: {pullover_price}")
