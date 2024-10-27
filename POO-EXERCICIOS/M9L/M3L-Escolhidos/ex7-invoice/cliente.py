class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.pedidos = []  # Lista de pedidos associados ao cliente

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)
        pedido.cliente = self  # Estabelece a relação bilateral

    def exibir_pedidos(self):
        print(f"\nPedidos de {self.nome} (CPF: {self.cpf}):")
        for pedido in self.pedidos:
            print(f"Pedido {pedido.num_pedido} - Valor total: R$ {pedido.calcular_valor_total():.2f}")