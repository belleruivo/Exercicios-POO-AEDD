class Pedido:
    def __init__(self, num_pedido):
        self.num_pedido = num_pedido
        self.cliente = None  # O cliente é associado posteriormente
        self.faturas = []  # Lista de faturas associadas ao pedido

    def adicionar_fatura(self, fatura):
        self.faturas.append(fatura)
        fatura.pedido = self  # Estabelece a relação bilateral

    def calcular_valor_total(self):
        return sum(fatura.calcular_fatura() for fatura in self.faturas)

    def exibir_detalhes_pedido(self):
        print(f"\nDetalhes do Pedido {self.num_pedido} para {self.cliente.nome}:")
        for fatura in self.faturas:
            print(f"Fatura {fatura.numFatura} - {fatura.descricao} - Quantidade: {fatura.quantidade} - Total: R$ {fatura.calcular_fatura():.2f}")
        print(f"Valor total do pedido: R$ {self.calcular_valor_total():.2f}")