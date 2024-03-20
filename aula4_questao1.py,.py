comprimento = int(input("Insira o comprimento do terreno em metros: "))
largura = int(input("Insira a largura do terreno em metros: "))
preco_m2 = float(input("Insira o preço do metro quadrado da região em R$: "))


area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2

print(f"O terreno possui {area_m2}m² e custa R${preco_total:,.2f}.")