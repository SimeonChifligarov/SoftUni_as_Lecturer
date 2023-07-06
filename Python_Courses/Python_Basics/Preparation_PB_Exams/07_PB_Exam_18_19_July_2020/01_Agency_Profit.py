CHILD_TO_ADULT_PRICE_RATION = 0.30
NET_PROFIT_RATIO = 0.20

airline = input()
adult_tickets = int(input())
child_tickets = int(input())
adult_ticket_price = float(input())
service_extra_price = float(input())

child_ticket_price = adult_ticket_price * CHILD_TO_ADULT_PRICE_RATION

total_income = adult_tickets * adult_ticket_price + child_tickets * child_ticket_price \
               + (adult_tickets + child_tickets) * service_extra_price

total_net_profit = total_income * NET_PROFIT_RATIO
print(f"The profit of your agency from {airline} tickets is {total_net_profit :.2f} lv.")
