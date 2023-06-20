EVEN_YEAR_EXPENSES = 12_000


money_available = float(input())
end_year = int(input())
age = 18

money_needed = 0
for y in range(1800, end_year + 1):
    if y % 2 == 0:
        money_needed += EVEN_YEAR_EXPENSES
    else:
        money_needed += EVEN_YEAR_EXPENSES + 50 * age

    age += 1

if money_available >= money_needed:
    print(f"Yes! He will live a carefree life and will have {money_available - money_needed :.2f} dollars left.")
else:
    print(f"He will need {money_needed - money_available :.2f} dollars to survive.")
