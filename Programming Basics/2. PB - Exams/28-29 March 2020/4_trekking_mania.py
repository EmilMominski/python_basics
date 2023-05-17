# Read User's Input
groups_count = int(input())

# Logic
total_climbers = 0
musala_climbers = 0
mont_blanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

for i in range(groups_count):
    climbers_count = int(input())
    total_climbers += climbers_count

    if climbers_count <= 5:           # Musala
        musala_climbers += climbers_count
    elif climbers_count <= 12:        # Mont Blanc
        mont_blanc_climbers += climbers_count
    elif climbers_count <= 25:        # Kilimanjaro
        kilimanjaro_climbers += climbers_count
    elif climbers_count <= 40:        # K2
        k2_climbers += climbers_count
    elif climbers_count > 40:         # Everest
        everest_climbers += climbers_count

percent_musala = musala_climbers * 100 / total_climbers
percent_mont_blanc = mont_blanc_climbers * 100 / total_climbers
percent_kilimanjaro = kilimanjaro_climbers * 100 / total_climbers
percent_k2 = k2_climbers * 100 / total_climbers
percent_everest = everest_climbers * 100 / total_climbers

# Print Output
print(f"{percent_musala:.2f}%")
print(f"{percent_mont_blanc:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
