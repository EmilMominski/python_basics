# Data Input
first_start = int(input())
second_start = int(input())
first_end_value = int(input())
second_end_value = int(input())

# Logic
for i in range(first_start, first_start + first_end_value + 1):
    for j in range(second_start, second_start + second_end_value + 1):
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            for y in range(2, j):
                if j % y == 0:
                    break
            else:
                print(f"{i}{j}", end=" ")
