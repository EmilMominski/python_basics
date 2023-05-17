# Read User's Input
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

# Logic
exam_hr_to_min = exam_hour * 60
total_exam_min = exam_hr_to_min + exam_minute
arrival_hr_to_min = arrival_hour * 60
total_arrival_min = arrival_hr_to_min + arrival_minute
difference = total_arrival_min - total_exam_min
abs_diff = abs(difference)

if difference == 0:
    print(" On time")
else:
    if difference > 0:
        print("Late")
        if abs_diff < 60:
            print(f"{abs_diff} minutes after the start")
        elif abs_diff >= 60:
            hours = abs_diff // 60
            minutes = round((abs_diff / 60 - hours) * 60)
            if minutes < 10:
                print(f"{hours}:0{minutes} hours after the start")
            elif minutes >= 10:
                print(f"{hours}:{minutes} hours after the start")
    elif difference < 0:
        if abs_diff <= 30:
            print("On time")
            print(f"{abs_diff} minutes before the start")
        elif abs_diff > 30:
            print("Early")
            if abs_diff < 60:
                print(f"{abs_diff} minutes before the start")
            elif abs_diff >= 60:
                hours = abs_diff // 60
                minutes = round((abs_diff / 60 - hours) * 60)
                if minutes < 10:
                    print(f"{hours}:0{minutes} hours before the start")
                elif minutes >= 10:
                    print(f"{hours}:{minutes} hours before the start")
