from transacao import Transacao
from produto import Produto

class VendingMachine:
    def __init__(self):
        self.estoque = {}
        self.transacao = Transacao()  # Associação com Transacao

    def cadastrar_produto(self, nome, preco, quantidade):
        if nome in self.estoque:
            self.estoque[nome].quantidade += quantidade
        else:
            self.estoque[nome] = Produto(nome, preco, quantidade)  # Associação com Produto
        print(f"Produto {nome} cadastrado com sucesso!")

    def exibir_estoque(self):
        if not self.estoque:
            print("Estoque vazio.")
            return
        print("Estoque disponível:")
        for produto in self.estoque.values():
            print(produto)

    def inserir_dinheiro(self, valor):
        self.transacao.inserir_dinheiro(valor)

    def comprar_produto(self, nome):
        if nome not in self.estoque:
            print(f"Produto {nome} não disponível.")
            return
        produto = self.estoque[nome]
        if self.transacao.realizar_compra(produto):
            print(f"Compra do produto {nome} realizada com sucesso.")

    def retornar_troco(self):
        self.transacao.retornar_troco()