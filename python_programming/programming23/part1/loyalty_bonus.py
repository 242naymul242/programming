points = float(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
    print(f"You now have {points:.3f} points")
    
elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")
    print(f"You now have {points:.3f} points")

