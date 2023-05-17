import sys
number_text = input()
min_number = sys.maxsize

while number_text != "Stop":
    number_digit = int(number_text)
    if number_digit < min_number:
        min_number = number_digit
    number_text = input()
print(min_number)
