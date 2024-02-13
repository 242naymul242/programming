print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum = 0
positive_count = 0
negative_count = 0

while True:
    number = int(input("Number: "))
    if number == 0:
        print(f"Numbers typed in {count}") 
        print(f"The sum of the numbers is {sum}")
        mean = sum / count
        print(f"The mean of the numbers is {mean}")
        print(f"Positive numbers {positive_count}")
        print(f"Negative numbers {negative_count}")
        break
    else:
        count += 1
        sum += number
        if number > 0:
            positive_count += 1
        else:
            negative_count += 1