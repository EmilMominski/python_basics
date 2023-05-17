# Data Input
volume = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

# Logic
flag = True
p1_volume = p1 * h
p2_volume = p2 * h
total_volume = p1_volume + p2_volume
if total_volume <= volume:
    percent_volume = total_volume *100 / volume
    percent_p1 = p1_volume * 100 / total_volume
    percent_p2 = p2_volume * 100 / total_volume
else:
    difference = total_volume - volume
    flag = False

# Print Output
if flag:
    print(f"The pool is {percent_volume:.2f}% full. Pipe 1: {percent_p1:.2f}%. Pipe 2: {percent_p2:.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {difference:.2f} liters.")
