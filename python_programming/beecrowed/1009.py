sellers_name = input()
fixed_salary = float(input())
sales_total = float(input())
bonus = (sales_total * 15) / 100 
total = fixed_salary + bonus
print(f"TOTAL = R$ {total:.2f}")