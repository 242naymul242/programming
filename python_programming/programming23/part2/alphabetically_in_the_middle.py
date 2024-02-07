letters1 = input("1st letter: ")
letters2 = input("2nd letter: ")
letters3 = input("3rd letter: ")

if letters1 > letters2 and letters1 < letters3:
    print(f"The letter in the middle is {letters1}")
elif letters2 > letters1 and letters2 < letters3:
    print(f"The letter in the middle is {letters2}")
elif letters3 > letters1 and letters3 < letters2:
    print(f"The letter in the middle is {letters3}")    
elif letters1 > letters3 and letters1 < letters2:
    print(f"The letter in the middle is {letters1}")
elif letters2 > letters3 and letters3 < letters1:
    print(f"The letter in the middle is {letters2}")
elif letters3 > letters2 and letters3 < letters1:
    print(f"The letter in the middle is {letters3}")            