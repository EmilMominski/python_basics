square_meters_for_landscaping = float(input())
price_for_landscaping_the_whole_yard = square_meters_for_landscaping * 7.61
discount = price_for_landscaping_the_whole_yard * 18/100
final_price_for_landscaping_with_discount = price_for_landscaping_the_whole_yard - discount
print(f"The final price is: {final_price_for_landscaping_with_discount} lv.")
print(f"The discount is: {discount} lv.")
