class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.acervo = []

    def adicionar_item(self, item):
        self.acervo.append(item)
        print("Item adicionado com sucesso!\n")

    def listar_acervo(self):
        print("-"*35)
        print(f"   Acervo da Biblioteca {self.nome}:")
        print("-"*35)
        for item in self.acervo:
            print(item.descricao())