hall_rent = int(input())
statuette_price = hall_rent * 0.70
catering = statuette_price * 0.85
voiceover = catering * 0.50

total_cost = hall_rent + statuette_price + catering + voiceover

print(f"{total_cost :.2f}")
