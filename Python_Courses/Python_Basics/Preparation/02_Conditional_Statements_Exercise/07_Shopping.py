VIDEO_CARD_PRICE = 250
PROCESSOR_AS_MULTIPLIER = 0.35
RAM_AS_MULTIPLIER = 0.10

budget = float(input())
video_card_count = int(input())
processor_count = int(input())
ram_count = int(input())

video_card_total = video_card_count * VIDEO_CARD_PRICE
processor_price = PROCESSOR_AS_MULTIPLIER * video_card_total
ram_price = RAM_AS_MULTIPLIER * video_card_total

total_price = video_card_total + processor_count * processor_price + ram_count * ram_price

discount = 0
if video_card_count > processor_count:
    discount = 0.15

total_price_with_discount = total_price * (1 - discount)

if budget >= total_price_with_discount:
    print(f"You have {budget - total_price_with_discount :.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price_with_discount - budget :.2f} leva more!")
