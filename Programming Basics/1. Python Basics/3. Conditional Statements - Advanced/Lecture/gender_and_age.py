# Read User Input
gender = input()
age = int(input())

# Logic and Output
if gender == "f":
    if age < 16:
        print("Miss")
    else:
        print("Ms.")
else:
    if age < 16:
        print("Master")
    else:
        print("Mr.")
