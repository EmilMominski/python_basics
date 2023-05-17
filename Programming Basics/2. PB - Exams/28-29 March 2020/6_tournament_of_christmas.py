# Read User's Input
days = int(input())

# Logic
prize = 0
total_win_counter = 0
total_lose_counter = 0
money_won = 0
for _ in range(days):
    sport = input()
    result = input()  # win or lose
    win_counter = 0
    lose_counter = 0
    money_per_day = 0
    while sport != "Finish":
        if result == "win":
            win_counter += 1
            money_per_day += 20
        elif result == "lose":
            lose_counter += 1

        sport = input()
        if sport == "Finish":
            continue
        result = input()
    total_win_counter += win_counter
    total_lose_counter += lose_counter
    if win_counter > lose_counter:
        money_per_day += money_per_day * 10 / 100
    money_won += money_per_day

# Print Output
if total_win_counter > total_lose_counter:
    money_won += money_won * 20 / 100
    print(f"You won the tournament! Total raised money: {money_won:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_won:.2f}")
