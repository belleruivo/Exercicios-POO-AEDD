from product import Product

class Cart:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto: Product):
        self.itens.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao carrinho!\n")

    def calcular_total(self):
        return sum(produto.preco for produto in self.itens)

    def mostrar_itens(self):
        if not self.itens:
            print("O carrinho está vazio!\n")
            return
        print("Itens no carrinho:")
        for produto in self.itens:
            print(produto)