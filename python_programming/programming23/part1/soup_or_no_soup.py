cost = float(5.90)
geven_name = input("Please tell me your name: ")
if geven_name != "Jerry":
    number_of_portion = float(input("How many portions of soup?"))
    total_cost = (number_of_portion) * (cost)
    print(f"The total cost is {total_cost:.1f}")
print("Next please!")    

