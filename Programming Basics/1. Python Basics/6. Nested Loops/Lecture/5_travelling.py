destination = input()
min_budget = float(input())
savings_counter = 0

while destination != "End":
    while savings_counter < min_budget:
        savings_input = float(input())
        savings_counter += savings_input
    print(f"Going to {destination}!")
    savings_counter = 0
    destination = input()
    if destination == "End":
        continue
    min_budget = float(input())
