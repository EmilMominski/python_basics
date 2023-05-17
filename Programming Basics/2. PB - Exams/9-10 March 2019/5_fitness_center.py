# Data Input
people_in_the_gym = int(input())

# Logic
back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_shake_count = 0
protein_bar_count = 0
for i in range(people_in_the_gym):
    activity = input()    # Back, Chest, Legs, Abs, Protein shake or Protein bar
    if activity == "Back":
        back_count += 1
    elif activity == "Chest":
        chest_count += 1
    elif activity == "Legs":
        legs_count +=1
    elif activity == "Abs":
        abs_count += 1
    elif activity == "Protein shake":
        protein_shake_count += 1
    elif activity == "Protein bar":
        protein_bar_count += 1
work_out = (back_count + chest_count + legs_count + abs_count) * 100 / people_in_the_gym
protein = (protein_shake_count + protein_bar_count) * 100 / people_in_the_gym

# Print Output
print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{protein_shake_count} - protein shake")
print(f"{protein_bar_count} - protein bar")
print(f"{work_out:.2f}% - work out")
print(f"{protein:.2f}% - protein")
