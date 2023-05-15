city = input()
sales = float(input())

trade_commissions = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        trade_commissions = sales * 0.05
    elif 500 < sales <= 1_000:
        trade_commissions = sales * 0.07
    elif 1_000 < sales <= 10_000:
        trade_commissions = sales * 0.08
    elif sales > 10_000:
        trade_commissions = sales * 0.12
elif city == "Varna":
    if 0 <= sales <= 500:
        trade_commissions = sales * 0.045
    elif 500 < sales <= 1_000:
        trade_commissions = sales * 0.075
    elif 1_000 < sales <= 10_000:
        trade_commissions = sales * 0.10
    elif sales > 10_000:
        trade_commissions = sales * 0.13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        trade_commissions = sales * 0.055
    elif 500 < sales <= 1_000:
        trade_commissions = sales * 0.08
    elif 1_000 < sales <= 10_000:
        trade_commissions = sales * 0.12
    elif sales > 10_000:
        trade_commissions = sales * 0.145

if trade_commissions:
    print(f"{trade_commissions :.2f}")
else:
    print("error")
