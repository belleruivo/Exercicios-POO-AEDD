from produto import Produto

class VendingMachine:
    def __init__(self, sistema_pagamento):
        self.estoque = {}
        self.sistema_pagamento = sistema_pagamento

    def cadastrar_produto(self, nome, preco, quantidade):
        if nome in self.estoque:
            self.estoque[nome].quantidade += quantidade
        else:
            self.estoque[nome] = Produto(nome, preco, quantidade)
        print(f"Produto {nome} cadastrado com sucesso!")

    def selecionar_produto(self, nome):
        if nome not in self.estoque:
            print(f"Produto {nome} não disponível.")
            return None
        produto = self.estoque[nome]
        if produto.quantidade <= 0:
            print(f"Produto {nome} esgotado.")
            return None
        return produto

    def comprar_produto(self, nome):
        produto = self.selecionar_produto(nome)
        if produto is None:
            return

        if not self.sistema_pagamento.processar_pagamento(produto.preco):
            return

        produto.quantidade -= 1
        print(f"Compra realizada com sucesso! Você comprou: {nome}.")
        self.sistema_pagamento.retornar_troco()

    def exibir_estoque(self):
        if not self.estoque:
            print("Estoque vazio.")
            return
        print("Estoque disponível:")
        for produto in self.estoque.values():
            print(produto)