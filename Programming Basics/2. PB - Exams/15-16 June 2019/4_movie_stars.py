# Read User's Input
budget = float(input())
actor_name = input()
if len(actor_name) > 15:
    actor_wage = budget * 20 / 100
else:
    actor_wage = float(input())

# Logic
remaining_budget = budget
flag = True
while actor_name != "ACTION":
    remaining_budget -= actor_wage
    if remaining_budget <= 0:
        flag = False
        break
    actor_name = input()
    if actor_name == "ACTION":
        continue
    if len(actor_name) > 15:
        actor_wage = remaining_budget * 20 / 100
    else:
        actor_wage = float(input())

# Print Output
if flag:
    print(f"We are left with {remaining_budget:.2f} leva.")
else:
    print(f"We need {abs(remaining_budget):.2f} leva for our actors.")
