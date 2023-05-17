# Data Input
upper_limit_hundred = int(input())
upper_limit_ten = int(input())
upper_limit_one = int(input())

# Logic & Print Output
for i in range(1, upper_limit_hundred + 1):
    for j in range(2, upper_limit_ten + 1):
        for m in range(2, j):
            if j % m == 0:
                break
        else:
            for k in range(1, upper_limit_one + 1):
                if i % 2 == 0 and k % 2 == 0:
                    print(i, j, k)
