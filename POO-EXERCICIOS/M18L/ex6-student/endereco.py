class Endereco:
    
    def __init__(self, rua, numero, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def get_endereco_completo(self):
        return f'{self.rua}, {self.numero}, {self.cidade} - {self.estado}, CEP: {self.cep}'
