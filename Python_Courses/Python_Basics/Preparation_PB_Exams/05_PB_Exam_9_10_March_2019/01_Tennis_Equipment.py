import math

DJOKOVIC_RATIO = 1 / 8
SPONSORS_RATIO = 7 / 8

SNEAKERS_TO_RACKET_PRICE_RATIO = 1 / 6
OTHERS_PRICE_MULTIPLIER = 0.20

racket_price = float(input())
racket_count = int(input())
sneakers_count = int(input())
sneakers_price = SNEAKERS_TO_RACKET_PRICE_RATIO * racket_price

total_price = (racket_price * racket_count + sneakers_price * sneakers_count) * (1 + OTHERS_PRICE_MULTIPLIER)
djokovic_price = total_price * DJOKOVIC_RATIO
sponsors_price = total_price * SPONSORS_RATIO

print(f"Price to be paid by Djokovic {math.floor(djokovic_price)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_price)}")
