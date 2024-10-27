class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.proximo = None
        self.anterior = None