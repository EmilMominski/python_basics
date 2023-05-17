print(not(5 == 5) and (4 + 1 == 5))
print(not(3 == 3) or (3 == 5))
print(not(3 > 5) or (1 == 1))

number = 101
if number >= 1:
    print("Larger than 1")
if number <= 101:
    print("Less than 101")
    print("Equal to 101")

role = "Administrator"
password = "SoftUni"
if role == "SoftUni":
    if password == "SoftUni":
        print("Welcome!")
