# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit_amount = float(input())
deposit_months = int(input())
annual_interest_rate = float(input())  # 5.7 => 5.7%

annual_interest_rate_percent = annual_interest_rate / 100  # 0.057
result = deposit_amount + deposit_months * ((deposit_amount * annual_interest_rate_percent) / 12)

print(result)
