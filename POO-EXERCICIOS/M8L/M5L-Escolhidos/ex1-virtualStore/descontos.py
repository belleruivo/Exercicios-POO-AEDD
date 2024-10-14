class Desconto:
    def aplicar(self, cliente):
        raise NotImplementedError("Este método deve ser implementado na subclasse.")

class DescontoPercentual(Desconto):
    def __init__(self, percentual):
        self.percentual = percentual

    def aplicar(self, cliente):
        if not cliente.carrinho:
            print("O carrinho está vazio!\n")
            return
        for produto in cliente.carrinho:
            produto.preco -= produto.preco * (self.percentual / 100)
        print(f"Desconto de {self.percentual}% aplicado a todos os produtos no carrinho de {cliente.nome}.\n")