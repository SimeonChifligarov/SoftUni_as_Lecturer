# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

# 1. E
deposit_amount = float(input())  # 33.5
deposit_months = int(input())
annual_interest_rate = float(input())

# 2. T
annual_interest_rate_as_percent = annual_interest_rate / 100
final_amount = deposit_amount + deposit_months * ((deposit_amount * annual_interest_rate_as_percent) / 12)

# 3. L
print(final_amount)
