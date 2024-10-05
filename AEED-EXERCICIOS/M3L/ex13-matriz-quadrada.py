'''13. Crie uma aplicação que implemente uma matriz quadrada com n números inteiros, os
quais devem ser fornecidos aleatoriamente pelo usuário. Implemente um menu com
duas opções:
a. Colocar os elementos em ordem crescente (use o insertionSort).
b. Colocar os elementos em ordem decrescente (use o selectionSort).'''

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def selectionSort(list):
    i = 0
    for i in range(len(list)):
        maxIndex = i
        for j in range(i+1, len(list)):
            if list[j] > list[maxIndex]:
                maxIndex = j
        if maxIndex !=i:
            swap(list, maxIndex, i)


def insertionSort(list):
    for i in range(1, len(list)):
        itemToInsert = list[i]
        j = i -1
        while j >= 0 and itemToInsert < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = itemToInsert
    

def printMatriz(matriz):
    for c in matriz:
        print(c)


def criarMatriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for c in range(n):
            while True:
                try:
                    valor = int(input(f"Insira o valor do índice {i+1}x{c+1}: "))
                    break
                except ValueError:
                    print("Valor inválido! Por favor, insira um número inteiro.")
            linha.append(valor)
        matriz.append(linha)
    return matriz

def matrizParaLista(matriz):
    lista = []
    for c in matriz:
        lista.extend(c)
    return lista

def listaParaMatriz(lista, n):
    matriz = []
    for i in range(0, len(lista), n):
        matriz.append(lista[i:i+n])
    return matriz


def main():
    while True:
        try:
            n = int(input("Digite o tamanho da matriz quadrada (n): "))
            if n <= 0:
                print("O tamanho da matriz deve ser um número inteiro positivo.\n")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.\n")
    
    matriz = criarMatriz(n)
    
    print("\nMatriz original:")
    printMatriz(matriz)
    
    lista = matrizParaLista(matriz)
    
    while True:
        print("\nEscolha uma opção:")
        print("a) Colocar os elementos em ordem crescente (Insertion Sort)")
        print("b) Colocar os elementos em ordem decrescente (Selection Sort)")
        opção = input("\nOpção: ").strip().lower()

        if opção == "a":
            insertionSort(lista)
            print("\nMatriz em ordem crescente:")
            break
        elif opção == "b":  
            selectionSort(lista)
            print("\nMatriz em ordem decrescente:")
            break
        else:
            print("Opção inválida! Por favor, escolha 'a' ou 'b'.")

    sortedMatrix = listaParaMatriz(lista, n)
    
    printMatriz(sortedMatrix)

main()