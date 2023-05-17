deposit = float(input())
deposit_period = int(input())
annual_interest = float(input())
calculated_annual_interest = deposit * annual_interest / 100
monthly_interest = calculated_annual_interest / 12
final_interest = monthly_interest * deposit_period
final_deposit = deposit + final_interest
print(final_deposit)
