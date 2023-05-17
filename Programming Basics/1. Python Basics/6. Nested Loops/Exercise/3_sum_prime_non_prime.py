# Read User's Input
prime_numbers_sum = 0
non_prime_numbers_sum = 0
flag = True

# Logic
while True:
    number = input()
    if number == "stop":
        break
    digit = int(number)
    if digit > 1:
        non_prime_counter = 0
        for i in range(1, digit + 1):
            if digit % i == 0:
                non_prime_counter += 1
        if non_prime_counter >= 3:
            non_prime_numbers_sum += digit
        else:
            prime_numbers_sum += digit
    else:
        if digit == 0:
            non_prime_numbers_sum += digit
        elif digit < 0:
            print("Number is negative.")
            continue

# Print Output
print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
