class Invoice:
    def __init__(self, numFatura, cliente, itens):
        self.numFatura = numFatura
        self.cliente = cliente
        self.itens = itens  # Lista de tuplas (Produto, quantidade)

    def calcular_fatura(self):
        total = sum(produto.preco * qtd for produto, qtd in self.itens)
        return total

    def exibir_fatura(self):
        print(f"\nFatura {self.numFatura} para {self.cliente.nome} (CPF: {self.cliente.cpf})")
        print("-" * 30)
        for produto, qtd in self.itens:
            print(f"{produto.descricao} - Quantidade: {qtd} - Preço unitário: R$ {produto.preco:.2f}")
        total = self.calcular_fatura()
        print(f"\nTotal da fatura: R$ {total:.2f}")