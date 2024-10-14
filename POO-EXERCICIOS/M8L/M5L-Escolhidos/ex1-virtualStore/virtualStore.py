from produto import Produto
from cliente import Cliente
from pagamentos import PagamentoCartao, PagamentoDinheiro
from descontos import DescontoPercentual

class VirtualStore:
    #from pagamentos import PagamentoBoleto  # Nova classe de pagamento
    #loja = VirtualStore(pagamento_cartao_cls=PagamentoCartao, pagamento_dinheiro_cls=PagamentoDinheiro, pagamento_boleto_cls=PagamentoBoleto)
    
    def __init__(self, pagamento_cartao_cls=PagamentoCartao, pagamento_dinheiro_cls=PagamentoDinheiro):
        self.produtos = []
        self.clientes = []
        self.pagamentos = {
            'cartao': pagamento_cartao_cls,
            'dinheiro': pagamento_dinheiro_cls
        }
        self.descontos = {}

    def criar_produto(self, nome, preco):
        return Produto(nome, preco)

    def produto_existe(self, nome):
        return any(produto.nome.lower() == nome.lower() for produto in self.produtos)

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

    def aplicar_desconto(self, cliente, percentual):
        desconto = DescontoPercentual(percentual)
        desconto.aplicar(cliente)

    def finalizar_compra(self, cliente):
        if not cliente.carrinho:
            print("O carrinho está vazio!\n")
            return

        total = cliente.calcular_total()
        cliente.mostrar_carrinho()
        
        # Mostrar o total antes de solicitar o pagamento
        print(f"Total da compra: R$ {total:.2f}\n")
        pagamento = self.obter_pagamento(total)  # Solicita a forma de pagamento
        pagamento.processar_pagamento()  # Processa o pagamento
        print("Compra finalizada com sucesso!\n")

    def obter_pagamento(self, total):
        while True:
            tipo = input("Escolha o tipo de pagamento (cartão/dinheiro): ").strip().lower()
            if tipo in self.pagamentos:
                return self.pagamentos[tipo](total)
            else:
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

    def obter_email(self):
        while True:
            email = input("Digite o e-mail do cliente: ").strip().lower()
            if "@" in email:
                return email
            print("E-mail inválido! Tente novamente.\n")

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
        return any(cliente.nome.lower() == nome.lower() or cliente.email.lower() == email.lower() for cliente in self.clientes)