# Data Input
rent = int(input())

# Logic
statues = rent * (1 - 30/100)
catering = statues * (1 - 15/100)
sound = catering / 2
expenses = rent + statues + catering + sound

# Output
print(f"{expenses:.2f}")
