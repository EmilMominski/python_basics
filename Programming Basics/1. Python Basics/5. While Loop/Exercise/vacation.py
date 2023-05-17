# Read User's Input
money_needed = float(input())
money_in_the_pocket = float(input())
day_counter = 0
spend_counter = 0

# Logic
while money_in_the_pocket < money_needed and spend_counter < 5:
    operation = input()     # spend or save
    amount = float(input())
    day_counter += 1
    if operation == "spend":
        spend_counter += 1
        money_in_the_pocket -= amount
        if money_in_the_pocket < 0:
            money_in_the_pocket = 0
    elif operation == "save":
        spend_counter = 0
        money_in_the_pocket += amount

# Print Output
if money_in_the_pocket >= money_needed:
    print(f"You saved the money for {day_counter} days.")
if spend_counter == 5:
    print("You can't save the money.")
    print(f"{day_counter}")
