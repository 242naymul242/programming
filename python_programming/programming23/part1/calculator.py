geven_number1 = int(input("Number 1: "))
geven_number2 = int(input("Number 2: "))
Operation = input("Operation:")
if Operation == "add":
    add = geven_number1 + geven_number2
    print(f"{geven_number1} + {geven_number2} = {add} ")
if Operation == "multiply":
    multiply = geven_number1 * geven_number2
    print(f"{geven_number1} * {geven_number2} = {multiply} ")    
    
if Operation == "subtract":
    subtract = geven_number1 - geven_number2
    print(f"{geven_number1} - {geven_number2} = {subtract} ")    
    