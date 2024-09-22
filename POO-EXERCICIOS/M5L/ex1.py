'''1. Crie uma classe chamada VirtualStore que represente uma plataforma de vendas
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho
de compras, aplicar descontos e calcular o valor total da compra.'''

class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome}: R$ {self.preco:.2f}"


class VirtualStore:
    def __init__(self):
        self.produtos = []
        self.carrinho = []

    def adicionar_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = self.obter_entrada("Digite o preço do produto: R$ ", tipo=float, positivo=True)
        produto = Product(nome, preco)
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
                self.carrinho.append(produto)
                print(f"Produto '{produto.nome}' adicionado ao carrinho!\n")
                return
        print(f"Produto '{nome_produto}' não encontrado.\n")

    def aplicar_desconto(self):
        porcentagem_desconto = self.obter_entrada("Digite a porcentagem de desconto (Sem %): ", tipo=float, positivo=True)
        for produto in self.carrinho:
            produto.preco -= produto.preco * (porcentagem_desconto / 100)
        print(f"Desconto de {porcentagem_desconto}% aplicado a todos os produtos no carrinho.\n")

    def calcular_total(self):
        total = sum(produto.preco for produto in self.carrinho)
        return total

    def finalizar_compra(self):
        if not self.carrinho:
            print("O carrinho está vazio!\n")
            return
        total = self.calcular_total()
        print("Itens no carrinho:")
        for produto in self.carrinho:
            print(produto)
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


def main():
    loja = VirtualStore()
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
            loja.adicionar_produto()
        elif escolha == '2':
            loja.mostrar_produtos()
        elif escolha == '3':
            loja.adicionar_ao_carrinho()
        elif escolha == '4':
            loja.aplicar_desconto()
        elif escolha == '5':
            loja.finalizar_compra()
        elif escolha == '6':
            print("Saindo da loja. Obrigado!")
            print("-=" * 30)
            break
        else:
            print("Opção inválida! Tente novamente.\n")


main()