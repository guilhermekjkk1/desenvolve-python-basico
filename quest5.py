pip install emoji
import emoji

def listar_emojis():
    print("Lista de Emojis Disponíveis:")
    for emoji_key, emoji_name in emoji.UNICODE_EMOJI.items():
        print(f"{emoji_name} : {emoji_key}")

def emojizar_frase(frase_codificada):
    frase_decodificada = emoji.emojize(frase_codificada, use_aliases=True)
    return frase_decodificada

def main():
    listar_emojis()
    frase_codificada = input("\nDigite a frase codificada usando emojis: ")
    frase_decodificada = emojizar_frase(frase_codificada)
    print("\nFrase decodificada com emojis:")
    print(frase_decodificada)

if __name__ == "__main__":
    main()
