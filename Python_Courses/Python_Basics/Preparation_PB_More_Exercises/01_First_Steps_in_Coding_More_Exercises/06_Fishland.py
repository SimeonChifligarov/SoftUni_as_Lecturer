BELTED_BONITO_MULTIPLIER = 1.6
SCAD_FISH_MULTIPLIER = 1.8
MUSSELS_PRICE = 7.5

mackerel_price = float(input())
sprat_fish_price = float(input())
belted_bonito_kgs = float(input())
scad_fish_kgs = float(input())
mussels_kgs = int(input())

belted_bonito_price = mackerel_price * BELTED_BONITO_MULTIPLIER
scad_fish_price = sprat_fish_price * SCAD_FISH_MULTIPLIER

total_price = belted_bonito_kgs * belted_bonito_price + scad_fish_kgs * scad_fish_price + mussels_kgs * MUSSELS_PRICE

print(f"{total_price :.2f}")
