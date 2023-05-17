# Read User's Input
capacity = float(input())

# Logic
remaining_capacity = capacity
suitcase_count = 0
third_suitcase = 0

flag = True
while True:
    suitcase = input()
    if suitcase == "End":
        break
    suitcase_digit = float(suitcase)
    third_suitcase += 1
    if third_suitcase == 3:
        suitcase_digit += suitcase_digit * 10 / 100
        third_suitcase = 0
    if suitcase_digit > remaining_capacity:
        flag = False
        print("No more space!")
        break
    remaining_capacity -= suitcase_digit
    suitcase_count += 1

# Print Output
if flag:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcase_count} suitcases loaded.")
