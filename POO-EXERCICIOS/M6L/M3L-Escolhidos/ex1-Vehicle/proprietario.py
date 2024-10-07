class Proprietario:
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def imprimir(self):
        print(f"Nome do Proprietário: {self.nome}")
