class Cart:
    def __init__(self):
        self.itens = []
        self.desconto = None

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        total = sum(produto.preco for produto in self.itens)
        if self.desconto:
            total -= self.desconto.calcular_desconto(total)
        return max(total, 0)

    def mostrar_carrinho(self):
        if not self.itens:
            print("O carrinho está vazio!\n")
            return
        print("Itens no carrinho:")
        for produto in self.itens:
            print(produto)
        print()
        
    def definir_desconto(self, desconto):
        self.desconto = desconto
        print(f"Desconto definido para o carrinho.\n")