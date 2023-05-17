# Data Input
mackerel = float(input())
sprat = float(input())
kilos_bonito = float(input())
kilos_scad = float(input())
kilos_mussels = float(input())

# Logic
bonito_per_kilo = mackerel * (1 + 60 / 100)
total_bonito = bonito_per_kilo * kilos_bonito
scad_per_kilo = sprat * (1 + 80 / 100)
total_scad = scad_per_kilo * kilos_scad
total_mussels = kilos_mussels * 7.5
bill = total_bonito + total_scad + total_mussels

# Print Output
print(f"{bill:.2f}")
