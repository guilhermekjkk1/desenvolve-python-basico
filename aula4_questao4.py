def calcular_frete(distancia, peso):
    if peso > 10:
        frete = 10  # Taxa fixa para pacotes com peso superior a 10 kg
    else:
        if distancia <= 100:
            frete = peso * 1
        elif 101 <= distancia <= 300:
            frete = peso * 1.5
        else:
            frete = peso * 2
    return frete

def main():
    distancia = float(input("Digite a distância da entrega em quilômetros: "))
    peso = float(input("Digite o peso do pacote em quilogramas: "))

    valor_frete = calcular_frete(distancia, peso)

    print("O valor do frete é R$", valor_frete)

if __name__ == "__main__":
    main()
