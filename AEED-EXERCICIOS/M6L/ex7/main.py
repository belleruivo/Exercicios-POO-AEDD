'''
Faça um programa para executar as operações abaixo em uma árvore binária não ordenada.
Menu
1 – Inserir número aleatório com geração e inserção aleatórias
2 – Mostrar os números da árvore usando o imprimeRelacoes da questão 4
3 – Imprimir emOrdem, preOrdem e posOrdem
4 – Mostrar o maior número na árvore
5 – Sair
'''

from BinarySearchTree import BinaryTree
import random

def menu():
    print("\nMenu")
    print("1 – Inserir número aleatório com geração e inserção aleatórias")
    print("2 – Mostrar os números da árvore usando o imprimeRelacoes")
    print("3 – Imprimir em Ordem, Pré-Ordem e Pós-Ordem")
    print("4 – Mostrar o maior número na árvore")
    print("5 – Sair")

if __name__ == "__main__":
    bt = BinaryTree()
    while True:
        menu()
        choice = int(input("Escolha uma opção: "))
        if choice == 1:
            data = random.randint(0, 100)
            print(f'Inserindo número: {data}')
            bt.insert(bt.root, data)
        elif choice == 2:
            bt.imprimeRelacoes()
        elif choice == 3:
            print("\nEm Ordem:")
            bt.printInOrder(bt.root)
            print("\nPré-Ordem:")
            bt.printPreOrder(bt.root)
            print("\nPós-Ordem:")
            bt.printPostOrder(bt.root)
        elif choice == 4:
            print(f'Maior número na árvore: {bt.maxNode(bt.root)}')
        elif choice == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")
