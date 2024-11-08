class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        """Adiciona um item no topo da pilha."""
        self.items.append(item)

    def desempilhar(self):
        """Remove e retorna o item do topo da pilha."""
        if not self.esta_vazia():
            return self.items.pop()
        return None

    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.items) == 0

    def elementos(self):
        """Retorna todos os elementos da pilha."""
        return self.items