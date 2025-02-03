budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

video_cards_price = video_cards_count * 250

processor_price = video_cards_price * 0.35
ram_price = video_cards_price * 0.10

total_price = video_cards_price + processors_count * processor_price + ram_count * ram_price

# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка
if video_cards_count > processors_count:
    total_price *= 0.85

if budget > total_price:
    money_left = budget - total_price
    print(f'You have {money_left :.2f} leva left!')
else:
    money_needed = total_price - budget
    print(f'Not enough money! You need {money_needed :.2f} leva more!')
