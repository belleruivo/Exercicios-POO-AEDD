class Transacao:
    def __init__(self):
        self.saldo = 0.0

    def inserir_dinheiro(self, valor):
        if valor <= 0:
            print("Valor inválido. O valor deve ser positivo.")
            return
        self.saldo += valor
        print(f"R$ {valor:.2f} inserido. Saldo atual: R$ {self.saldo:.2f}")

    def realizar_compra(self, produto):
        if self.saldo < produto.preco:
            print(f"Saldo insuficiente. O preço do produto é R$ {produto.preco:.2f}.")
            return False
        if not produto.reduzir_estoque():
            print(f"Produto {produto.nome} esgotado.")
            return False
        self.saldo -= produto.preco
        print(f"Compra realizada com sucesso! Você comprou: {produto.nome}. Troco: R$ {self.saldo:.2f}")
        return True

    def retornar_troco(self):
        if self.saldo > 0:
            print(f"Retornando troco: R$ {self.saldo:.2f}")
            self.saldo = 0
        else:
            print("Não há troco a ser retornado.")