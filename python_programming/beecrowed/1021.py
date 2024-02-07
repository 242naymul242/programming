taka_and_poisa = float(input())
taka = int(taka_and_poisa)
poisa = int((taka_and_poisa * 100) - (taka * 100))
print("NOTAS:")
note100 = int(taka // 100)
print(f"{note100} nota(s) de R$ 100.00")
now_taka = taka - note100 * 100
note50 = int(now_taka // 50)
print(f"{note50} nota(s) de R$ 50.00")
now_taka = now_taka - note50 * 50
note20 = int(now_taka // 20)
print(f"{note20} nota(s) de R$ 20.00")
now_taka = now_taka - note20 * 20
note10 = int(now_taka // 10)
print(f"{note10} nota(s) de R$ 10.00")
now_taka = now_taka - note10 * 10
note5 = int(now_taka // 5)
print(f"{note5} nota(s) de R$ 5.00")
now_taka = now_taka - note5 * 5
note2 = int(now_taka // 2)
print(f"{note2} nota(s) de R$ 2.00")
print("MOEDAS:")
now_taka = now_taka - note2 * 2
modes1 = int(now_taka // 1) 
print(f"{modes1} moeda(s) de R$ 1.00")

now_taka = poisa
modes2 = int(now_taka // 50)
print(f"{modes2} moeda(s) de R$ 0.50")
now_taka = now_taka - modes2 * 50
modes3 = int(now_taka // 25)
print(f"{modes3} moeda(s) de R$ 0.25")
now_taka = now_taka - modes3 * 25
modes4 = int(now_taka // 10)
print(f"{modes4} moeda(s) de R$ 0.10")

now_taka = now_taka - modes4 * 10
modes5 = int(now_taka // 5)
print(f"{modes5} moeda(s) de R$ 0.05")

now_taka = now_taka - modes5 * 5
modes6 = int(now_taka // 1)
print(f"{modes6} moeda(s) de R$ 0.01")









