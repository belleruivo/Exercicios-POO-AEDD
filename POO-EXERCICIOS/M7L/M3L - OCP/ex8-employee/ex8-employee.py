'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

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

class ExtendedEmployee(Employee):
    def __init__(self, nome, sobrenome, salario_mensal, departamento):
        super().__init__(nome, sobrenome, salario_mensal)
        self.departamento = departamento

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, value):
        self._departamento = value

def main():
    # dois objetos employee
    emp1 = ExtendedEmployee("Murilo", "Dantas", 3000.0, "TI")
    emp2 = ExtendedEmployee("Pedro", "Henrique", 2500.0, "RH")

    # salário anual de cada objeto
    print(f"Salário anual de {emp1.nome} {emp1.sobrenome} ({emp1.departamento}): R${emp1.salario_anual():.2f}")
    print(f"Salário anual de {emp2.nome} {emp2.sobrenome} ({emp2.departamento}): R${emp2.salario_anual():.2f}")

    # 10% de aumento para cada
    emp1.dar_aumento(10)
    emp2.dar_aumento(10)

    # salários anuais após o aumento
    print(f"Novo salário anual de {emp1.nome} {emp1.sobrenome} ({emp1.departamento}): R${emp1.salario_anual():.2f}")
    print(f"Novo salário anual de {emp2.nome} {emp2.sobrenome} ({emp2.departamento}): R${emp2.salario_anual():.2f}")

if __name__ == "__main__":
    main()