class Venda:
    def __init__(self, cliente, veiculo):
        self.cliente = cliente  
        self.veiculo = veiculo  

    def registrar_venda(self):
        return f"Venda realizada: {self.cliente.nome} comprou {self.veiculo.marca} de {self.veiculo.ano}."
