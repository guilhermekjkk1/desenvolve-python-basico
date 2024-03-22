n = int(input("Digite um número: "))
contador = int(input("Digite um contador: "))

if n < contador:
    print("Fim")
elif n > contador:
    contador += 1
    print(contador)
    n -= contador
    print("Fim")
