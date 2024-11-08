'''
Faça um programa que implemente uma lista encadeada de números inteiros com
inserção de dados pelo usuário através de um menu. Escreva uma função que faça
uma cópia da lista e outra função que concatene duas listas encadeadas (isto é,
engate a segunda no fim da primeira). Faça duas versões da função: uma iterativa e
uma recursiva.
'''

from lista import LinkedList

def menu():
    print("\n1 - Inserir número na lista 1")
    print("2 - Inserir número na lista 2")
    print("3 - Imprimir lista 1")
    print("4 - Imprimir lista 2")
    print("5 - Copiar lista 1")
    print("6 - Concatenar listas (Iterativo)")
    print("7 - Concatenar listas (Recursivo)")
    print("0 - Sair")

def main():
    lista1 = LinkedList()
    lista2 = LinkedList()

    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            num = int(input("Digite um número para a lista 1: "))
            lista1.inserir(num)

        elif opcao == 2:
            num = int(input("Digite um número para a lista 2: "))
            lista2.inserir(num)

        elif opcao == 3:
            print("Lista 1: ", end="")
            lista1.imprimir()

        elif opcao == 4:
            print("Lista 2: ", end="")
            lista2.imprimir()

        elif opcao == 5:
            lista_copia = lista1.copiar()
            print("Cópia da lista 1: ", end="")
            lista_copia.imprimir()

        elif opcao == 6:
            lista_copia = lista1.copiar()
            lista_copia.concatenar_iterativa(lista2)
            print("Lista 1 concatenada com lista 2 (Iterativo): ", end="")
            lista_copia.imprimir()

        elif opcao == 7:
            lista_copia = lista1.copiar()
            lista_copia.concatenar_recursiva(lista2)
            print("Lista 1 concatenada com lista 2 (Recursivo): ", end="")
            lista_copia.imprimir()

        elif opcao == 0:
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
