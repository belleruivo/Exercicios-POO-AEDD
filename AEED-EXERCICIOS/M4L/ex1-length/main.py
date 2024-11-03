'''
1. Defina uma função length (não len) que espera uma estrutura unicamente ligada
como argumento. A função retorna o número de itens na estrutura.
'''
from linkedList import LinkedList
from node import Node

def length(linked_list): #uma instância da classe LinkedList.
    current = linked_list.head
    count = 0
    while current:
        count += 1
        current = current.next
    return count

def menu():
    option = -1

    while(option < 0 or option > 2):
        print("\n1 - Preencher a lista com x elementos.\n" +
            "2 - Exibir comprimento da lista")
        option = int(input("Digite sua opção: "))
        if (option < 0 or option > 2):
            print("\tOpção inválida! Tente novamente")

    return option


def main():
    print("-="*15, "LINKED LIST", "-="*15)
    choice = 100
    my_list = LinkedList()

    while choice != 0:
        choice = menu()

        if choice == 1:
            print("\nDigite os elementos da lista (0 para sair):")
            while True:
                elem = int(input("Digite um elemento: "))
                if elem == 0:
                    break

                new_node = Node(elem, my_list.head)
                my_list.head = new_node
            print("\nElementos inseridos na lista.")

        else:
            print("\nValores na lista:", end=" ")
            current = my_list.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("||") 

            length_of_list = length(my_list)
            print("Comprimento da lista:", length_of_list)
            break
    print("-="*35)
main()

