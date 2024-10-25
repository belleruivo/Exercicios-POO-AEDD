from produto import Product

class VirtualStore:
    def __init__(self):
        self.produtos = []

    def criar_produto(self, nome, preco):
        return Product(nome, preco)

    def adicionar_produto(self, nome, preco):
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

    def buscar_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome.lower() == nome_produto.lower():
                return produto
        return None