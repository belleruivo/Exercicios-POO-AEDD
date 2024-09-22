'''
8. Crie uma classe chamada Employee que inclui três variáveis de instância: um nome
(string), um sobrenome (string) e um salário mensal (float). Sua classe deve ter um
construtor que inicializa as três variáveis. Forneça um método get e set para cada
variável. Se o salário mensal fornecido pelo usuário não for positivo, configure-o
como 0.0. Teste a classe implementada e seus métodos. Crie dois objetos Employee e
exiba o salário anual de cada objeto. Depois, dê 10% de aumento para cada
empregado e exiba novamente os salários.
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

def main():
    # dois objetos employee
    emp1 = Employee("Murilo", "Dantas", 3000.0)
    emp2 = Employee("Pedro", "Henrique", 2500.0)

    # salário anual de cada objeto
    print(f"Salário anual de {emp1.nome} {emp1.sobrenome}: R${emp1.salario_anual():.2f}")
    print(f"Salário anual de {emp2.nome} {emp2.sobrenome}: R${emp2.salario_anual():.2f}")

    # 10% de aumento para cada
    emp1.dar_aumento(10)
    emp2.dar_aumento(10)

    # salários anuais após o aumento
    print(f"Novo salário anual de {emp1.nome} {emp1.sobrenome}: R${emp1.salario_anual():.2f}")
    print(f"Novo salário anual de {emp2.nome} {emp2.sobrenome}: R${emp2.salario_anual():.2f}")

if __name__ == "__main__":
    main()  