PHOTO_WITH_TROPHY = 40

prices = {
    "Quarter final": {
        "Standard": 55.50,
        "Premium": 105.20,
        "VIP": 118.90,
    },
    "Semi final": {
        "Standard": 75.88,
        "Premium": 125.22,
        "VIP": 300.40,
    },
    "Final": {
        "Standard": 110.10,
        "Premium": 160.66,
        "VIP": 400,
    },
}

stage = input()  # “Quarter final”, “Semi final”, or “Final”
ticket_type = input()  # “Standard”, “Premium”, or “VIP”
tickets_count = int(input())
photo_with_trophy = input()  # 'Y' or 'N'

price_per_ticket = prices[stage][ticket_type]
total_price = price_per_ticket * tickets_count

if total_price > 4000:
    total_price *= (1 - 0.25)
    PHOTO_WITH_TROPHY = 0
elif total_price > 2500:
    total_price *= (1 - 0.10)

if photo_with_trophy == "Y":
    total_price += PHOTO_WITH_TROPHY * tickets_count

print(f"{total_price :.2f}")
