class Pilha:
    def __init__(self):
        self.stack = []

    def push(self, valor):
        self.stack.append(valor)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return " -> ".join(map(str, reversed(self.stack)))
