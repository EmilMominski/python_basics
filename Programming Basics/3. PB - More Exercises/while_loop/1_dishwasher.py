# Data Input
bottles = int(input())
dishes = input()

# Logic
initial_detergent = bottles * 750
detergent = initial_detergent
counter = 0
plates_count = 0
pots_count = 0
dishes_integer = int(dishes)
flag = True

while dishes != "End":
    counter += 1
    if counter == 3:
        pots_count += dishes_integer
        detergent -= dishes_integer * 15
        counter = 0
    else:
        plates_count += dishes_integer
        detergent -= dishes_integer * 5
    if detergent < 0:
        flag = False
        break
    dishes = input()
    if dishes == "End":
        continue
    else:
        dishes_integer = int(dishes)

# Print Output
if flag:
    print("Detergent was enough!")
    print(f"{plates_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")
else:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
