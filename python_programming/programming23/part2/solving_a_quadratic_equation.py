import math
a = float(input("Value of a: ")) 
b = float(input("Value of b: ")) 
c = float(input("Value of c: "))
root1 = (-b + math.sqrt(b**2-4*a*c))/(2*a) 
root2 = (-b - math.sqrt(b**2-4*a*c))/(2*a) 
print(f"The roots are {root1} and {root2}")