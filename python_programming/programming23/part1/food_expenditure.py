times = float(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
spent_on_groceries = float(input("How much money do you spend on groceries in a week? "))
Weekly_total_cost = times * price + spent_on_groceries
avarage = Weekly_total_cost / 7
print("Average food expenditure:")
print(f"Daily: {avarage} euros")
print(f"Weekly: {Weekly_total_cost} euros")
