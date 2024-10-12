from employee import Employee  # Importa a classe Employee
from salary_manager import SalaryManager  # Importa a classe SalaryManager

def main():
    # Criação de dois objetos SalaryManager
    salary_manager1 = SalaryManager(3000.0)
    salary_manager2 = SalaryManager(2500.0)

    # Criação de dois objetos Employee com injeção de dependência
    emp1 = Employee("Murilo", "Dantas", salary_manager1)
    emp2 = Employee("Pedro", "Henrique", salary_manager2)

    # Salário anual de cada objeto
    print(f"Salário anual de {emp1.nome} {emp1.sobrenome}: R${emp1.salario_anual():.2f}")
    print(f"Salário anual de {emp2.nome} {emp2.sobrenome}: R${emp2.salario_anual():.2f}")

    # 10% de aumento para cada
    emp1.dar_aumento(10)
    emp2.dar_aumento(10)

    # Salários anuais após o aumento
    print(f"Novo salário anual de {emp1.nome} {emp1.sobrenome}: R${emp1.salario_anual():.2f}")
    print(f"Novo salário anual de {emp2.nome} {emp2.sobrenome}: R${emp2.salario_anual():.2f}")

if __name__ == "__main__":
    main()  # Chama a função main
