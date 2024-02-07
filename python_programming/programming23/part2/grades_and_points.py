given_points = int(input("How many points [0-100]: "))

if given_points < 0:
    print("Grade: impossible!")
elif given_points >= 0 and given_points <= 49:
    print("Grade: fail")
elif given_points >= 50 and given_points <= 59:
    print("Grade: 1")
elif given_points >= 60 and given_points <= 69:        
    print("Grade: 2")
elif given_points >= 70 and given_points <= 79:
    print("Grade: 3")
elif given_points >= 80 and given_points <= 89:
    print("Grade: 4")
elif given_points >= 90 and given_points <= 100: 
    print("Grade: 5")
elif given_points > 100:
    print("impossible!")               