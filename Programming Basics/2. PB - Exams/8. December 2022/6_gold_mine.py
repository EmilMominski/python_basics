locations = int(input())

for i in range(locations):
    expected_gold_per_day = float(input())
    days = int(input())
    real_gold_all_days = 0
    for j in range(days):
        real_gold_per_day = float(input())
        real_gold_all_days += real_gold_per_day
    average_gold_obtained = real_gold_all_days / days
    if average_gold_obtained >= expected_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold_obtained:.2f}.")
    else:
        difference = abs(average_gold_obtained - expected_gold_per_day)
        print(f"You need {difference:.2f} gold.")
    average_gold_obtained = 0
