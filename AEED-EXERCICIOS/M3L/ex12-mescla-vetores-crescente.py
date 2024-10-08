'''
12. Desenvolva uma aplicação que, dados dois vetores de inteiros quaisquer com
tamanho de 20 elementos, gere um terceiro com os elementos de ambos em ordem
crescente, usando o mergeSort. Apresente o resultado final.
'''

import random

def gerar_vetor(tamanho, min_valor, max_valor):
    return [random.randint(min_valor, max_valor) for _ in range(tamanho)]

def mesclar(vetor1, vetor2):
    return vetor1 + vetor2

def merge_sort(vetor):
    if len(vetor) > 1:
        meio = len(vetor) // 2
        esquerda = vetor[:meio]
        direita = vetor[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1

def main():
    tamanho = 20
    min_valor, max_valor = 1, 100

    vetor1 = gerar_vetor(tamanho, min_valor, max_valor)
    vetor2 = gerar_vetor(tamanho, min_valor, max_valor)

    print("Vetor 1:", vetor1)
    print("Vetor 2:", vetor2)

    vetor_mesclado = mesclar(vetor1, vetor2)

    merge_sort(vetor_mesclado)

    print("Vetor mesclado e ordenado:", vetor_mesclado)

main()