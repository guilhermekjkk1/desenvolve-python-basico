def calcular_diferenca_absoluta(num1, num2):
    diferenca = abs(num1 - num2)
    return round(diferenca, 2)

def main():
    try:
        num1 = float(input("Digite o primeiro número decimal: "))
        num2 = float(input("Digite o segundo número decimal: "))
        
        diferenca_absoluta = calcular_diferenca_absoluta(num1, num2)
        
        print(f"A diferença absoluta entre {num1} e {num2} é: {diferenca_absoluta}")
    except ValueError:
        print("Por favor, insira números válidos.")

if __name__ == "__main__":
    main()
