# Função para calcular o percentual
def calcular_percentual(total, quantidade):
    return (quantidade / total) * 100

# Dicionário para armazenar a quantidade de cada tipo de cobaia
cobaias = {'S': 0, 'R': 0, 'C': 0}

# Total de experimentos
N = int(input("Digite a quantidade de experimentos registrados: "))

# Lê os experimentos e atualiza o dicionário de cobaias
total_cobaias = 0
for _ in range(N):
    quantidade, tipo = input("Digite a quantidade e o tipo de cobaia (S - Sapo, R - Rato, C - Coelho): ").split()
    quantidade = int(quantidade)
    cobaias[tipo] += quantidade
    total_cobaias += quantidade

# Imprime os resultados
print("Total de cobaias utilizadas:", total_cobaias)
for tipo, quantidade in cobaias.items():
    percentual = calcular_percentual(total_cobaias, quantidade)
    print(f"Total de {tipo}s: {quantidade}, Percentual: {percentual:.2f}%")
