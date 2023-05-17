# Read User's Input
starting_number = int(input())
ending_number = int(input())
magic_number = int(input())

# Logic
combination_counter = 0
result = 0
flag = True

for i in range(starting_number, ending_number + 1):
    for j in range(starting_number, ending_number + 1):
        result = i + j
        combination_counter += 1
        if result == magic_number:
            flag = False
            break
    if not flag:
        break
if not flag:
    print(f"Combination N:{combination_counter} ({i} + {j} = {result})")
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
