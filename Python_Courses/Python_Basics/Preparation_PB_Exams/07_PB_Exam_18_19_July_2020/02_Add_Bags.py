luggage_above_20kg_price = float(input())
luggage_kg = float(input())
days = int(input())
luggage_count = int(input())

if luggage_kg < 10:
    luggage_price = luggage_above_20kg_price * 0.20
elif luggage_kg <= 20:
    luggage_price = luggage_above_20kg_price * 0.50
else:
    luggage_price = luggage_above_20kg_price

if days < 7:
    luggage_price *= (1 + 0.40)
elif days <= 30:
    luggage_price *= (1 + 0.15)
else:
    luggage_price *= (1 + 0.10)

total_price = luggage_price * luggage_count

print(f"The total price of bags is: {total_price :.2f} lv.")
