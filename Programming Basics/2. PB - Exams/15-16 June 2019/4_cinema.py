capacity = int(input())

remaining_capacity = capacity
profit = 0
flag = True
while True:
    people_count = input()
    if people_count == "Movie time!":
        break
    digit = int(people_count)
    if remaining_capacity == 0:
        flag = False
        break
    else:
        remaining_capacity -= digit
        if remaining_capacity < 0:
            flag = False
            break
    if digit % 3 == 0:
        profit += digit * 5 - 5
    else:
        profit += digit * 5

if flag:
    print(f"There are {remaining_capacity} seats left in the cinema.")
else:
    print("The cinema is full.")
print(f"Cinema income - {profit} lv.")
