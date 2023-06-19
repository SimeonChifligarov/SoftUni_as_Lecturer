EXTRA_COST = 2
HOLIDAY_EXTRA_COST = 15 / 100

prices = {
    "Spring": {
        "chrysanthemums": 2.00,
        "roses": 4.10,
        "tulips": 2.50,
    },
    "Summer": {
        "chrysanthemums": 2.00,
        "roses": 4.10,
        "tulips": 2.50,
    },
    "Autumn": {
        "chrysanthemums": 3.75,
        "roses": 4.50,
        "tulips": 4.15,
    },
    "Winter": {
        "chrysanthemums": 3.75,
        "roses": 4.50,
        "tulips": 4.15,
    },
}

chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()  # Spring, Summer, Autumn, or Winter
input_holiday = input()  # "Y", "N"

is_holiday = input_holiday == "Y"

chrysanthemums_price = prices[season]["chrysanthemums"]
roses_price = prices[season]["roses"]
tulips_price = prices[season]["tulips"]

total_price = chrysanthemums_count * chrysanthemums_price + \
              roses_count * roses_price + \
              tulips_count * tulips_price
if is_holiday:
    total_price *= 1 + HOLIDAY_EXTRA_COST

extra_discount = 0
if tulips_count > 7 and season == "Spring":
    extra_discount = 5 / 100
    total_price *= (1 - extra_discount)

if roses_count >= 10 and season == "Winter":
    extra_discount = 10 / 100
    total_price *= (1 - extra_discount)

if tulips_count + roses_count + chrysanthemums_count > 20:
    extra_discount = 20 / 100
    total_price *= (1 - extra_discount)


total_price_final = total_price + EXTRA_COST

print(f"{total_price_final :.2f}")
