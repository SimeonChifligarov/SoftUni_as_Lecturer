EUR_TO_BGN = 1.94
BGN_TO_EUR = 1 / EUR_TO_BGN

vegetables_price = float(input())
fruits_price = float(input())
vegetables_weight = int(input())
fruits_weight = int(input())

vegetables_total = vegetables_weight * vegetables_price
fruits_total = fruits_weight * fruits_price

sum_total_bng = vegetables_total + fruits_total
# sum_total_eur = sum_total_bng / EUR_TO_BGN
sum_total_eur = sum_total_bng * BGN_TO_EUR

print(f"{sum_total_eur :.2f}")
