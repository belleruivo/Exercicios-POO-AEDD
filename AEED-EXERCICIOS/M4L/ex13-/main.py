'''13. Faça um programa que implemente uma lista encadeada de números inteiros com inserção de dados pelo usuário através de um menu. Escreva uma função que insira uma nova célula com conteúdo x imediatamente depois da k-ésima célula da listaencadeada e outra função que troque de posição duas células de uma mesma lista. Faça duas versões: uma iterativa e uma recursiva.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_after(self, k, x):
        new_node = Node(x)
        current = self.head
        count = 0
        
        while current is not None and count < k:
            current = current.next
            count += 1
        
        if current is None:
            print(f"Não há {k} células na lista.")
            return
        
        new_node.next = current.next
        current.next = new_node

    def swap_nodes_iterative(self, x, y):
        if x == y:
            return

        prevX = None
        currX = self.head

        while currX and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head

        while currY and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX is None or currY is None:
            print("Um dos elementos não está na lista.")
            return

        if prevX:
            prevX.next = currY
        else:
            self.head = currY
        
        if prevY:
            prevY.next = currX
        else:
            self.head = currX
        
        # Swap next pointers
        currX.next, currY.next = currY.next, currX.next

    def swap_nodes_recursive(self, x, y):
        if x == y:
            return
        
        def swap_util(curr, prevX, prevY):
            if not curr:
                return None, None, None

            if curr.data == x:
                return curr, prevX, prevY
            elif curr.data == y:
                return None, prevX, curr

            next_node, px, py = swap_util(curr.next, curr, prevY if curr.data == y else prevX)

            if next_node:
                return next_node, prevX, py
            return curr, px, py

        self.head, _, _ = swap_util(self.head, None, None)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



def safe_input(prompt, expected_type=int):
    while True:
        try:
            return expected_type(input(prompt))
        except ValueError:
            print(f"Erro: Por favor, insira um número {expected_type.__name__} válido.\n")

def menu():
    linked_list = LinkedList()
    
    while True:
        print("\nMenu:")
        print("1. Inserir número")
        print("2. Inserir número após a k-ésima célula")
        print("3. Trocar duas células (iterativo)")
        print("4. Trocar duas células (recursivo)")
        print("5. Mostrar lista")
        print("6. Sair")

        choice = safe_input("Escolha uma opção: ")

        if choice == 1:
            num = safe_input("Digite um número: ")
            new_node = Node(num)
            if linked_list.head is None:
                linked_list.head = new_node
            else:
                current = linked_list.head
                while current.next:
                    current = current.next
                current.next = new_node
                
        elif choice == 2:
            k = safe_input("Digite a posição k: ")
            x = safe_input("Digite um número: ")
            linked_list.insert_after(k, x)
        
        elif choice == 3:
            x = safe_input("Digite o primeiro número a ser trocado: ")
            y = safe_input("Digite o segundo número a ser trocado: ")
            linked_list.swap_nodes_iterative(x, y)
        
        elif choice == 4:
            x = safe_input("Digite o primeiro número a ser trocado: ")
            y = safe_input("Digite o segundo número a ser trocado: ")
            linked_list.swap_nodes_recursive(x, y)
        
        elif choice == 5:
            linked_list.display()
        
        elif choice == 6:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

menu()