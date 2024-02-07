given_number1 = int(input("Please type in the first number: "))
given_number2 = int(input("Please type in another number:"))
if given_number1 > given_number2:
    print(f"The greater number was: {given_number1}")

elif given_number2 > given_number1:
    print(f"The greater number was: {given_number2}")

else:
    print("The numbers are equal!")        
