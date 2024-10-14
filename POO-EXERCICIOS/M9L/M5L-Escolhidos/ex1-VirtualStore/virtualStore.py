from product import Product
from pagamento import Pagamento
from cliente import Cliente

class VirtualStore:
    def __init__(self):
        self.produtos = []
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    @classmethod
    def criar_produto(cls, nome, preco):
        return Product(nome, preco)

    def produto_existe(self, nome):
        """Verifica se um produto com o mesmo nome já está cadastrado."""
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return True
        return False
    
    def adicionar_produto(self):
        nome = input("Digite o nome do produto: ")
        if self.produto_existe(nome):
            print(f"Produto '{nome}' já cadastrado!\n")
            return
        
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

    def adicionar_ao_carrinho(self, cliente):
        nome_produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
        for produto in self.produtos:
            if produto.nome.lower() == nome_produto.lower():
                cliente.adicionar_ao_carrinho(produto)
                print(f"Produto '{produto.nome}' adicionado ao carrinho!\n")
                return
        print(f"Produto '{nome_produto}' não encontrado.\n")

    def aplicar_desconto(self, cliente):
        if not cliente.carrinho:
            print("O carrinho está vazio!\n")
            return
        
        while True:
            porcentagem_desconto = input("Digite a porcentagem de desconto (%): ")
            if porcentagem_desconto.isdigit():
                porcentagem_desconto = int(porcentagem_desconto)
                break
            else:
                print("Entrada inválida! Digite apenas números inteiros.\n")
        
        for produto in cliente.carrinho:
            produto.preco -= produto.preco * (porcentagem_desconto / 100)
        
        print(f"Desconto de {porcentagem_desconto}% aplicado a todos os produtos no carrinho de {cliente.nome}.\n")

    def finalizar_compra(self, cliente):
        if not cliente.carrinho:
            print("O carrinho está vazio!\n")
            return
        
        total = cliente.calcular_total()
        cliente.mostrar_carrinho()
        print(f"Total da compra: R$ {total:.2f}\n")

        tipo_pagamento = self.obter_pagamento()
        pagamento = Pagamento(tipo_pagamento, total)
        pagamento.processar_pagamento()
        print("Compra finalizada com sucesso!\n")

    def obter_pagamento(self):
        while True:
            tipo = input("Escolha o tipo de pagamento (cartão/dinheiro): ").strip().lower()
            if tipo in ['cartao', 'cartão', 'dinheiro']:
                return tipo
            print("Tipo de pagamento inválido! Tente novamente.\n")

    def obter_entrada(self, mensagem, tipo=str, positivo=False):
        while True:
            try:
                entrada = tipo(input(mensagem))
                if positivo and entrada < 0:
                    raise ValueError("O valor não pode ser negativo.")
                return entrada
            except ValueError:
                print(f"Entrada inválida. Tente novamente.\n")

    def selecionar_cliente(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.\n")
            return None
        print("Clientes cadastrados:")
        for i, cliente in enumerate(self.clientes, start=1):
            print(f"{i}. {cliente.nome}")
        
        while True:
            escolha = self.obter_entrada("Escolha o número do cliente: ", tipo=int, positivo=True)
            if 1 <= escolha <= len(self.clientes):
                return self.clientes[escolha - 1]
            print("Opção inválida! Tente novamente.\n")

    def cliente_existe(self, nome, email):
        for cliente in self.clientes:
            if cliente.nome.lower() == nome.lower() or cliente.email.lower() == email.lower():
                return True
        return False

    def cadastrar_cliente(self):
        while True:
            nome_cliente = input("Digite o nome do cliente: ").lower()
            if nome_cliente.replace(" ", "").isalpha():
                break
            print("Nome inválido. Certifique-se de inserir somente letras.\n")
        email_cliente = input("Digite o e-mail do cliente: ").lower()

        if self.cliente_existe(nome_cliente, email_cliente):
            print(f"Cliente '{nome_cliente}' já está cadastrado!\n")
        else:
            cliente = Cliente(nome_cliente, email_cliente, self)  # Passando a loja para o cliente
            print(f"Cliente '{cliente.nome}' cadastrado com sucesso!\n")