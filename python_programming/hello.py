attempts = 0
while True:
    pin = int(input("PIN: "))
    attempts += 1
    if pin != 4321:
        print("wrong")

    
    elif pin == 4321:
        print(f"Correct! It took you {attempts} attempts")
        break
        
        
    elif pin == 4321:
        print("Correct! It only took you one single attempt!")
        break   