taka = int(input())

print(taka)
note100 = taka // 100
print(f"{note100} nota(s) de R$ 100,00")
now_taka = taka - note100 * 100
note50 = now_taka // 50
print(f"{note50} nota(s) de R$ 50,00")
now_taka = now_taka - note50 * 50
note20 = now_taka // 20
print(f"{note20} nota(s) de R$ 20,00")
now_taka = now_taka - note20 * 20
note10 = now_taka // 10
print(f"{note10} nota(s) de R$ 10,00")
now_taka = now_taka - note10 * 10
note5 = now_taka // 5
print(f"{note5} nota(s) de R$ 5,00")
now_taka = now_taka - note5 * 5
note2 = now_taka // 2
print(f"{note2} nota(s) de R$ 2,00")
now_taka = now_taka - note2 * 2
note1 = now_taka // 1 
print(f"{note1} nota(s) de R$ 1,00")





