# Data Input
M = int(input())

# Logic & Print Output
password_count = 0
password = str()
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == M and a < b and c > d:
                    password_count += 1
                    print(f"{a}{b}{c}{d}", end=" ")
                    if password_count == 4:
                        password = str(f"{a}{b}{c}{d}")

if password_count >= 4:
    print(f"\nPassword: {password}")
else:
    print("\nNo!")
