def verificar_admissao(idade, jogou_tres_jogos, venceu_pelo_menos_um_jogo):
    if 16 <= idade <= 18 and jogou_tres_jogos and venceu_pelo_menos_um_jogo:
        return True
    else:
        return False

def main():
    idade = int(input("Qual é a sua idade? "))
    jogou_tres_jogos = input("Você já jogou pelo menos 3 jogos de tabuleiro? (True/False) ")
    venceu_pelo_menos_um_jogo = int(input("Quantas vezes você venceu um jogo? "))

    # Convertendo a entrada para o tipo correto
    jogou_tres_jogos = jogou_tres_jogos.lower() == 'true'

    pode_ser_admitido = verificar_admissao(idade, jogou_tres_jogos, venceu_pelo_menos_um_jogo)

    print("Pode ser admitido no clube? ", pode_ser_admitido)

if __name__ == "__main__":
    main()
