'''Refazer a Lista M3L, aplicando o Princípio da Responsabilidade Única e mostrar as
diferenças de seu código, antes e depois.'''

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

class EmployeeDisplay:
    def display_salario_anual(self, employee):
        print(f"Salário anual de {employee.nome} {employee.sobrenome}: R${employee.salario_anual():.2f}")

    def display_novo_salario_anual(self, employee):
        print(f"Novo salário anual de {employee.nome} {employee.sobrenome}: R${employee.salario_anual():.2f}")

def main():
    # dois objetos employee
    emp1 = Employee("Murilo", "Dantas", 3000.0)
    emp2 = Employee("Pedro", "Henrique", 2500.0)

    display = EmployeeDisplay()

    # salário anual de cada objeto
    display.display_salario_anual(emp1)
    display.display_salario_anual(emp2)

    # 10% de aumento para cada
    emp1.dar_aumento(10)
    emp2.dar_aumento(10)

    # salários anuais após o aumento
    display.display_novo_salario_anual(emp1)
    display.display_novo_salario_anual(emp2)

if __name__ == "__main__":
    main()