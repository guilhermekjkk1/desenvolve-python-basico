def verificar_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return "Bissexto"
    else:
        return "Não Bissexto"

def main():
    anos_teste = [1900, 2000, 2016, 2017]

    for ano in anos_teste:
        resultado = verificar_bissexto(ano)
        print(f"O ano {ano} é {resultado}.")

if __name__ == "__main__":
    main()
