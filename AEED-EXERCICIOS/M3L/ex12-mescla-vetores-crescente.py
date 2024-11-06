'''
12. Desenvolva uma aplicação que, dados dois vetores de inteiros quaisquer com
tamanho de 20 elementos, gere um terceiro com os elementos de ambos em ordem
crescente, usando o mergeSort. Apresente o resultado final.
'''

import random

# função para gerar um vetor de tamanho especificado com números aleatórios entre min_valor e max_valor
def gerar_vetor(tamanho, min_valor, max_valor):
    # usando list comprehension para preencher o vetor com números aleatórios
    # for _ in range(tamanho): significa que o laço será executado 'tamanho' vezes, mas a variável não será usada
    return [random.randint(min_valor, max_valor) for _ in range(tamanho)]

# função para mesclar dois vetores simplesmente concatenando-os
def mesclar(vetor1, vetor2):
    # concatena os dois vetores usando o operador +
    return vetor1 + vetor2

# implementação do algoritmo de ordenação merge sort
def merge_sort(vetor):
    # se o vetor tiver mais de um elemento, continua a dividir
    if len(vetor) > 1:
        # encontra o índice do meio do vetor para dividi-lo em duas partes
        meio = len(vetor) // 2

        # divide o vetor em duas partes: esquerda e direita
        esquerda = vetor[:meio]
        direita = vetor[meio:]

        # chamada recursiva para ordenar as duas metades
        merge_sort(esquerda)
        merge_sort(direita)

        # inicializa os índices para as sublistas esquerda, direita e o vetor principal
        i = j = k = 0

        # enquanto ainda houver elementos em ambas as sublistas
        while i < len(esquerda) and j < len(direita):
            # compara os elementos das duas sublistas e coloca o menor no vetor principal
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]  # coloca o elemento da esquerda
                i += 1  # avança o índice da sublista esquerda
            else:
                vetor[k] = direita[j]  # coloca o elemento da direita
                j += 1  # avança o índice da sublista direita
            k += 1  # avança o índice do vetor principal

        # caso ainda restem elementos na sublista esquerda, coloca-os no vetor principal
        while i < len(esquerda):
            vetor[k] = esquerda[i]  # coloca o elemento restante da esquerda
            i += 1  # avança o índice da sublista esquerda
            k += 1  # avança o índice do vetor principal

        # caso ainda restem elementos na sublista direita, coloca-os no vetor principal
        while j < len(direita):
            vetor[k] = direita[j]  # coloca o elemento restante da direita
            j += 1  # avança o índice da sublista direita
            k += 1  # avança o índice do vetor principal

# função principal que executa o programa
def main():
    tamanho = 20  # tamanho dos vetores
    min_valor, max_valor = 1, 100  # intervalo para os números aleatórios

    # gera dois vetores de tamanho 20 com números aleatórios entre 1 e 100
    vetor1 = gerar_vetor(tamanho, min_valor, max_valor)
    vetor2 = gerar_vetor(tamanho, min_valor, max_valor)

    # imprime os vetores gerados
    print("Vetor 1:", vetor1)
    print("Vetor 2:", vetor2)

    # mescla os dois vetores em um só
    vetor_mesclado = mesclar(vetor1, vetor2)

    # ordena o vetor mesclado usando o merge sort
    merge_sort(vetor_mesclado)

    # imprime o vetor mesclado e ordenado
    print("Vetor mesclado e ordenado:", vetor_mesclado)

# executa a função principal
main()