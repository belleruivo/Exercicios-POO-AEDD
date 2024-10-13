# employee.py

class Employee:
    def __init__(self, nome, sobrenome, salario_mensal): 
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_mensal = max(salario_mensal, 0.0)  # salário mensal positivo

    @property
    def nome(self): # getter para o nome
        return self._nome

    @nome.setter
    def nome(self, value): # setter para o nome
        self._nome = value

    @property
    def sobrenome(self): 
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, value): 
        self._sobrenome = value

    @property
    def salario_mensal(self): 
        return self._salario_mensal

    @salario_mensal.setter
    def salario_mensal(self, value): 
        self._salario_mensal = max(value, 0.0) # salário mensal positivo

    def salario_anual(self): # método para calcular o salário anual
        return self._salario_mensal * 12

    def dar_aumento(self, porcentagem): # método para dar um aumento
        self._salario_mensal *= (1 + porcentagem / 100)
