class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.veiculos = [] 

    def adicionar_veiculo(self, veiculo):
        if veiculo not in self.veiculos:
            self.veiculos.append(veiculo)

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"
