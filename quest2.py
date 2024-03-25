import random
from math import sqrt

def calcular_raiz_quadrada_soma(n):
    valores = [random.randint(0, 100) for _ in range(n)]
    soma = sum(valores)
    raiz_quadrada_soma = sqrt(soma)
    return raiz_quadrada_soma

def main():
    try:
        n = int(input("Digite o valor de n: "))
        if n <= 0:
            print("Por favor, insira um valor positivo para n.")
            return
        
        raiz_quadrada = calcular_raiz_quadrada_soma(n)
        print(f"A raiz quadrada da soma dos {n} valores inteiros aleatórios entre 0 e 100 é: {raiz_quadrada:.2f}")
    except ValueError:
        print("Por favor, insira um valor inteiro válido para n.")

if __name__ == "__main__":
    main()
