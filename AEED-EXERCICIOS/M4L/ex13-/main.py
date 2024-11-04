'''13. Faça um programa que implemente uma lista encadeada de números inteiros 
com inserção de dados pelo usuário através de um menu. Escreva uma função que 
insira uma nova célula com conteúdo x imediatamente depois da k-ésima célula 
da listaencadeada e outra função que troque de posição duas células de uma 
mesma lista. Faça duas versões: uma iterativa e uma recursiva.'''
from linkedList import LinkedList

def menu():
    option = -1

    while(option < 0 or option > 2):
        print("\n1 - Inserir no final.\n" +
            "2 - Inserir após a k-ésima célula\n" +
            "3 - Trocar posições (iterativo)\n" +
            "4. Trocar posições (recursivo)\n" +
            "5. Mostrar lista\n" +
            "6. Sair")
        try:
            option = int(input("Digite sua opção: "))
        except ValueError:
            print("\tOpção inválida! Tente novamente.")
            continue
        if (option < 0 or option > 6):
            print("\tOpção inválida! Tente novamente")
    return option
            


def main():
    print("-="*15, "LINKED LIST", "-="*15)
    choice = 100
    linked_list = LinkedList()
    
    while choice != 0:
        choice = menu()

        if choice == 1:
            data = int(input("Digite um número: "))
            linked_list.insert_at_end(data)
        elif choice == 2:
            k = int(input("Digite o índice k: "))
            data = int(input("Digite um número: "))
            linked_list.insert_after_k(k, data)
        elif choice == 3:
            x = int(input("Digite o primeiro número para trocar: "))
            y = int(input("Digite o segundo número para trocar: "))
            linked_list.swap_iterative(x, y)
        elif choice == 4:
            x = int(input("Digite o primeiro número para trocar: "))
            y = int(input("Digite o segundo número para trocar: "))
            linked_list.swap_recursive(x, y)
        elif choice == 5:
            linked_list.display()
        elif choice == 6:
            print("Saindo...")
        else:
            print("\tOpção inválida! Tente novamente.")
    print("-="*35) 
    
main() 