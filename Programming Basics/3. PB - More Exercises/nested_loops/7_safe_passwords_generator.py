# Data Input
a = int(input())
b = int(input())
max_passwords = int(input())

# Logic & Print Output
passwords_counter = 0
x = int()
y = int()
for A in range(35, 55):
    for B in range(64, 96):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                passwords_counter += 1
                if passwords_counter <= max_passwords:
                    print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}|", end="")
                    B += 1
                    if B > 96:
                        B = 64
                    A += 1
                    if A > 55:
                        A = 35
        if x == a and y == b:
            break
    if x == a and y == b:
        break
