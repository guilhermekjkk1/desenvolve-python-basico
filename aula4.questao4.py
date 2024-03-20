valor = int(input("Digite o valor em reais: "))
notas = [100, 50, 20, 10, 5, 2, 1]
#576

notas_100 = valor // 100 # 576 // 100 = 5
valor = valor % 100 # 576 - 5*100 = 76

notas_50 = valor // 50 # 76 // 50 = 1
valor = valor % 50 #valor - 50*notas_50 # 26

notas_20 = valor // 20 # 26 // 20 = 1
valor = valor % 20 #valor - 20*notas_20 # 6

notas_10 = valor // 10 # 6 // 10 = 0
valor = valor % 10 # 6
 
notas_5 = valor // 5 # 6 // 10 = 0
valor = valor % 5 # 1

notas_2 = valor // 2 # 1 // 2 = 0
valor = valor % 2 # 1

notas_1 = valor

print(f"{notas_100} nota(s) de 100")
print(f"{notas_50} nota(s) de 50")
print(f"{notas_20} nota(s) de 20")
print(f"{notas_10} nota(s) de 10")
print(f"{notas_5} nota(s) de 5")
print(f"{notas_2} nota(s) de 2")
print(f"{notas_1} nota(s) de 1")
