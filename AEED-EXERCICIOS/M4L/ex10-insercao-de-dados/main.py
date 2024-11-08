# Faça um programa que implemente uma lista encadeada de números inteiros com
# inserção de dados pelo usuário através de um menu. Escreva uma função que
# verifique se esta lista está em ordem crescente e outra função que faça uma busca na
# lista, dado um elemento passado pelo usuário. Faça versões recursiva e iterativa.

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

def verificar_ordem_crescente_iterativa(head):
    if not head:
        return True
    
    current = head
    while current and current.next:
        if current.data > current.next.data:
            return False
        current = current.next
    return True

def verificar_ordem_crescente_recursiva(node):
    if not node or not node.next:
        return True
    if node.data > node.next.data:
        return False
    return verificar_ordem_crescente_recursiva(node.next)

def buscar_iterativo(head, elemento):
    current = head
    while current:
        if current.data == elemento:
            return True
        current = current.next
    return False

# Função recursiva para buscar um elemento na lista
def buscar_recursivo(head, elemento):
    if not head:
        return False
    if head.data == elemento:
        return True
    return buscar_recursivo(head.next, elemento)

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
        print("1. Inserir número na lista")
        print("2. Verificar se a lista está em ordem crescente (Iterativo)")
        print("3. Verificar se a lista está em ordem crescente (Recursivo)")
        print("4. Buscar um número na lista (Iterativo)")
        print("5. Buscar um número na lista (Recursivo)")
        print("6. Imprimir lista")
        print("7. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            numero = int(input("Digite um número para inserir na lista: "))
            head = inserir_lista(head, numero)
        elif opcao == 2:
            if verificar_ordem_crescente_iterativa(head):
                print("A lista está em ordem crescente.")
            else:
                print("A lista NÃO está em ordem crescente.")
        elif opcao == 3:
            if verificar_ordem_crescente_recursiva(head):
                print("A lista está em ordem crescente.")
            else:
                print("A lista NÃO está em ordem crescente.")
        elif opcao == 4:
            elemento = int(input("Digite o número a ser buscado: "))
            if buscar_iterativo(head, elemento):
                print(f"O número {elemento} foi encontrado na lista.")
            else:
                print(f"O número {elemento} não foi encontrado na lista.")
        elif opcao == 5:
            elemento = int(input("Digite o número a ser buscado: "))
            if buscar_recursivo(head, elemento):
                print(f"O número {elemento} foi encontrado na lista.")
            else:
                print(f"O número {elemento} não foi encontrado na lista.")
        elif opcao == 6:
            print("Lista atual:")
            imprimir_lista(head)
        elif opcao == 7:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
