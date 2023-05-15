# # Solution 1
# PREMIERE_PRICE = 12.00
# NORMAL_PRICE = 7.50
# DISCOUNT_PRICE = 5.00
#
# screening_type = input()
# rows = int(input())
# cols = int(input())
#
# screening_capacity = rows * cols
#
# price = 0
# if screening_type == "Premiere":
#     price = PREMIERE_PRICE
# elif screening_type == "Normal":
#     price = NORMAL_PRICE
# elif screening_type == "Discount":
#     price = DISCOUNT_PRICE
#
# total_income = screening_capacity * price
# print(f"{total_income :.2f} leva")

# Solution 2
prices = {
    "Premiere": 12.00,
    "Normal": 7.50,
    "Discount": 5.00,
}

screening_type = input()
rows = int(input())
cols = int(input())

screening_capacity = rows * cols
price = prices[screening_type]

total_income = screening_capacity * price
print(f"{total_income :.2f} leva")
