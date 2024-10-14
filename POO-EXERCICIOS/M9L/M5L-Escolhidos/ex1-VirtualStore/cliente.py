class Cliente:
    def __init__(self, nome, email, loja=None):
        self.nome = nome
        self.email = email
        self.carrinho = []
        self.loja = loja  # Referência à loja

        # Se a loja for fornecida, adicione este cliente a ela
        if loja:
            loja.adicionar_cliente(self)

    def adicionar_ao_carrinho(self, produto):
        self.carrinho.append(produto)

    def calcular_total(self):
        return sum(produto.preco for produto in self.carrinho)

    def mostrar_carrinho(self):
        if not self.carrinho:
            print(f"{self.nome}, seu carrinho está vazio!\n")
            return
        print(f"Itens no carrinho de {self.nome}:")
        for produto in self.carrinho:
            print(produto)
        print()