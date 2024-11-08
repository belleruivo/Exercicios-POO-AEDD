from node import Node

class Queue:
    def __init__(self):
        self.head = None  # Primeira posição da fila (inicialmente vazia).
        self.tail = None  # Última posição da fila (inicialmente vazia).
        self.size = 0      # Contagem de itens na fila.

    def is_empty(self):
        return self.head is None

    def enqueue(self, airplane):
        new_node = Node(airplane)  # Cria um novo nó com o avião.
        if self.is_empty():
            # Se a fila estiver vazia, o novo nó será o primeiro e o último da fila.
            self.head = self.tail = new_node
        else:
            # Se a fila não estiver vazia, o novo nó será adicionado no final.
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1  # Incrementa o tamanho da fila.

    def dequeue(self):
        if self.is_empty():
            print("Não há aviões na fila.")
            return None
        removed_airplane = self.head.data  # Pega o avião na frente da fila.
        self.head = self.head.next  # Atualiza o head para o próximo nó.
        self.size -= 1  # Decrementa o tamanho da fila.
        if self.is_empty():
            self.tail = None  # Se a fila ficou vazia, o tail também deve ser None.
        return removed_airplane  # Retorna o avião removido.

    def peek(self):
        return self.head.data if self.head else None

    def list_airplanes(self):
        current = self.head
        airplanes = []
        while current:
            airplanes.append(current.data)  # Adiciona o avião na lista.
            current = current.next  # Vai para o próximo nó.
        return airplanes