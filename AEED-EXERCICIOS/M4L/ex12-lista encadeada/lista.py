from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def inserir(self, data):
        """Insere um novo nó no final da lista."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def imprimir(self):
        """Imprime os elementos da lista."""
        if not self.head:
            print("Lista vazia!")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> " if current.next else "\n")
                current = current.next

    def copiar(self):
        """Cria uma cópia da lista."""
        copia_lista = LinkedList()
        current = self.head
        while current:
            copia_lista.inserir(current.data)
            current = current.next
        return copia_lista

    def concatenar_iterativa(self, outra_lista):
        """Concatena a outra lista ao final da lista atual (de forma iterativa)."""
        if not self.head:
            self.head = outra_lista.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = outra_lista.head

    def concatenar_recursiva(self, outra_lista):
        """Concatena a outra lista ao final da lista atual (de forma recursiva)."""
        if not self.head:
            self.head = outra_lista.head
        else:
            self._concatenar_recursiva_aux(self.head, outra_lista.head)

    def _concatenar_recursiva_aux(self, current, nova_head):
        """Função auxiliar para concatenar recursivamente."""
        if current.next is None:
            current.next = nova_head
        else:
            self._concatenar_recursiva_aux(current.next, nova_head)
