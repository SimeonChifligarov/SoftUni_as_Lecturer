# •	До 3 тона – микробус (200 лева на тон)
# •	От 4 до 11 тона – камион (175 лева на тон)
# •	12 и повече тона – влак (120 лева на тон)
BUS_PRICE = 200
TRUCK_PRICE = 175
TRAIN_PRICE = 120

bus_tons = 0
truck_tons = 0
train_tons = 0

cargo_count = int(input())

for _ in range(cargo_count):
    current_cargo = int(input())
    if current_cargo <= 3:
        bus_tons += current_cargo
    elif current_cargo <= 11:
        truck_tons += current_cargo
    else:
        train_tons += current_cargo

total_tons = bus_tons + truck_tons + train_tons

total_money = bus_tons * BUS_PRICE + truck_tons * TRUCK_PRICE + train_tons * TRAIN_PRICE
avg_money = total_money / total_tons

print(f"{avg_money :.2f}")
print(f"{bus_tons / total_tons :.2%}")
print(f"{truck_tons / total_tons :.2%}")
print(f"{train_tons / total_tons :.2%}")
