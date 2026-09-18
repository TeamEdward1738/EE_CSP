# EE, your_budget

income_monthly= float(input("tell me your monthly income: $"))

rent_monthly= float(input("tell me your monthly rent: $"))

utilities_monthly= float(input("tell me your monthly utilities: $"))

groceries_monthly= float(input("tell me your monthly groceries: $"))

transportation_monthly= float(input("tell me your monthly transportation: $"))

print(f"Your rent is ${rent_monthly:.2f} and that is {int(round(rent_monthly/income_monthly*100))}% of your income")

print(f"Your utilities bill is ${utilities_monthly:.2f} and that is {int(round(utilities_monthly/income_monthly*100))}% of your income")

print(f"Your groceries bill is ${groceries_monthly:.2f} and that is {int(round(groceries_monthly/income_monthly*100))}% of your income")

print(f"Your transportation bill is ${transportation_monthly:.2f} and that is {int(round(transportation_monthly/income_monthly*100))}% of your income")

print(f"You save ${income_monthly*0.1:.2f} a month and that is 10% of your income")
print(f"You have $550.00 of spending money each month")