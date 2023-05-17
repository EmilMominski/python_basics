# Data Input
capacity = int(input())
fens_count = int(input())

# Logic
sector_a_fens = 0
sector_b_fens = 0
sector_g_fens = 0
sector_v_fens = 0
for i in range(fens_count):
    sector = input()
    if sector == "A":
        sector_a_fens += 1
    elif sector == "B":
        sector_b_fens += 1
    elif sector == "G":
        sector_g_fens += 1
    elif sector == "V":
        sector_v_fens += 1
average_sector_a = sector_a_fens * 100 / fens_count
average_sector_b = sector_b_fens * 100 / fens_count
average_sector_g = sector_g_fens * 100 / fens_count
average_sector_v = sector_v_fens * 100 / fens_count
average_per_capacity = fens_count * 100 / capacity

# Print Output
print(f"{average_sector_a:.2f}%")
print(f"{average_sector_b:.2f}%")
print(f"{average_sector_v:.2f}%")
print(f"{average_sector_g:.2f}%")
print(f"{average_per_capacity:.2f}%")
