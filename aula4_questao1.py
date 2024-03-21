def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    soma = num1 + num2

    print("A soma dos números é", verificar_par_ou_impar(soma))

if __name__ == "__main__":
    main()
