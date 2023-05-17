# Data Input
import sys
couples = int(input())

# Logic
a = 0
equal_counter = 0
max_difference = -sys.maxsize
for i in range(couples):
    b = 0
    number_1 = int(input())
    number_2 = int(input())
    if i == 0:
        a += number_1 + number_2
        continue
    else:
        b += number_1 + number_2
        if a == b:

            equal_counter += 1
        else:
            c = abs(a - b)

            if c > max_difference:
                max_difference = c
    a = b

# Print Output
if equal_counter == couples - 1:
    print(f"Yes, value={a}")
else:
    print(f"No, maxdiff={max_difference}")
