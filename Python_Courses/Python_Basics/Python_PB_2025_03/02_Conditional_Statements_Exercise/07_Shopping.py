# 1.	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
budget = float(input())
# 2.	Броят видеокарти - цяло число в интервала [1…100]
video_cards_count = int(input())
# 3.	Броят процесори - цяло число в интервала [1…100]
processors_count = int(input())
# 4.	Броят рам памет - цяло число в интервала [1…100]
ram_count = int(input())

# •	Видеокарта – 250 лв./бр.
video_card_price = 250

video_cards_total_cost = video_cards_count * video_card_price

# •	Процесор – 35% от цената на закупените видеокарти/бр.
processor_price = video_cards_total_cost * 0.35

# •	Рам памет – 10% от цената на закупените видеокарти/бр.
ram_price = video_cards_total_cost * 0.10

total_cost = (
    video_cards_total_cost
    + processors_count * processor_price
    + ram_count * ram_price
)

# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка.
discount = 0.0
if video_cards_count > processors_count:
    discount = 0.15  # 15 / 100 == 0.15

total_cost_after_discount = total_cost * (1 - discount)

if budget >= total_cost_after_discount:
    print(f'You have {abs(budget - total_cost_after_discount):.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(budget - total_cost_after_discount):.2f} leva more!')
