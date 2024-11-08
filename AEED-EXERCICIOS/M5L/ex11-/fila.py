from collections import deque

class Fila:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, valor):
        self.queue.append(valor)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return " -> ".join(map(str, self.queue)) if self.queue else "Fila vazia"
