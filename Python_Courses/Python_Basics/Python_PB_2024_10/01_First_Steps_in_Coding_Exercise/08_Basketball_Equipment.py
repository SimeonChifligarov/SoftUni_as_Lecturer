# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

annual_fee = int(input())

sneakers = annual_fee * 0.60  # shoes = annual_fee * (1 - 40 / 100)
equip = sneakers * 0.80
ball = equip * 0.25  # ball = equip / 4
accessories = ball * 0.20  # accessories = ball / 5

total_result = annual_fee + sneakers + equip + ball + accessories

print(total_result)
