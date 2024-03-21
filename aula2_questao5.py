def pode_se_aposentar(genero, idade, tempo_de_servico):
    if genero == 'F':
        if idade > 60 or tempo_de_servico >= 30 or (idade >= 60 and tempo_de_servico >= 25):
            return True
        else:
            return False
    elif genero == 'M':
        if idade > 65 or tempo_de_servico >= 30 or (idade >= 65 and tempo_de_servico >= 25):
            return True
        else:
            return False
    else:
        return False  # Gênero inválido

def main():
    genero = input("Digite seu gênero (M/F): ")
    idade = int(input("Digite sua idade: "))
    tempo_de_servico = int(input("Digite seu tempo de serviço em anos: "))

    pode_aposentar = pode_se_aposentar(genero.upper(), idade, tempo_de_servico)

    print("Pode se aposentar?", pode_aposentar)

if __name__ == "__main__":
    main()
