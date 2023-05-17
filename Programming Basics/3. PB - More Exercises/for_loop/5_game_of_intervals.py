# Data Input
attempts = int(input())

# Logic
result = 0
numbers_0_to_9 = 0
numbers_10_to_19 = 0
numbers_20_to_29 = 0
numbers_30_to_39 = 0
numbers_40_to_50 = 0
invalid_numbers = 0
for i in range(attempts):
    number = int(input())
    if 0 <= number <= 9:
        numbers_0_to_9 += 1
        result += number * 20 /100
    elif 10 <= number <= 19:
        numbers_10_to_19 += 1
        result += number * 30 / 100
    elif 20 <= number <= 29:
        numbers_20_to_29 += 1
        result += number * 40 / 100
    elif 30 <= number <= 39:
        numbers_30_to_39 += 1
        result += 50
    elif 40 <= number <= 50:
        numbers_40_to_50 += 1
        result += 100
    else:
        invalid_numbers += 1
        result = result / 2
percent_0_to_9 = numbers_0_to_9 * 100 / attempts
percent_10_to_19 = numbers_10_to_19 * 100 / attempts
percent_20_to_29 = numbers_20_to_29 * 100 / attempts
percent_30_to_39 = numbers_30_to_39 * 100 / attempts
percent_40_to_50 = numbers_40_to_50 * 100 / attempts
percent_invalid_numbers = invalid_numbers * 100 / attempts

# Print Output
print(f"{result:.2f}")
print(f"From 0 to 9: {percent_0_to_9:.2f}%")
print(f"From 10 to 19: {percent_10_to_19:.2f}%")
print(f"From 20 to 29: {percent_20_to_29:.2f}%")
print(f"From 30 to 39: {percent_30_to_39:.2f}%")
print(f"From 40 to 50: {percent_40_to_50:.2f}%")
print(f"Invalid numbers: {percent_invalid_numbers:.2f}%")
