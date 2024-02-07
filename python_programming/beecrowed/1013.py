values = input().split()
a = int(values[0])
b = int(values[1])
c = int(values[2])

if a >= b and a >= c:
    print(f"{a} eh o maior")
elif  b >= a and b >= c:   
    print(f"{b} eh o maior")
else:
    print(f"{c} eh o maior")  