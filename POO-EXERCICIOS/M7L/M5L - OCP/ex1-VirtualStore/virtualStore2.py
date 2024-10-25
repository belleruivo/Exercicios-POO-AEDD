'''1. Crie uma classe chamada VirtualStore que represente uma plataforma de vendas
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho
de compras, aplicar descontos e calcular o valor total da compra.'''

class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, desconto):
        self.preco -= desconto.calcular_desconto(self.preco)

    def __str__(self):
        return f"{self.nome}: R$ {self.preco:.2f}"


class Discount:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def calcular_desconto(self, preco):
        if self.tipo == "percentual":
            return preco * (self.valor / 100)
        elif self.tipo == "fixo":
            return self.valor
        else:
            return 0


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        return sum(produto.preco for produto in self.itens)

    def mostrar_carrinho(self):
        if not self.itens:
            print("O carrinho está vazio!\n")
            return
        print("Itens no carrinho:")
        for produto in self.itens:
            print(produto)
        print()
        
    def aplicar_desconto(self, desconto):
        for produto in self.itens:
            produto.aplicar_desconto(desconto)
        print(f"Desconto '{desconto.tipo}' aplicado aos produtos no carrinho.\n")


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
            entrada = tipo(input(mensagem))
            if positivo and entrada < 0:
                raise ValueError("O valor não pode ser negativo.")
            return entrada
        except ValueError:
            print(f"Entrada inválida. Tente novamente.\n")


def main():
    loja = VirtualStore()
    carrinho = Carrinho()
    print("-=" * 30)

    while True:
        print("Menu:")
        print("1. Cadastrar Produto")
        print("2. Mostrar Produtos")
        print("3. Adicionar ao Carrinho")
        print("4. Aplicar Desconto")
        print("5. Finalizar Compra")
        print("6. Sair")

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
            tipo_desconto = input("Digite o tipo de desconto (percentual/fixo): ").lower()
            if tipo_desconto not in ["percentual", "fixo"]:
                print("Tipo de desconto inválido! Tente novamente.\n")
                continue

            valor_desconto = obter_entrada(
                f"Digite o valor do desconto {'(%)' if tipo_desconto == 'percentual' else '(em R$)'}: ", 
                tipo=float, positivo=True
            )
            desconto = Discount(tipo_desconto, valor_desconto)
            carrinho.aplicar_desconto(desconto)
        elif escolha == '5':
            carrinho.mostrar_carrinho()
            total = carrinho.calcular_total()
            print(f"Total da compra: R$ {total:.2f}\n")
        elif escolha == '6':
            print("Saindo da loja. Obrigado!")
            print("-=" * 30)
            break
        else:
            print("Opção inválida! Tente novamente.\n")


main()