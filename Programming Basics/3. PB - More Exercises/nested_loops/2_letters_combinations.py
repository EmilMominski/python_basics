# Data Input
beginning_letter = input()
end_letter = input()
skip_letter = input()

# Logic & Print Output
beginning_digit = ord(beginning_letter)
end_digit = ord(end_letter)
skip_digit = ord(skip_letter)
counter = 0

for i in range(beginning_digit, end_digit + 1):
    for j in range(beginning_digit, end_digit + 1):
        for k in range(beginning_digit, end_digit + 1):
            if i == skip_digit or j == skip_digit or k == skip_digit:
                continue
            counter += 1
            print(f"{chr(i)}{chr(j)}{chr(k)} ", end="")
print(counter)
