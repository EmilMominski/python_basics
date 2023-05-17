# Read User's Input
weight_of_delivery = float(input())
type_of_service = input()       # standard or express
distance = int(input())

# Logic
price = 0
if type_of_service == "standard":
    if weight_of_delivery < 1:
        price = distance * 0.03
    elif weight_of_delivery < 10:
        price = distance * 0.05
    elif weight_of_delivery < 40:
        price = distance * 0.1
    elif weight_of_delivery < 90:
        price = distance * 0.15
    elif weight_of_delivery < 150:
        price = distance * 0.2
elif type_of_service == "express":
    if weight_of_delivery < 1:
        price = (0.03 + weight_of_delivery * 0.03 * 0.8) * distance
    elif weight_of_delivery < 10:
        price = (0.05 + weight_of_delivery * 0.05 * 0.4) * distance
    elif weight_of_delivery < 40:
        price = (0.1 + weight_of_delivery * 0.1 * 0.05) * distance
    elif weight_of_delivery < 90:
        price = (0.15 + weight_of_delivery * 0.15 * 0.02) * distance
    elif weight_of_delivery < 150:
        price = (0.2 + weight_of_delivery * 0.2 * 0.01) * distance

# Print Output
print(f"The delivery of your shipment with weight of {weight_of_delivery:.3f} kg. would cost {price:.2f} lv.")
