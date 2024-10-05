'''17. Crie uma aplicação que permita inserir cerca de 10 mil números inteiros aleatórios de
1 a 10 mil num vetor de inteiros. Registre o tempo de início e término da operação de
ordenação e compare essas diferenças entre os algoritmos bubbleSort, insertionSort
e quickSort. Comente as diferenças e considere testar com números diferentes de
elementos. Dica: quando tiver rodando os algoritmos, evite executar outros
programas na máquina.'''

import random
import time

def gerarLista(size=10000, minimo=1, maximo=10000):
    random_list = []
    for c in range(size):
        number = random.randint(minimo, maximo)
        random_list.append(number)
    return random_list

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def insertionSort(list):
    for i in range(1, len(list)):
        itemToInsert = list[i]
        j = i -1
        while j >= 0 and itemToInsert < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = itemToInsert

def bubbleSort(list):
    n = len(list)
    while n  > 1:
        swapped = False
        i = 1
        while i < n:
            if list[i] < list[i-1]:
                swap(list, i, i-1)
                swapped = True
            i += 1
        if not swapped:return
        n -=1

def partition(list, left, right):
    middle = (left+right)//2
    pivot = list[middle]
    list[middle] = list[right]
    list[right] = pivot
    boundary = left
    for index in range(left, right):
        if list[index]<pivot:
            swap(list, index, boundary)
            boundary += 1
    swap (list, right, boundary)
    return boundary

def quicksortHelper(list, left, right):
    if left < right:
        pivotLocation = partition(list, left, right)
        quicksortHelper(list, left, pivotLocation-1)
        quicksortHelper(list, pivotLocation + 1, right)

def quickSort(list):
    quicksortHelper(list, 0, len(list)-1)

def measure_sort_time(sort_function, list, *args):
    start_time = time.time()
    sort_function(list, *args)
    end_time = time.time()
    return end_time - start_time

listaAleatoria = gerarLista()

listaBubble= listaAleatoria.copy()
listaInsertion = listaAleatoria.copy()
listaQuickSort = listaAleatoria.copy()

time_bubble = measure_sort_time(bubbleSort, listaBubble)
time_insertion = measure_sort_time(insertionSort, listaInsertion)
time_quick = measure_sort_time(quickSort, listaQuickSort)

print(f"Tempo Bubble Sort: {time_bubble:.6f} segundos")
print(f"Tempo Insertion Sort: {time_insertion:.6f} segundos")
print(f"Tempo Quick Sort: {time_quick:.6f} segundos")

