# Data Input
upper_limit_first = int(input())
upper_limit_second = int(input())
upper_limit_third = int(input())

# Logic
for i in range(1, upper_limit_first + 1):
    if i % 2 == 0:
        for j in range(2, upper_limit_second + 1):
            for m in range(2, j):
                if j % m == 0:
                    break
            else:
                for k in range(1, upper_limit_third + 1):
                    if k % 2 == 0:
                        print(i, j, k)
