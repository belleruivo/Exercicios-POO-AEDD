class Fila:
    def __init__(self):
        self.items = []

    def inserir(self, item):
        """Insere um item no final da fila."""
        self.items.append(item)

    def remover(self):
        """Remove e retorna o item do início da fila."""
        if not self.esta_vazia():
            return self.items.pop(0)
        return None

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.items) == 0

    def elementos(self):
        """Retorna todos os elementos da fila."""
        return self.items
