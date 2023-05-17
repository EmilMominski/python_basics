open_tabs = int(input())
salary = int(input())
deduction = 0

for i in range(0, open_tabs):
    variable = input()
    if variable == "Facebook":
        deduction = deduction + 150
    elif variable == "Instagram":
        deduction = deduction + 100
    elif variable == "Reddit":
        deduction = deduction + 50
    if deduction >= salary:
        print("You have lost your salary.")
        break

if deduction < salary:
    print(salary - deduction)
