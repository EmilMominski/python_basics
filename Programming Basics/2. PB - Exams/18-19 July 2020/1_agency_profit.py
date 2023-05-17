# User's Input
company_name = input()
adult_ticket_count = int(input())
children_ticket_count = int(input())
adult_net_price = float(input())
fee = float(input())

# Logic
children_net_price = adult_net_price - adult_net_price * 70 / 100
children_gross_price = children_net_price + fee
adult_gross_price = adult_net_price + fee
total_children_price = children_gross_price * children_ticket_count
total_adult_price = adult_gross_price * adult_ticket_count
total_price = total_children_price + total_adult_price
profit = total_price * 20 / 100

# Print Output
print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")
