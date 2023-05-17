# Data Input
juniors_count = int(input())
seniors_count = int(input())
track_type = input()    # trail, cross-country, downhill and road

# Logic
juniors_fee = 0
seniors_fee = 0
participants = juniors_count + seniors_count
if track_type == "trail":
    juniors_fee += 5.5
    seniors_fee += 7
elif track_type == "cross-country":
    juniors_fee += 8
    seniors_fee += 9.5
elif track_type == "downhill":
    juniors_fee += 12.25
    seniors_fee += 13.75
elif track_type == "road":
    juniors_fee += 20
    seniors_fee += 21.5
donation = juniors_count * juniors_fee + seniors_count * seniors_fee
if track_type == "cross-country" and participants >= 50:
    donation -= donation * 25 / 100
donation -= donation * 5 / 100

# Print Output
print(f"{donation:.2f}")