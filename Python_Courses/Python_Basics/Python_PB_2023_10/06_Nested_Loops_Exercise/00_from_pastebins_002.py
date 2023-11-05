town = input()
package = input()
vip_access = input()
days = int(input())

total_cost = 0

if days > 7:
    days -= 1

if town == "Bansko" or town == "Borovets":
    if package == "withEquipment":
        price = 100
        cost = days * price
        if vip_access == "yes":
            total_cost = cost * 0.9
        elif vip_access == "no":
            total_cost = cost
    elif package == "noEquipment":
        price = 80
        cost = days * price
        if vip_access == "yes":
            total_cost = cost * 0.95
        elif vip_access == "no":
            total_cost = cost
    if days <= 0:
        print("Days must be positive number!")
    else:
        print(f"The price is {total_cost:.2f}lv! Have a nice time!")
elif town == "Varna" or town == "Burgas":
    if package == "withBreakfast":
        price = 130
        cost = days * price
        if vip_access == "yes":
            total_cost = cost * 0.88
        elif vip_access == "no":
            total_cost = cost
    elif package == "noBreakfast":
        price = 100
        cost = days * price
        if vip_access == "yes":
            total_cost = cost * 0.93
        elif vip_access == "no":
            total_cost = cost
    if days <= 0:
        print("Days must be positive number!")
    else:
        print(f"The price is {total_cost:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
