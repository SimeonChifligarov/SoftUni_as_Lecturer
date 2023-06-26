NON_POSITIVE_DAYS_MSG = "Days must be positive number!"
INVALID_INPUT_MSG = "Invalid input!"
valid_cities = ("Bansko", "Borovets", "Varna", "Burgas")
valid_packages = {
    "Bansko": ["noEquipment", "withEquipment"],
    "Borovets": ["noEquipment", "withEquipment"],
    "Varna": ["noBreakfast", "withBreakfast"],
    "Burgas": ["noBreakfast", "withBreakfast"],
}

prices = {
    "Bansko": {
        "withEquipment": {
            "cost": 100,
            "VIP discount": 0.10,
        },
        "noEquipment": {
            "cost": 80,
            "VIP discount": 0.05,
        },
    },
    "Borovets": {
        "withEquipment": {
            "cost": 100,
            "VIP discount": 0.10,
        },
        "noEquipment": {
            "cost": 80,
            "VIP discount": 0.05,
        },
    },
    "Varna": {
        "withBreakfast": {
            "cost": 130,
            "VIP discount": 0.12,
        },
        "noBreakfast": {
            "cost": 100,
            "VIP discount": 0.07,
        },
    },
    "Burgas": {
        "withBreakfast": {
            "cost": 130,
            "VIP discount": 0.12,
        },
        "noBreakfast": {
            "cost": 100,
            "VIP discount": 0.07,
        },
    },
}

city = input()  # "Bansko",  "Borovets", "Varna", or "Burgas"
package = input()  # "noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast"
vip_discount = input()  # "yes" or "no"
days = int(input())
if days > 7:
    days -= 1

is_valid = True
if days < 1:
    print(NON_POSITIVE_DAYS_MSG)
    is_valid = False

if city not in valid_cities:  # if city not in prices:
    print(INVALID_INPUT_MSG)
    is_valid = False

elif package not in valid_packages[city]:
    print(INVALID_INPUT_MSG)
    is_valid = False

if is_valid:
    price = prices[city][package]["cost"]
    if vip_discount == "yes":
        price *= (1 - prices[city][package]["VIP discount"])

    total_price = price * days

    print(f"The price is {total_price :.2f}lv! Have a nice time!")
