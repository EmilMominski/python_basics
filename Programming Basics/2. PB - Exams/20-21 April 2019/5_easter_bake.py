import math
import sys
easter_bread = int(input())

max_sugar = -sys.maxsize
max_flour = -sys.maxsize
sugar_counter = 0
flour_counter = 0

for i in range(easter_bread):
    sugar = int(input())
    flour = int(input())
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour
    sugar_counter += sugar
    flour_counter += flour
sugar_packs = math.ceil(sugar_counter / 950)
flour_packs = math.ceil(flour_counter / 750)

print(f"Sugar: {sugar_packs}")
print(f"Flour: {flour_packs}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
