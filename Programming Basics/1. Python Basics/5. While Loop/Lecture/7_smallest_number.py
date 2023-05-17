import sys
text = input()
min_number = sys.maxsize

while text != "Stop":
    number = int(text)
    if number < min_number:
        min_number = number
    text = input()
print(min_number)
