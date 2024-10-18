# main.py
from extended_employee import ExtendedEmployee

def main():
    # Criando dois objetos Employee
    emp1 = ExtendedEmployee("Murilo", "Dantas", 3000.0, "TI")
    emp2 = ExtendedEmployee("Pedro", "Henrique", 2500.0, "RH")

    # Exibindo o salário anual de cada funcionário
    print(f"Salário anual de {emp1.nome} {emp1.sobrenome} ({emp1.departamento}): R${emp1.salario_anual():.2f}")
    print(f"Salário anual de {emp2.nome} {emp2.sobrenome} ({emp2.departamento}): R${emp2.salario_anual():.2f}")

    # Aplicando um aumento de 10% para cada funcionário
    emp1.dar_aumento(10)
    emp2.dar_aumento(10)

    # Exibindo os salários anuais após o aumento
    print(f"Novo salário anual de {emp1.nome} {emp1.sobrenome} ({emp1.departamento}): R${emp1.salario_anual():.2f}")
    print(f"Novo salário anual de {emp2.nome} {emp2.sobrenome} ({emp2.departamento}): R${emp2.salario_anual():.2f}")

if __name__ == "__main__":
    main()
