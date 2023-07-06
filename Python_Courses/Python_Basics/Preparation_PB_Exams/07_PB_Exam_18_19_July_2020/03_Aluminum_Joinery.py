# # Solution 1 -> 1 year ago
# dogrami_count = int(input())
# dogrami_type = input()
# delivery = input()
#
# price_per_one = 0
# discount_percent = 0
# total_price = 0
#
# if dogrami_type == "90X130":
#     price_per_one = 110
#     if 30 < dogrami_count <= 60:
#         discount_percent = 5
#     elif dogrami_count > 60:
#         discount_percent = 8
# elif dogrami_type == "100X150":
#     price_per_one = 140
#     if 40 < dogrami_count <= 80:
#         discount_percent = 6
#     elif dogrami_count > 80:
#         discount_percent = 10
# elif dogrami_type == "130X180":
#     price_per_one = 190
#     if 20 < dogrami_count <= 50:
#         discount_percent = 7
#     elif dogrami_count > 50:
#         discount_percent = 12
# elif dogrami_type == "200X300":
#     price_per_one = 250
#     if 25 < dogrami_count <= 50:
#         discount_percent = 9
#     elif dogrami_count > 50:
#         discount_percent = 14
#
# total_price = price_per_one * dogrami_count * (100 - discount_percent) / 100
#
# if delivery == "With delivery":
#     total_price += 60
#
# if dogrami_count > 99:
#     total_price *= 0.96
#
# if dogrami_count < 10:
#     print('Invalid order')
# else:
#     print(f'{total_price:.2f} BGN')
#
# #####################################################
#
# # Solution 2
DELIVERY_PRICE = 60

prices = {
    "90X130": 110,
    "100X150": 140,
    "130X180": 190,
    "200X300": 250,
}

aluminum_count = int(input())
aluminum_type = input()  # "90X130", "100X150", "130X180", or "200X300"
delivery = input()  # "With delivery" or "Without delivery"

is_valid = True
if aluminum_count < 10:
    is_valid = False

price = prices[aluminum_type]

if aluminum_type == "90X130":
    if aluminum_count > 60:
        price *= (1 - 0.08)
    elif aluminum_count > 30:
        price *= (1 - 0.05)
elif aluminum_type == "100X150":
    if aluminum_count > 80:
        price *= (1 - 0.10)
    elif aluminum_count > 40:
        price *= (1 - 0.06)
elif aluminum_type == "130X180":
    if aluminum_count > 50:
        price *= (1 - 0.12)
    elif aluminum_count > 20:
        price *= (1 - 0.07)
elif aluminum_type == "200X300":
    if aluminum_count > 50:
        price *= (1 - 0.14)
    elif aluminum_count > 25:
        price *= (1 - 0.09)

total_price = aluminum_count * price
if delivery == "With delivery":
    total_price += DELIVERY_PRICE

if aluminum_count > 99:
    total_price *= (1 - 0.04)

if not is_valid:
    print("Invalid order")
else:
    print(f"{total_price :.2f} BGN")
