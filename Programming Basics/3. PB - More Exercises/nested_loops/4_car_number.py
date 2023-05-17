# Data Input
first_number = int(input())
last_number = int(input())

# Logic & Print Output
for i in range(first_number, last_number + 1):
    for j in range(first_number, last_number + 1):
        for k in range(first_number, last_number + 1):
            for m in range(first_number, last_number + 1):
                if i % 2 == 0 and m % 2 != 0 or i % 2 != 0 and m % 2 == 0:
                    if i > m and (j + k) % 2 == 0:
                        print(f"{i}{j}{k}{m} ", end="")
