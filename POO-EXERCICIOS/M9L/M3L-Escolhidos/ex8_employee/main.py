# main.py

from employee import Employee  # Importa a classe Employee do arquivo employee.py

def main():
    nome = input("Digite o nome do funcionário: ")
    sobrenome = input("Digite o sobrenome do funcionário: ")
    salario_mensal = float(input("Digite o salário mensal do funcionário: "))

    emp1 = Employee(nome, sobrenome, salario_mensal)

    print(f"Salário anual de {emp1.nome} {emp1.sobrenome}: R${emp1.salario_anual():.2f}")

    # Aumento de 10%
    emp1.dar_aumento(10)

    print(f"Novo salário anual de {emp1.nome} {emp1.sobrenome}: R${emp1.salario_anual():.2f}")

if __name__ == "__main__":
    main()
