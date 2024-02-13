import math
number = input().split()
a = float(number[0])
b = float(number[1])
c = float(number[2])

calculation = (b**2) - (4*a*c)

while True:
    if a == 0:
        print("Impossivel calcular")
        break
    if calculation < 0:
        print("Impossivel calcular")
        break
   
    root1 = (-b + math.sqrt (calculation)) / (2 * a)
    root2 = (-b - math.sqrt (calculation)) / (2 * a)
    print(f"R1 = {root1:.5f}")
    print(f"R2 = {root2:.5f}")
    break