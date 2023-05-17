import math
record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())

swimming_time = distance_in_meters * time_per_meter
delays = math.floor(distance_in_meters / 15)
real_delay = delays * 12.5
real_time = swimming_time + real_delay
difference = abs(real_time - record_in_seconds)

if real_time < record_in_seconds:
    print("Yes, he succeeded! The new world record is " f"{real_time:.2f} " 
          "seconds.")
elif real_time >= record_in_seconds:
    print("No, he failed! He was " f"{difference:.2f} " "seconds slower.")
