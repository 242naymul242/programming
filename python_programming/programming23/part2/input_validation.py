# import math
# while True:
#     given_number = int(input("Please type in a number: "))

#     if given_number == 0:
#         break
#     elif given_number < 0:
#         print("invalid number")
#     elif given_number > 0:    
#      root = math.sqrt(given_number)
#     print(root)
    
# print("Exiting...")    

import math


while True:
    given_number = int(input("Please type in a number: "))
    if given_number == 0:
        print("Exiting...")
        break
    elif given_number > 0:    
        given_number = math.sqrt(given_number)
        print(given_number)
    else:
        print("Invalid number")
    









