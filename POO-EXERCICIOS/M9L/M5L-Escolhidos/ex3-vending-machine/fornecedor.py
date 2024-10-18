class Fornecedor:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.produtos_fornecidos = []

    def fornecer_produto(self, nome, preco, quantidade, vending_machine):
        vending_machine.cadastrar_produto(nome, preco, quantidade, self)
        self.produtos_fornecidos.append(nome)
        print(f"Fornecedor {self.nome} forneceu {quantidade} unidades de {nome}.")