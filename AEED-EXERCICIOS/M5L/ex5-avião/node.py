class Node:
    def __init__(self, data, next=None):
        self.data = data      # O dado (avião) armazenado no nó.
        self.next = next      # O ponteiro para o próximo nó (inicialmente None).