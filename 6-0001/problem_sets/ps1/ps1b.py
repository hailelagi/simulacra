annual_salary = float(input("Enter your annual salary"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal"))
total_cost = float(input("Enter the cost of your dream home"))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal"))

portion_down_payment = 0.25 * total_cost
current_savings = 0

months = 0

while current_savings < portion_down_payment:
    if months % 6 == 0 and months != 0:
        annual_salary += annual_salary * semi_annual_raise

    r = (current_savings * 0.04) / 12
    current_savings += ((annual_salary/12) * portion_saved) + r
    months += 1

print("Number of months: ", months)