a = int(input())
b = int(input())
c = int(input())
d = int(input())
sum1 = c + d
sum2 = a + b

if b > c:
    if d > a:
        if sum1 > sum2:
            if  c > 0 :
                if d > 0:
                    if a %2 == 0:
                        print("Valores aceitos")
                    else:
                        print("Valores nao aceitos")
                else:
                    print("Valores nao aceitos")        
            else:
                print("Valores nao aceitos")  
        else:
            print("Valores nao aceitos")                  
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")