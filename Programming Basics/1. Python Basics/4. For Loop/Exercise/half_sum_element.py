# Read User's Input
import sys
number = int(input())
max_number = -sys.maxsize
sum_variables = 0

# Logic
for i in range(0, number):
    variable = int(input())
    if variable > max_number:
        max_number = variable
    sum_variables = sum_variables + variable

# Print Output
if max_number == sum_variables - max_number:
    print("Yes")
    print(f"Sum = {sum_variables - max_number}")
else:
    print("No")
    sum_variables = sum_variables - max_number
    print(f"Diff = {abs(max_number - sum_variables)}")
