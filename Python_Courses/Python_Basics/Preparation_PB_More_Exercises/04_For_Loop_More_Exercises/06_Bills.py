# •	За ток – всеки месец е различен, ще се чете от конзолата
# •	за вода – 20 лв.
# •	за интернет – 15 лв.
# •	за други – събират се тока, водата и интернета за месеца и към сумата се прибавят 20%.
WATER_BILL_PER_MONTH = 20
INTERNET_BILL_PER_MONTH = 15
OTHER_BILLS_PER_MONTH_MULTIPLIER = 1.20

electricity_total = 0
water_total = 0
internet_total = 0
other_total = 0

months_count = int(input())

for _ in range(months_count):
    electricity_bill = float(input())
    electricity_total += electricity_bill
    water_total += WATER_BILL_PER_MONTH
    internet_total += INTERNET_BILL_PER_MONTH
    other_total += OTHER_BILLS_PER_MONTH_MULTIPLIER * \
                   (WATER_BILL_PER_MONTH + INTERNET_BILL_PER_MONTH + electricity_bill)


total_bills = electricity_total + water_total + internet_total + other_total

print(f"Electricity: {electricity_total :.2f} lv")
print(f"Water: {water_total :.2f} lv")
print(f"Internet: {internet_total :.2f} lv")
print(f"Other: {other_total :.2f} lv")
print(f"Average: {total_bills / months_count :.2f} lv")
