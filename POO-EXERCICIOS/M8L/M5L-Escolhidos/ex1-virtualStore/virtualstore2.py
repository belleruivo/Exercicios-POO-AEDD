from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calcular_desconto(self, preco):
        pass

class DiscountPercentage(Discount):
    def __init__(self, valor):
        self.valor = valor

    def calcular_desconto(self, preco):
        return preco * (self.valor / 100)

class DiscountFixed(Discount):
    def __init__(self, valor):
        self.valor = valor

    def calcular_desconto(self, preco):
        return self.valor
    
class DiscountManager:
    def __init__(self):
        self.desconto = None

    def definir_desconto(self, desconto: Discount):
        self.desconto = desconto

    def aplicar_desconto(self, total):
        if self.desconto:
            return total - self.desconto.calcular_desconto(total)
        return total

class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome}: R$ {self.preco:.2f}"

class Cart:
    def __init__(self):
        self.itens = []
        self.discount_manager = DiscountManager() 

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        total = sum(produto.preco for produto in self.itens)
        total = self.discount_manager.aplicar_desconto(total) 
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
        self.discount_manager.definir_desconto(desconto)  
        print("Desconto definido para o carrinho.\n")

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

def obter_entrada(mensagem, tipo=str, positivo=False):
    while True:
        try:
            entrada = input(mensagem).replace(',', '.')
            entrada = tipo(entrada)
            if positivo and entrada < 0:
                raise ValueError("O valor não pode ser negativo.")
            return entrada
        except ValueError:
            print(f"Entrada inválida. Tente novamente.\n")

def main():
    loja = VirtualStore()
    carrinho = Cart()  
    print("-=" * 30)

    while True:
        print("\nMenu:")
        print("1. Cadastrar Produto")
        print("2. Mostrar Produtos")
        print("3. Adicionar ao Carrinho")
        print("4. Mostrar Carrinho")
        print("5. Aplicar Desconto")
        print("6. Finalizar Compra")

        escolha = input("\nEscolha uma opção: ")
        print()

        if escolha == '1':
            nome = input("Digite o nome do produto: ")
            preco = obter_entrada("Digite o preço do produto: R$ ", tipo=float, positivo=True)
            loja.adicionar_produto(nome, preco)
        elif escolha == '2':
            loja.mostrar_produtos()
        elif escolha == '3':
            nome_produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
            produto = loja.buscar_produto(nome_produto)
            if produto:
                carrinho.adicionar_produto(produto)
                print(f"Produto '{produto.nome}' adicionado ao carrinho!\n")
            else:
                print(f"Produto '{nome_produto}' não encontrado.\n")
        elif escolha == '4':
            carrinho.mostrar_carrinho()
            total = carrinho.calcular_total()
            print(f"Total da compra: R$ {total:.2f}\n")
        elif escolha == '5':
            tipo_desconto = input("Digite o tipo de desconto (percentual/fixo): ").lower()
            if tipo_desconto not in ["percentual", "fixo"]:
                print("Tipo de desconto inválido! Tente novamente.\n")
                continue

            valor_desconto = obter_entrada(
                f"Digite o valor do desconto {'(%)' if tipo_desconto == 'percentual' else '(R$)'}: ", 
                tipo=float, positivo=True
            )
            if tipo_desconto == "percentual":
                desconto = DiscountPercentage(valor_desconto)
            else:
                desconto = DiscountFixed(valor_desconto)

            carrinho.definir_desconto(desconto)
        elif escolha == '6':
            carrinho.mostrar_carrinho()
            total = carrinho.calcular_total()
            print(f"Total da compra: R$ {total:.2f}\n")
            print("Compra Finalizada. Obrigado!")
            print("-=" * 30)
            break
        else:
            print("Opção inválida! Tente novamente.\n")

main()