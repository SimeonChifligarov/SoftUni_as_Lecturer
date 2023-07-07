BITCOIN_TO_BGN = 1168
CNY_TO_USD = 0.15
USD_TO_BGN = 1.76
EUR_TO_BGN = 1.95

BITCOIN_TO_EUR = BITCOIN_TO_BGN / EUR_TO_BGN
CNY_TO_EUR = CNY_TO_USD * USD_TO_BGN / EUR_TO_BGN

bitcoins = int(input())
cny = float(input())
commission = float(input()) / 100

eur = bitcoins * BITCOIN_TO_EUR + cny * CNY_TO_EUR
eur_net = eur * (1 - commission)

print(f"{eur_net :.2f}")
