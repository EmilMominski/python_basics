import sys
command = ""
max_digit = -sys.maxsize
while True:
    command = input()
    if command != "Stop":
        digit = int(command)
        if digit > max_digit:
            max_digit = digit
    else:
        break
print(max_digit)
