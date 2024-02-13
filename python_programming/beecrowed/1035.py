number = input().split()
a = int(number[0])
b = int(number[1])
c = int(number[2])
d = int(number[3])
sum1 = c + d
sum2 = a + b

# if b > c:
#     if d > a:
#         if sum1 > sum2:
#             if  c > 0 :
#                 if d > 0:
#                     if a %2 == 0:
#                         print("Valores aceitos")
#                     else:
#                         print("Valores nao aceitos")
#                 else:
#                     print("Valores nao aceitos")        
#             else:
#                 print("Valores nao aceitos")  
#         else:
#             print("Valores nao aceitos")                  
#     else:
#         print("Valores nao aceitos")
# else:
#     print("Valores nao aceitos")


if b > c and d > a and sum1 > sum2 and c > 0 and d > 0 and a %2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")    