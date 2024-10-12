class SalaryManager:
    def __init__(self, salario_mensal):
        self.salario_mensal = max(salario_mensal, 0.0)  # salário mensal positivo

    def calcular_salario_anual(self):
        return self.salario_mensal * 12

    def dar_aumento(self, porcentagem):
        self.salario_mensal *= (1 + porcentagem / 100)  # método para dar um aumento
