'''13. Faça um programa que implemente uma lista encadeada de números inteiros com
inserção de dados pelo usuário através de um menu. Escreva uma função que insira
uma nova célula com conteúdo x imediatamente depois da k-ésima célula da lista
encadeada e outra função que troque de posição duas células de uma mesma lista.
Faça duas versões: uma iterativa e uma recursiva.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_after_k(self, k, data):
        new_node = Node(data)
        if k < 0:
            print("O índice k não pode ser negativo.")
            return
        
        current = self.head
        count = 0

        while current is not None:
            if count == k:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            count += 1

        print("A lista não contém uma k-ésima célula.")

    def swap_nodes_iterative(self, k1, k2):
        if k1 == k2:
            return

        prev1 = None
        curr1 = self.head
        count1 = 0

        while curr1 and count1 != k1:
            prev1 = curr1
            curr1 = curr1.next
            count1 += 1

        prev2 = None
        curr2 = self.head
        count2 = 0

        while curr2 and count2 != k2:
            prev2 = curr2
            curr2 = curr2.next
            count2 += 1

        if not curr1 or not curr2:
            print("Um dos índices está fora dos limites.")
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    def swap_nodes_recursive(self, k1, k2):
        def swap_helper(current, count1, count2):
            if current is None:
                return None

            if count1 == 0:
                self.node1 = current
            if count2 == 0:
                self.node2 = current

            current.next = swap_helper(current.next, count1 - 1, count2 - 1)

            return current

        self.node1 = None
        self.node2 = None

        self.head = swap_helper(self.head, k1, k2)

        if self.node1 and self.node2:
            self.node1.data, self.node2.data = self.node2.data, self.node1.data

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    linked_list = LinkedList()

    while True:
        print("\nMenu:")
        print("1. Inserir um número após a k-ésima célula")
        print("2. Trocar duas células de posição")
        print("3. Imprimir a lista")
        print("4. Sair")
        try:
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                try:
                    k = int(input("Digite a posição k: "))
                    data = int(input("Digite o número a ser inserido: "))
                    linked_list.insert_after_k(k, data)
                except ValueError:
                    print("Erro: Por favor, insira um número válido para k e o dado.")

            elif choice == 2:
                try:
                    k1 = int(input("Digite a posição da primeira célula: "))
                    k2 = int(input("Digite a posição da segunda célula: "))
                    linked_list.swap_nodes_iterative(k1, k2)
                    # linked_list.swap_nodes_recursive(k1, k2)  # Para usar a versão recursiva, descomente esta linha
                except ValueError:
                    print("Erro: Por favor, insira números válidos para as posições.")

            elif choice == 3:
                linked_list.print_list()

            elif choice == 4:
                break

            else:
                print("Opção inválida, tente novamente.")
                
        except ValueError:
            print("Erro: Por favor, insira um número válido para a opção.")

main()