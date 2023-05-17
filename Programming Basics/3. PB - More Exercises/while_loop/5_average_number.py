# Data Input
number = int(input())

# Logic
i = 1
average_number = 0
while i <= number:
    input_number = int(input())
    average_number += input_number
    i += 1
average_number /= number

# Print Output
print(f"{average_number:.2f}")
