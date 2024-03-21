def classificar_filme(avaliacao):
    if avaliacao == 5:
        return "Excelente!"
    elif avaliacao == 4:
        return "Muito Bom!"
    elif avaliacao == 3:
        return "Bom!"
    elif avaliacao == 2:
        return "Regular."
    elif avaliacao == 1:
        return "Ruim."
    else:
        return "Avaliação inválida. Por favor, insira uma avaliação de 1 a 5."

def main():
    avaliacao = int(input("Insira a avaliação do filme (de 1 a 5): "))

    mensagem = classificar_filme(avaliacao)

    print(mensagem)

if __name__ == "__main__":
    main()
