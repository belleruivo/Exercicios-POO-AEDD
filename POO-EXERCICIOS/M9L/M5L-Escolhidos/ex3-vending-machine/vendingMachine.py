class VendingMachine:
    def __init__(self):
        self.estoque = {}
        self.saldo = 0.0

    def cadastrar_produto(self, nome, preco, quantidade, fornecedor=None):
        if nome in self.estoque:
            self.estoque[nome]['quantidade'] += quantidade
        else:
            self.estoque[nome] = {'preco': preco, 'quantidade': quantidade, 'fornecedor': fornecedor}
        print(f"Produto {nome} cadastrado com sucesso na máquina de vendas!")

    def selecionar_produto(self, nome):
        if nome not in self.estoque:
            print(f"Produto {nome} não disponível.")
            return None
        produto = self.estoque[nome]
        if produto['quantidade'] <= 0:
            print(f"Produto {nome} esgotado.")
            return None
        return produto

    def inserir_dinheiro(self, valor):
        if valor <= 0:
            print("Valor inválido. O valor deve ser positivo.")
            return
        self.saldo += valor
        print(f"R$ {valor:.2f} inserido. Saldo atual: R$ {self.saldo:.2f}")

    def comprar_produto(self, nome, cliente):
        produto = self.selecionar_produto(nome)
        if produto is None:
            return

        if self.saldo < produto['preco']:
            print(f"Saldo insuficiente. O preço do produto é R$ {produto['preco']:.2f}.")
            return

        self.saldo -= produto['preco']
        produto['quantidade'] -= 1
        print(f"Compra realizada com sucesso! Você comprou: {nome}. Troco: R$ {self.saldo:.2f}")
        self.saldo = 0
        cliente.adicionar_compra(nome)  # Adiciona ao histórico de compras do cliente

    def retornar_troco(self):
        if self.saldo > 0:
            print(f"Retornando troco: R$ {self.saldo:.2f}")
            self.saldo = 0
        else:
            print("Não há troco a ser retornado.")

    def exibir_estoque(self):
        if not self.estoque:
            print("Estoque vazio.")
            return
        print("Estoque disponível:")
        for nome, info in self.estoque.items():
            fornecedor = info['fornecedor'].nome if info['fornecedor'] else "Desconhecido"
            print(f"{nome}: R$ {info['preco']:.2f} - Quantidade: {info['quantidade']} - Fornecedor: {fornecedor}")