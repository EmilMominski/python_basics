pens = int(input())
highlighters = int(input())
cleaning_material = int(input())
discount = int(input())
pen_price = pens * 5.8
highlighter_price = highlighters * 7.2
cleaning_material_price = cleaning_material * 1.2
total_price = pen_price + highlighter_price + cleaning_material_price
final_price = total_price - total_price * discount / 100
print(final_price)
