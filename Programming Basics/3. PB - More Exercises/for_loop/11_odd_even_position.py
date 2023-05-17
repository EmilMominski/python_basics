# Data Input
import sys
amount_of_numbers = int(input())

# Logic
odd_sum = 0
odd_min_number = sys.maxsize
odd_max_number = -sys.maxsize
even_sum = 0
even_min_number = sys.maxsize
even_max_number = -sys.maxsize
for i in range(1, amount_of_numbers + 1):
    number = float(input())
    if i % 2 != 0:
        odd_sum += number
        if number >= odd_max_number:
            odd_max_number = number
        if number <= odd_min_number:
            odd_min_number = number
    else:
        even_sum += number
        if number >= even_max_number:
            even_max_number = number
        if number <= even_min_number:
            even_min_number = number
if odd_max_number == -sys.maxsize:
    odd_max_number = "No"
else:
    odd_max_number = str(f"{odd_max_number:.2f}")
if odd_min_number == sys.maxsize:
    odd_min_number = "No"
else:
    odd_min_number = str(f"{odd_min_number:.2f}")
if even_min_number == sys.maxsize:
    even_min_number = "No"
else:
    even_min_number = str(f"{even_min_number:.2f}")
if even_max_number == -sys.maxsize:
    even_max_number = "No"
else:
    even_max_number = str(f"{even_max_number:.2f}")

# Print Output
print("OddSum=" + str(f"{odd_sum:.2f},"))
print("OddMin=" + odd_min_number + ",")
print("OddMax=" + odd_max_number + ",")
print("EvenSum=" + str(f"{even_sum:.2f},"))
print("EvenMin=" + even_min_number + ",")
print("EvenMax=" + even_max_number)
