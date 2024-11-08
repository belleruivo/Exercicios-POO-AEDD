# Escreva um programa que recebe duas listas encadeadas de inteiros e efetue os
# seguintes passos:
# a. Verifique se as listas estão ordenadas;
# b. Ordene as listas, caso não estejam ordenadas;
# c. Mescle os elementos da segunda lista na primeira, mantendo a ordenação na lista
# final.

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def append(self, data):
        """Adiciona um novo nó no final da lista"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        """Imprime os elementos da lista"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def is_sorted(self):
        """Verifica se a lista está ordenada"""
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def sort(self):
        """Ordena a lista (usar o algoritmo de ordenação por inserção)"""
        if not self.head or not self.head.next:
            return  # Lista vazia ou com um único elemento já está ordenada

        # Usaremos o algoritmo de ordenação por inserção
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def sorted_insert(self, sorted_list, node):
        """Insere o nó na lista ordenada"""
        if not sorted_list or sorted_list.data >= node.data:
            node.next = sorted_list
            sorted_list = node
        else:
            current = sorted_list
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
        return sorted_list

    def merge(self, other):
        """Mescla a lista 'other' na lista atual, mantendo a ordem"""
        # Se uma das listas estiver vazia, retornamos a outra
        if not self.head:
            self.head = other.head
            return
        if not other.head:
            return
        
        # Mesclagem de duas listas ordenadas
        merged = None
        if self.head.data < other.head.data:
            merged = self.head
            self.head = self.head.next
        else:
            merged = other.head
            other.head = other.head.next
        
        current = merged
        
        while self.head and other.head:
            if self.head.data < other.head.data:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other.head
                other.head = other.head.next
            current = current.next

        # Se restarem elementos em uma das listas
        if self.head:
            current.next = self.head
        if other.head:
            current.next = other.head
        
        # Atualiza a cabeça da lista atual
        self.head = merged

def read_list():
    linked_list = LinkedList()
    while True:
        try:
            data = input("Digite um número (ou pressione Enter para terminar a lista): ")
            if data == "":  # Finaliza a lista se o usuário apertar Enter sem digitar nada
                break
            linked_list.append(int(data))  # Converte a entrada para inteiro e adiciona à lista
        except ValueError:
            print("Por favor, insira um número válido.")
    return linked_list

def main():
    print("Criando a primeira lista...")
    list1 = read_list()  # Lê os números para a primeira lista

    print("Criando a segunda lista...")
    list2 = read_list()  # Lê os números para a segunda lista

    print("\nLista 1 antes da mesclagem:")
    list1.print_list()

    print("Lista 2 antes da mesclagem:")
    list2.print_list()

    # a. Verificar se as listas estão ordenadas
    if list1.is_sorted():
        print("\nLista 1 já está ordenada.")
    else:
        print("\nLista 1 não está ordenada. Ordenando...")
        list1.sort()

    if list2.is_sorted():
        print("Lista 2 já está ordenada.")
    else:
        print("Lista 2 não está ordenada. Ordenando...")
        list2.sort()

    print("\nMesclando as duas listas:")
    list1.merge(list2)

    print("\nLista final após mesclagem:")
    list1.print_list()

main()
