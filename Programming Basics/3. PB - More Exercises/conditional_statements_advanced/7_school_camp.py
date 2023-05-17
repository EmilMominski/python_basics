# Data Input
season = input()    # Winter, Spring or Summer
group_type = input()    # boys, girls or mixed
students_count = int(input())
days_count = int(input())

# Logic
coefficient = 0
sport = str()
if season == "Winter":
    if group_type == "boys":
        sport = "Judo"
        coefficient += 9.6
    elif group_type == "girls":
        sport = "Gymnastics"
        coefficient += 9.6
    elif group_type == "mixed":
        sport = "Ski"
        coefficient += 10
elif season == "Spring":
    if group_type == "boys":
        sport = "Tennis"
        coefficient += 7.2
    elif group_type == "girls":
        sport = "Athletics"
        coefficient += 7.2
    elif group_type == "mixed":
        sport = "Cycling"
        coefficient += 9.5
elif season == "Summer":
    if group_type == "boys":
        sport = "Football"
        coefficient += 15
    elif group_type == "girls":
        sport = "Volleyball"
        coefficient += 15
    elif group_type == "mixed":
        sport = "Swimming"
        coefficient += 20
price = students_count * days_count * coefficient
if students_count >= 50:
    price -= price * 50 / 100
elif 20 <= students_count < 50:
    price -= price * 15 / 100
elif 10 <= students_count < 20:
    price -= price * 5 / 100

# Print Output
print(f"{sport} {price:.2f} lv.")
