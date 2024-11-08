'''
Crie uma aplicação que permita inserir cerca de 8 mil números inteiros aleatórios de 1 a 8 mil num vetor de inteiros. Faça um comparativo considerando o número de trocas realizadas entre os algoritmos selectionSort, mergeSort e quickSort. Comente as diferenças e considere testar com números diferentes de elementos. Dica: quando tiver rodando os algoritmos, evite executar outros programas na máquina.
'''

import random
import time

# Função para gerar um vetor com números aleatórios
def gerar_vetor(tamanho):
    return [random.randint(1, 8000) for _ in range(tamanho)]

# Função para realizar a troca de elementos no vetor
def swap(lista, i, j):
    """Troca os itens nas posições i e j"""
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp

# Função de SelectionSort com contagem de trocas, utilizando a função swap
def selectionSort(vetor):
    trocas = 0
    n = len(vetor)
    
    # Laço principal
    for i in range(n - 1):  # Não precisamos procurar no último elemento
        # Assume-se que o menor elemento é o da posição i
        menor = i
        
        # Laço para encontrar o menor elemento na parte não ordenada
        for j in range(i + 1, n):
            if vetor[j] < vetor[menor]:
                menor = j
        
        # Se o menor não for o elemento atual, fazemos a troca
        if i != menor:
            swap(vetor, i, menor)
            trocas += 1

    return trocas

# Função de MergeSort com contagem de trocas
def mergeSort(vetor):
    trocas = 0

    def merge(vetor, esquerda, direita):
        nonlocal trocas
        if esquerda < direita:
            meio = (esquerda + direita) // 2
            trocas += merge(vetor, esquerda, meio)
            trocas += merge(vetor, meio + 1, direita)
            trocas += merge_intercalacao(vetor, esquerda, meio, direita)
        return trocas

    def merge_intercalacao(vetor, esquerda, meio, direita):
        nonlocal trocas
        n1 = meio - esquerda + 1
        n2 = direita - meio
        L = vetor[esquerda:meio+1]
        R = vetor[meio+1:direita+1]
        i = j = k = 0
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                vetor[k] = L[i]
                i += 1
            else:
                vetor[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            vetor[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            vetor[k] = R[j]
            j += 1
            k += 1
        return 1  # Indica que houve uma troca na intercalação, mesmo que o vetor não tenha sido trocado

    return merge(vetor, 0, len(vetor) - 1)

# Função de QuickSort com contagem de trocas
def quickSort(vetor):
    trocas = 0
    
    def partition(vetor, low, high):
        nonlocal trocas
        pivot = vetor[high]
        i = low - 1
        for j in range(low, high):
            if vetor[j] <= pivot:
                i += 1
                vetor[i], vetor[j] = vetor[j], vetor[i]
                trocas += 1
        vetor[i + 1], vetor[high] = vetor[high], vetor[i + 1]
        trocas += 1
        return i + 1

    def sort(vetor, low, high):
        if low < high:
            pi = partition(vetor, low, high)
            sort(vetor, low, pi - 1)
            sort(vetor, pi + 1, high)
    
    sort(vetor, 0, len(vetor) - 1)
    return trocas

# Função para testar e comparar os algoritmos
def testar_algoritmos(tamanho):
    # Gerar o vetor aleatório
    vetor = gerar_vetor(tamanho)
    
    # Testar SelectionSort
    vetor_copy = vetor[:]
    start_time = time.time()
    trocas_selection = selectionSort(vetor_copy)
    selection_time = time.time() - start_time
    
    # Testar MergeSort
    vetor_copy = vetor[:]
    start_time = time.time()
    trocas_merge = mergeSort(vetor_copy)
    merge_time = time.time() - start_time
    
    # Testar QuickSort
    vetor_copy = vetor[:]
    start_time = time.time()
    trocas_quick = quickSort(vetor_copy)
    quick_time = time.time() - start_time
    
    # Exibir os resultados
    print(f"Resultados para {tamanho} elementos:")
    print(f"SelectionSort: {trocas_selection} trocas, tempo: {selection_time:.4f} segundos")
    print(f"MergeSort: {trocas_merge} trocas, tempo: {merge_time:.4f} segundos")
    print(f"QuickSort: {trocas_quick} trocas, tempo: {quick_time:.4f} segundos")

# Função principal
def main():
    tamanho = int(input("Digite o número de elementos (ex: 8000): "))
    testar_algoritmos(tamanho)

if __name__ == "__main__":
    main()
