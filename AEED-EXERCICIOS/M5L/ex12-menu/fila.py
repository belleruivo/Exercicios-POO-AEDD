class Fila:
    def __init__(self):
        self.itens = []

    def inserir(self, item):
        """Insere um item no final da fila."""
        self.itens.append(item)

    def remover(self):
        """Remove e retorna o item do início da fila."""
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.itens) == 0

    def primeiro(self):
        """Retorna o primeiro item da fila sem removê-lo."""
        if not self.esta_vazia():
            return self.itens[0]
        return None

    def elementos(self):
        """Retorna todos os elementos da fila."""
        return self.itens