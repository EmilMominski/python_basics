day_counter = 1
distance_climbed = 5364

while True:
    rest = input()
    if rest == "END":
        if distance_climbed >= 8848:
            print(f"Goal reached for {day_counter} days!")
            break
        else:
            print("Failed!")
            print(f"{distance_climbed}")
            break
    meters = int(input())
    if rest == "Yes":
        day_counter += 1
    distance_climbed += meters
    if day_counter >= 5:
        if distance_climbed >= 8848:
            print(f"Goal reached for {day_counter} days!")
            print("Failed!")
        else:
            print(f"{distance_climbed}")
            break
    if distance_climbed >= 8848:
        print(f"Goal reached for {day_counter} days!")
        break
