import math

input1 = input().split()
input2 = input().split()
x1 = float(input1[0])
x2 = float(input2[0])
y1 = float(input1[1])
y2 = float(input2[1])
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"{distance:.4f}")