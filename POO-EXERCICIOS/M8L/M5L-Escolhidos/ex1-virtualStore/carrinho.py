from descontos import *

class Cart:
    def __init__(self, discount_manager: DiscountManager):  # Injeção de dependência
        self.itens = []
        self.discount_manager = discount_manager  # Usando a instância recebida

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        total = sum(produto.preco for produto in self.itens)
        total = self.discount_manager.aplicar_desconto(total)  # Aplica desconto usando DiscountManager
        return max(total, 0)

    def mostrar_carrinho(self):
        if not self.itens:
            print("O carrinho está vazio!\n")
            return
        print("Itens no carrinho:")
        for produto in self.itens:
            print(produto)
        print()

    def definir_desconto(self, desconto: Discount):
        self.discount_manager.definir_desconto(desconto)  # Delegar para DiscountManager
        print("Desconto definido para o carrinho.\n")
