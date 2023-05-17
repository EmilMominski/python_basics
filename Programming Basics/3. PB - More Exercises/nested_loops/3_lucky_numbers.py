# Data Input
number = int(input())

# Logic & Print Output
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                if i + j == k + m and number % (i + j) == 0:
                    print(f"{i}{j}{k}{m} ", end="")
