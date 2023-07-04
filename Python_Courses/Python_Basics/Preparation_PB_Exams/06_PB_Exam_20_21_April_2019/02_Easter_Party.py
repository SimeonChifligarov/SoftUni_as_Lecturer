guests = int(input())
price_per_guest = float(input())
budget = float(input())

total_price_guests = guests * price_per_guest
if guests > 20:
    total_price_guests *= (1 - 0.25)
elif guests > 15:
    total_price_guests *= (1 - 0.20)
elif guests >= 10:
    total_price_guests *= (1 - 0.15)

cake_price = budget * 0.10

total_price = total_price_guests + cake_price

if budget >= total_price:
    print(f"It is party time! {budget - total_price :.2f} leva left.")
else:
    print(f"No party! {total_price - budget :.2f} leva needed.")
