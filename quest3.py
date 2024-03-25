import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 10)
    
    while True:
        try:
            palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))
            
            if palpite < 1 or palpite > 10:
                print("Por favor, insira um número dentro do intervalo válido.")
                continue
            
            if palpite < numero_secreto:
                print("O número é maior. Tente novamente!")
            elif palpite > numero_secreto:
                print("O número é menor. Tente novamente!")
            else:
                print("Parabéns! Você acertou o número!")
                break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    adivinhar_numero()
