from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Cabeça da lista, inicialmente vazia

    def isEmpty(self):
        return self.head is None  # Verifica se a lista está vazia

    # Função para inserir um nó após o nó apontado por p (Iterativo)
    def insert_after(self, p, x):
        if p is None:
            print("O nó dado não existe.")
            return
        new_node = Node(x)
        new_node.next = p.next  # O próximo do novo nó será o próximo do nó p
        new_node.previous = p  # O anterior do novo nó será o nó p
        if p.next:
            p.next.previous = new_node  # Se o próximo nó existir, ajustamos o ponteiro anterior
        p.next = new_node  # O próximo de p será o novo nó

    # Função recursiva para inserir um nó após o nó apontado por p
    def insert_after_recursive(self, p, x):
        if p is None:
            print("O nó dado não existe.")
            return
        self._insert_after_recursive(p, x)

    def _insert_after_recursive(self, p, x):
        if p.next is None:  # Se p for o último nó, podemos inserir após ele
            new_node = Node(x)
            p.next = new_node
            new_node.previous = p
        else:
            self._insert_after_recursive(p.next, x)

    # Função para remover o nó apontado por p (Iterativo)
    def remove(self, p):
        if p is None:
            print("O nó dado não existe.")
            return
        if p.previous:
            p.previous.next = p.next  # Ajusta o ponteiro do nó anterior
        if p.next:
            p.next.previous = p.previous  # Ajusta o ponteiro do próximo nó
        if p == self.head:
            self.head = p.next  # Se for o nó cabeça, o próximo nó se torna o cabeça
        p = None  # Desconecta o nó removido

    # Função recursiva para remover um nó
    def remove_recursive(self, p):
        if p is None:
            print("O nó dado não existe.")
            return
        self._remove_recursive(p)

    def _remove_recursive(self, p):
        if p.next is None:  # Se for o último nó
            if p.previous:
                p.previous.next = None  # Ajusta o ponteiro do nó anterior
        else:
            self._remove_recursive(p.next)
        if p.previous:
            p.previous.next = p.next
        if p.next:
            p.next.previous = p.previous
        if p == self.head:
            self.head = p.next
        p = None  # Desconecta o nó removido

    # Função para imprimir a lista
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Função para inserir um nó no início da lista
    def insert_front(self, x):
        new_node = Node(x)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

