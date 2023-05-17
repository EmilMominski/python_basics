# Data Input
control_minutes = int(input())
control_seconds = int(input())
length = float(input())
seconds_per_hundred = int(input())

# Logic
control_time = control_minutes * 60 + control_seconds
marin_time = seconds_per_hundred * length / 100
delay = length / 120 * 2.5
total_marin_time = marin_time - delay

# Print Output
if total_marin_time <= control_time:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {total_marin_time:.3f}.")
else:
    difference = total_marin_time - control_time
    print(f"No, Marin failed! He was {difference:.3f} second slower.")