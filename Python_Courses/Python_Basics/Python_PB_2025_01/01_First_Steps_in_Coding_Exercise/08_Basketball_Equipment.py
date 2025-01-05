# •	Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]
annual_fee = int(input())

# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
basket_sneakers = annual_fee * 0.60  # annual_fee * (1 - 0.40)
# print(basket_sneakers)
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
basket_equip = basket_sneakers * 0.80  # (1 - 0.20)
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
basket_ball = basket_equip * 0.25  # basket_equip / 4
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
basket_accessoires = basket_ball * 0.20  # basket_ball / 5

total_cost = annual_fee + basket_sneakers + basket_equip + basket_ball + basket_accessoires

print(total_cost)
