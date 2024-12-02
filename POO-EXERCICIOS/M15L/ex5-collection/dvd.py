from collection import Collection

class DVD(Collection):
    def __init__(self, titulo, ano, duracao, diretor):
        super().__init__(titulo, ano)
        self.duracao = duracao
        self.diretor = diretor
        self.is_borrowed = False

    def descricao(self):
        return f"DVD: {self.titulo}, Diretor: {self.diretor}, Duração: {self.duracao} min, Ano: {self.ano}"