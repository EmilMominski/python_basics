# Data Input
cargo_count = int(input())

# Logic
total_cargo = 0
price_mini_van = 0
price_truck = 0
price_train = 0
weight_mini_van = 0
weight_truck = 0
weight_train = 0
for i in range(cargo_count):
    cargo_weight = int(input())
    if cargo_weight <= 3:
        price_mini_van += cargo_weight * 200
        weight_mini_van += cargo_weight
    elif 4 <= cargo_weight <= 11:
        price_truck += cargo_weight * 175
        weight_truck += cargo_weight
    elif cargo_weight >= 12:
        price_train += cargo_weight * 120
        weight_train += cargo_weight
    total_cargo += cargo_weight
average_price_cargo = (price_mini_van + price_truck + price_train) / total_cargo
mini_van_percent = weight_mini_van * 100 / total_cargo
truck_percent = weight_truck * 100 / total_cargo
train_percent = weight_train * 100 / total_cargo

# Print Output
print(f"{average_price_cargo:.2f}")
print(f"{mini_van_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")
