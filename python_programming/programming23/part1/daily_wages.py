hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_the_week = input("Day of the week: ")
daily_wages = hourly_wage * hours_worked
sum = daily_wages
if day_of_the_week == "Sunday":
    sum = daily_wages + daily_wages
print(f"Daily wages: {sum:.1f} euros")
