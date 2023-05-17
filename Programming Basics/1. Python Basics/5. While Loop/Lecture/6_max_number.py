import sys
number_text = input()
max_number = -sys.maxsize

while number_text != "Stop":
    number_digit = int(number_text)
    if number_digit > max_number:
        max_number = number_digit
    number_text = input()
print(max_number)
