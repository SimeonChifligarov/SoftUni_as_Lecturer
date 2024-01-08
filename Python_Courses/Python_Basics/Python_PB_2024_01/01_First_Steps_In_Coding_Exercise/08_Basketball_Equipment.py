# •	Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]
annual_fee = int(input())

# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
basketball_shoes = annual_fee * 0.60
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
basketball_equip = basketball_shoes * 0.80
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
basketball_ball = basketball_equip * 0.25
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
basketball_accessories = basketball_ball * 0.20

total_cost = annual_fee \
             + basketball_shoes \
             + basketball_equip \
             + basketball_ball \
             + basketball_accessories

# конзолата колко ще са разходите на Джеси, ако започне да спортува баскетбол.
print(total_cost)
