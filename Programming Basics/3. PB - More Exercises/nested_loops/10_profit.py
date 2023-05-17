# Data Input
coins_1 = int(input())
coins_2 = int(input())
notes_5 = int(input())
amount = int(input())

# Logic & Print Output
for i in range(coins_1 + 1):
    for j in range(coins_2 + 1):
        for k in range(notes_5 + 1):
            available_sum = i * 1 + j * 2 + k * 5
            if available_sum == amount:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {available_sum} lv.")
