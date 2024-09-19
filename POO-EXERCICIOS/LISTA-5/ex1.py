'''1. Crie uma classe chamada VirtualStore que represente uma plataforma de vendas
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho
de compras, aplicar descontos e calcular o valor total da compra.'''

class Produto:
    def __init__(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque

    def __repr__(self):
        return f"{self.nome} - ${self.preço:2f} (Estoque: {self.estoque})"

class ItemCarrinho:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def total_preço(self):
        return self.produto.preço * self.quantidade
    
class VirtualStore:
    def __init__(self):
        self.produto = []
        self.carrrinho = []
        self.disconto = 0

    def adicionar_produtos(self, nome, preço, estoque):
        produto = Produto(nome, preço, estoque)
        self.produtos.append(produto)
        print(f"Produto {nome} adicionado à loja" )

    def exibir_produtos(self):
        if not self.produtos:
            print("Nenhum produto disponível na loja")
        else:
            for idx, produto in enumerate(self.produtos, 1):    
                print(f"{idx}. {produto}")
    
    def adicionar_ao_carrinho(self, indice_produto, quantidade):
        if 0 < indice_produto <= len(self.produtos):
            produto = self.produtos[indice_produto - 1]
            if produto.estoque >= quantidade:
                item_carrinho = ItemCarrinho(produto, quantidade)
                self.carrinho.aapend(item_carrinho)
                produto.estoque -= quantidade
                print(f"{quantidade} unidades de {produto.nome} adicionadas ao carrinho")
            else:
                print(f"Estoque insuficiente para {produto.nome}")
        else:
            print("Produto nõ encontrado")

    def aplicar_desconto(self, porcentual):
        if 0 <= porcentual <= 100:
            self.desconto = porcentual
            print(f"Desconto de {porcentual}% aplicado.")
        else:
            print("Porcentagem de desconto inválida")

    def calcular_total(self):
        total = sum(item.preço_total() for item in self.carrinho)
        total_com_desconto = total* (1 - self.desconto/100)

    def exibir_carrinho(self):
        if not self.carrinho:
            print("Carrinho vazio")
        else:
            for idx, item in enumerate(self.carrinho, 1):
                print(f"`{idx}. {item.produto.nome} - Quantidade: {item.quantidade} - Prelo total: R${item.preço_total():.2f}")
            print(f"Total (com desconto): R${self.calcular_total():.2f}")