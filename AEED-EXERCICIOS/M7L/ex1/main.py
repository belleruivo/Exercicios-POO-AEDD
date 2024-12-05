'''1. Escreva um programa que, dados uma matriz de adjacência e dois nós de um grafo,
calcule:
a. O número de caminhos de determinado comprimento existentes entre eles.
b. O número total de caminhos existentes entre eles.'''

def multiplica_matrizes(matriz_a, matriz_b):
    n = len(matriz_a)
    resultado = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return resultado

def eleva_matriz(matriz, k):
    n = len(matriz)
    resultado = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # Matriz identidade
    for _ in range(k):
        resultado = multiplica_matrizes(resultado, matriz)
    return resultado

def caminhos_comprimento_k(matriz_adj, origem, destino, k):
    matriz_potencia = eleva_matriz(matriz_adj, k)
    print(f"A^{k} = {matriz_potencia}")  # Depuração: veja a matriz potência
    return matriz_potencia[origem][destino]

def total_caminhos(matriz_adj, origem, destino, max_comprimento):
    total = 0
    for k in range(1, max_comprimento + 1):
        caminhos = caminhos_comprimento_k(matriz_adj, origem, destino, k)
        print(f"Caminhos de comprimento {k}: {caminhos}")  # Depuração
        total += caminhos
    return total

# Exemplo
matriz_adjacencia = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

origem = 0
destino = 2
k = 2

print(f"Caminhos de comprimento {k} entre {origem} e {destino}:",
      caminhos_comprimento_k(matriz_adjacencia, origem, destino, k))

max_comprimento = 5
print(f"Caminhos totais até comprimento {max_comprimento} entre {origem} e {destino}:",
      total_caminhos(matriz_adjacencia, origem, destino, max_comprimento))
