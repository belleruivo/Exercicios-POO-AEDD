from product import Product
from cart import Cart
from discount import Discount

class VirtualStore:
    def __init__(self):
        self.produtos = []
        self.carrinho = Cart()

    def criar_produto(self, nome, preco):
        return Product(nome, preco)

    def adicionar_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = self.obter_entrada("Digite o preço do produto: R$ ", tipo=float, positivo=True)
        produto = self.criar_produto(nome, preco)
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' cadastrado com sucesso!\n")

    def mostrar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.\n")
            return
        print("Produtos disponíveis:")
        for produto in self.produtos:
            print(f"● {produto}")
        print()

    def adicionar_ao_carrinho(self):
        nome_produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
        for produto in self.produtos:
            if produto.nome.lower() == nome_produto.lower():
                self.carrinho.adicionar_produto(produto)
                return
        print(f"Produto '{nome_produto}' não encontrado.\n")

    def aplicar_desconto(self):
        porcentagem_desconto = self.obter_entrada("Digite a porcentagem de desconto (Sem %): ", tipo=int, positivo=True)
        Discount.aplicar_desconto(self.carrinho, porcentagem_desconto)

    def finalizar_compra(self):
        total = self.carrinho.calcular_total()
        self.carrinho.mostrar_itens()
        print(f"Total da compra: R$ {total:.2f}\n")

    def obter_entrada(self, mensagem, tipo=str, positivo=False):
        while True:
            try:
                entrada = tipo(input(mensagem))
                if positivo and entrada < 0:
                    raise ValueError("O valor não pode ser negativo.")
                return entrada
            except ValueError:
                print(f"Entrada inválida. Tente novamente.\n")