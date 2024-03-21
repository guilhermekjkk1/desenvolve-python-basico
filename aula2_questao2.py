def verificar_entrada_bar(idade_juliana, idade_cris):
    if idade_juliana > 17 or idade_cris > 17:
        return True
    else:
        return False

def main():
    idade_juliana = int(input("Digite a idade da Juliana: "))
    idade_cris = int(input("Digite a idade da Cris: "))

    podem_entrar = verificar_entrada_bar(idade_juliana, idade_cris)

    print("Podem entrar no bar?", podem_entrar)

if __name__ == "__main__":
    main()
