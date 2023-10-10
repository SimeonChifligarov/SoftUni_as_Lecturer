# price_per_meter = 7.61
# total_meters = int(input())
# discount = (price_per_meter * total_meters) - ((price_per_meter * total_meters) * 0.82)
# final_price = price_per_meter * total_meters - discount
# discount = round(discount, 2)
# final_price = round(final_price, 2)
# print(f"The final price is {final_price : }")
# print(f"The discount is: {discount : }.")

prices_for_landscaping_the_entire_yard = float(input()) * 7.61
discount_for_the_landscaping = prices_for_landscaping_the_entire_yard * 0.18
total_prices_for_pay = prices_for_landscaping_the_entire_yard - discount_for_the_landscaping

print(f"The final price is {total_prices_for_pay} lv.\nThe discount is {discount_for_the_landscaping} lv.")
