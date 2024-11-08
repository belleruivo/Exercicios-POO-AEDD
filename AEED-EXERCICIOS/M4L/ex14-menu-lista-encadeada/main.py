# Faça um programa que implemente uma lista encadeada de números inteiros com inserção de dados 
# pelo usuário através de um menu. Escreva uma função que inverta a ordem das células de uma lista 
# encadeada (a primeira passa a ser a última, a segunda passa a ser a penúltima, etc).
# Faça isso sem usar espaço auxiliar, apenas alterando ponteiros. Dê duas soluções: uma iterativa e uma recursiva 

from node import Node

def inserir_lista(head, data):
    novo_no = Node(data)
    if not head:
        return novo_no
    current = head
    while current.next:
        current = current.next
    current.next = novo_no
    return head

# Função iterativa para inverter a lista
def inverter_lista_iterativa(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Guarda o próximo nó
        current.next = prev       # Inverte o ponteiro
        prev = current            # Avança o ponteiro "prev"
        current = next_node       # Avança para o próximo nó
    return prev  # O "prev" será o novo head da lista invertida

# Função recursiva para inverter a lista
def inverter_lista_recursiva(head):
    # Caso base: se a lista está vazia ou tem apenas um nó, retorna o próprio nó
    if not head or not head.next:
        return head
    
    # Inverte o resto da lista
    rest = inverter_lista_recursiva(head.next)
    
    # Inverte o ponteiro do nó atual
    head.next.next = head
    head.next = None  # O antigo primeiro nó agora se torna o último, então seu próximo é None
    
    return rest  # Retorna o novo head da lista invertida

def imprimir_lista(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def main():
    head = None
    while True:
        print("\nMenu:")
        print("1- Inserir número na lista")
        print("2- Inverter lista (Iterativo)")
        print("3- Inverter lista (Recursivo)")
        print("4- Imprimir lista")
        print("5- Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            numero = int(input("Digite um número para inserir na lista: "))
            head = inserir_lista(head, numero)
        elif opcao == 2:
            head = inverter_lista_iterativa(head)
            print("Lista invertida (iterativamente).")
        elif opcao == 3:
            head = inverter_lista_recursiva(head)
            print("Lista invertida (recursivamente).")
        elif opcao == 4:
            print("Lista atual:")
            imprimir_lista(head)
        elif opcao == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
