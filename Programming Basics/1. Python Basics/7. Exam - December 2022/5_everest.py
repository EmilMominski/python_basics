day_counter = 1
distance_climbed = 5364
flag = True

while True:
    rest = input()
    if rest == "END":

        break
    meters = int(input())
    if rest == "Yes":
        day_counter += 1
    distance_climbed += meters
    if day_counter >= 5:
        flag = False
        break
    if distance_climbed >= 8848:
        break

if flag:
    print(f"Goal reached for {day_counter} days!")
else:
    print("Failed!")
    print(f"{distance_climbed}")
