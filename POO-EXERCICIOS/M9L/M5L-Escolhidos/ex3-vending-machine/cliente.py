class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.historico_compras = []

    def comprar_produto(self, vending_machine, nome_produto):
        vending_machine.comprar_produto(nome_produto, self)

    def adicionar_compra(self, nome_produto):
        self.historico_compras.append(nome_produto)
        print(f"{self.nome} comprou {nome_produto}.")

    def exibir_historico_compras(self):
        if not self.historico_compras:
            print(f"{self.nome} ainda não realizou compras.")
        else:
            print(f"Histórico de compras de {self.nome}: {', '.join(self.historico_compras)}")