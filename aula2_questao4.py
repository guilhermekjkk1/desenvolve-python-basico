def validar_ficha(classe, forca, magia):
    if classe.lower() == 'guerreiro':
        if forca >= 15 and magia <= 10:
            return True
        else:
            return False
    elif classe.lower() == 'mago':
        if forca <= 10 and magia >= 15:
            return True
        else:
            return False
    elif classe.lower() == 'arqueiro':
        if 5 < forca < 15 and 5 < magia < 15:
            return True
        else:
            return False
    else:
        return False

def main():
    classe = input("Escolha a classe do personagem (guerreiro, mago ou arqueiro): ")
    forca = int(input("Digite os pontos de força do personagem: "))
    magia = int(input("Digite os pontos de magia do personagem: "))

    ficha_valida = validar_ficha(classe, forca, magia)

    print("Ficha válida?", ficha_valida)

if __name__ == "__main__":
    main()
