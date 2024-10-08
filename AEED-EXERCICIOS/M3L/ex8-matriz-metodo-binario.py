'''
8. Elabore uma matriz com 500 linhas e 50 colunas, que deverá ser preenchida com
números inteiros aleatórios na faixa de 1 a 10.000. Faça a busca, pelo método binário,
de um elemento sorteado, indique a quantidade de elementos iguais a este presente
na matriz e indique a posição (ou as posições, caso aja repetição) em que ele se
encontra (i, j).
'''

import random

def criar_matriz(linhas, colunas, min_valor, max_valor):
    return [[random.randint(min_valor, max_valor) for _ in range(colunas)] for _ in range(linhas)]

def ordenar_matriz(matriz):
    for linha in matriz:
        linha.sort()

def busca_binaria(linha, elemento):
    esquerda, direita = 0, len(linha) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if linha[meio] == elemento:
            return meio
        elif linha[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def buscar_elemento_matriz(matriz, elemento):
    posicoes = []
    for i, linha in enumerate(matriz):
        indice = busca_binaria(linha, elemento)
        if indice != -1:
            esquerda = indice
            while esquerda >= 0 and linha[esquerda] == elemento:
                posicoes.append((i, esquerda))
                esquerda -= 1
            direita = indice + 1
            while direita < len(linha) and linha[direita] == elemento:
                posicoes.append((i, direita))
                direita += 1
    return posicoes

def main():
    linhas, colunas = 500, 50
    min_valor, max_valor = 1, 10000

    matriz = criar_matriz(linhas, colunas, min_valor, max_valor)
    ordenar_matriz(matriz)

    elemento_sorteado = random.randint(min_valor, max_valor)
    print(f"Elemento sorteado: {elemento_sorteado}")

    posicoes = buscar_elemento_matriz(matriz, elemento_sorteado)
    quantidade = len(posicoes)

    if quantidade > 0:
        print(f"Quantidade de elementos iguais a {elemento_sorteado}: {quantidade}")
        print("Posições (i, j):")
        for posicao in posicoes:
            print(posicao)
    else:
        print(f"O elemento {elemento_sorteado} não foi encontrado na matriz.")

main()