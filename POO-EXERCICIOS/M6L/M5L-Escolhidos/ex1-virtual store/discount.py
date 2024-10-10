from cart import Cart

class Discount:
    @staticmethod
    def aplicar_desconto(carrinho: Cart, porcentagem_desconto: int):
        for produto in carrinho.itens:
            produto.preco -= produto.preco * (porcentagem_desconto / 100)
        print(f"Desconto de {porcentagem_desconto}% aplicado a todos os produtos no carrinho.\n")