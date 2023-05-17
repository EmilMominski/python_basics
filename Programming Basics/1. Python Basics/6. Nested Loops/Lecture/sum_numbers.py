starting_number = int(input())
end_number = int(input())
magic_number = int(input())
combination_count = 0
flag = True
for i in range(starting_number, end_number + 1):
    for j in range(starting_number, end_number + 1):
        sum_numbers = i + j
        combination_count += 1
        if sum_numbers == magic_number:
            print(f"Combination N: {combination_count} ({i} + {j} = {sum_numbers})")
            flag = False
            break
    if not flag:
        break
if flag:
    print(f"{combination_count} combinations - neither equals {magic_number}")
