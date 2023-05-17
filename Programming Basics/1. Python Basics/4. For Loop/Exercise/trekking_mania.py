# Read User's Input
groups = int(input())
musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

# Logic
for i in range(0, groups):
    climbers_count = int(input())
    if climbers_count <= 5:
        musala = musala + climbers_count
    elif climbers_count <= 12:
        mont_blanc = mont_blanc + climbers_count
    elif climbers_count <= 25:
        kilimanjaro = kilimanjaro + climbers_count
    elif climbers_count <= 40:
        k2 = k2 + climbers_count
    elif climbers_count >= 41:
        everest = everest + climbers_count
total_climbers = musala + mont_blanc + kilimanjaro + k2 + everest
musala_percent = musala * 100 / total_climbers
mont_blanc_percent = mont_blanc * 100 / total_climbers
kilimanjaro_percent = kilimanjaro * 100 / total_climbers
k2_percent = k2 * 100 / total_climbers
everest_percent = everest * 100 / total_climbers

# Print Output
print(f"{musala_percent:.2f}%")
print(f"{mont_blanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
