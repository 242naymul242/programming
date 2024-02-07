given_number = int(input("Number: "))

if given_number % 3 == 0 and given_number % 5 == 0:
    print("FizzBuzz")        
elif given_number  % 3 == 0:
    print("Fizz")
elif given_number % 5 == 0:
    print("Buzz")
