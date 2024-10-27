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

def main():
    linked_list = LinkedList()
    
    while True:
        value = input("Digite um valor para adicionar à lista (ou 'sair' para encerrar): ")
        
        if value.lower() == 'sair':
            break
        
        #adiciona o novo nó ao final da lista
        new_node = Node(value)
        
        if linked_list.head is None:
            linked_list.head = new_node  #se a lista estiver vazia, define o novo nó como o cabeçote
        else:
            current = linked_list.head
            while current.next:  #percorre até o último nó
                current = current.next
            current.next = new_node  #adiciona o novo nó ao final da lista
    

    print("O comprimento da lista é:", length(linked_list))

main()
