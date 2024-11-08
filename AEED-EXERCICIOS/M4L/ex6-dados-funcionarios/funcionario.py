class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome  # Nome do funcionário
        self.salario = salario  # Salário do funcionário
        self.next = None  # Próximo nó (inicialmente None)