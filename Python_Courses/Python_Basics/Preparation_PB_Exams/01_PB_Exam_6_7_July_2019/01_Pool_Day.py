import math

guests = int(input())
ticket = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

tickets_total = guests * ticket
umbrella_total = math.ceil(guests / 2) * umbrella_price
sunbed_total = math.ceil(0.75 * guests) * sunbed_price

total = tickets_total + umbrella_total + sunbed_total

print(f"{total :.2f} lv.")
