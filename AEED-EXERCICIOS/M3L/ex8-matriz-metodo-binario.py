'''
8. Elabore uma matriz com 500 linhas e 50 colunas, que deverá ser preenchida com
números inteiros aleatórios na faixa de 1 a 10.000. Faça a busca, pelo método binário,
de um elemento sorteado, indique a quantidade de elementos iguais a este presente
na matriz e indique a posição (ou as posições, caso aja repetição) em que ele se
encontra (i, j).
'''

import random  # importa o módulo random para gerar números aleatórios

def criar_matriz(linhas, colunas, min_valor, max_valor):
    # cria uma matriz com 'linhas' linhas e 'colunas' colunas, preenchida com números aleatórios entre 'min_valor' e 'max_valor'
    return [[random.randint(min_valor, max_valor) for _ in range(colunas)] for _ in range(linhas)]

def ordenar_matriz(matriz):
    # ordena cada linha da matriz em ordem crescente
    for linha in matriz:
        linha.sort()

def busca_binaria(linha, elemento):
    # realiza uma busca binária em uma linha para encontrar o 'elemento'
    esquerda, direita = 0, len(linha) - 1  # define os limites esquerdo e direito da busca
    while esquerda <= direita:  # enquanto a parte não verificada da linha não for vazia
        meio = (esquerda + direita) // 2  # encontra o índice do meio
        if linha[meio] == elemento:  # se o elemento do meio é o procurado
            return meio  # retorna o índice do meio
        elif linha[meio] < elemento:  # se o elemento do meio é menor que o procurado
            esquerda = meio + 1  # move o limite esquerdo para a direita do meio
        else:  # se o elemento do meio é maior que o procurado
            direita = meio - 1  # move o limite direito para a esquerda do meio
    return -1  # retorna -1 se o elemento não for encontrado

def buscar_elemento_matriz(matriz, elemento):
    # busca o 'elemento' em toda a matriz e retorna uma lista de posições onde ele é encontrado
    posicoes = []  # inicializa uma lista vazia para armazenar as posições
    for i, linha in enumerate(matriz):  # percorre cada linha da matriz com seu índice
        indice = busca_binaria(linha, elemento)  # realiza a busca binária na linha
        if indice != -1:  # se o elemento foi encontrado na linha
            # Verifica todas as ocorrências do elemento na linha
            esquerda = indice
            while esquerda >= 0 and linha[esquerda] == elemento:  # verifica para a esquerda do índice encontrado
                posicoes.append((i, esquerda))  # adiciona a posição à lista
                esquerda -= 1  # move para a esquerda
            direita = indice + 1
            while direita < len(linha) and linha[direita] == elemento:  # verifica para a direita do índice encontrado
                posicoes.append((i, direita))  # adiciona a posição à lista
                direita += 1  # move para a direita
    return posicoes  # retorna a lista de posições

def main():
    linhas, colunas = 500, 50  # define o número de linhas e colunas da matriz
    min_valor, max_valor = 1, 10000  # define o valor mínimo e máximo dos números aleatórios

    matriz = criar_matriz(linhas, colunas, min_valor, max_valor)  # cria a matriz com os valores definidos
    ordenar_matriz(matriz)  # ordena cada linha da matriz

    elemento_sorteado = random.randint(min_valor, max_valor)  # sorteia um elemento aleatório entre min_valor e max_valor
    print(f"Elemento sorteado: {elemento_sorteado}")  # imprime o elemento sorteado

    posicoes = buscar_elemento_matriz(matriz, elemento_sorteado)  # busca o elemento sorteado na matriz
    quantidade = len(posicoes)  # conta a quantidade de posições encontradas

    if quantidade > 0:  # se o elemento foi encontrado
        print(f"Quantidade de elementos iguais a {elemento_sorteado}: {quantidade}")  # imprime a quantidade de elementos encontrados
        print("Posições (i, j):")  # imprime o cabeçalho das posições
        for posicao in posicoes:  # percorre cada posição encontrada
            print(posicao)  # imprime a posição
    else:  # se o elemento não foi encontrado
        print(f"O elemento {elemento_sorteado} não foi encontrado na matriz.")  # imprime que o elemento não foi encontrado

main()  # chama a função principal para executar o programa