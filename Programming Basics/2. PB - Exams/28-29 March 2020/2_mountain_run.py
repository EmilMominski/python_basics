record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())

real_time = distance_in_meters * time_per_meter
delay = (distance_in_meters // 50) * 30
real_time += delay
difference = abs(real_time - record_in_seconds)
if real_time < record_in_seconds:
    print(f"Yes! The new record is {real_time:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")
