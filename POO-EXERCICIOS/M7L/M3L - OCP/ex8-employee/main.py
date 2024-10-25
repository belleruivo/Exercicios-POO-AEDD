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

# Análise do Código
# Classe Base Employee:

# A classe Employee contém as propriedades e métodos básicos para um funcionário, como nome, sobrenome, salario_mensal, salario_anual() e dar_aumento().
# Essa classe pode ser estendida para adicionar novos comportamentos ou características sem alterar seu código original.
# Classe Derivada ExtendedEmployee:

# A classe ExtendedEmployee herda de Employee e adiciona um novo atributo departamento, junto com suas propriedades e métodos correspondentes.
# Isso permite que você crie novos tipos de funcionários (com atributos adicionais) sem modificar a classe Employee.
# Extensibilidade:

# Se um novo tipo de funcionário precisar de características adicionais (por exemplo, um funcionário com uma comissão), você pode simplesmente criar outra classe que herde de Employee ou ExtendedEmployee e adicione os novos atributos e métodos necessários.
# O uso de herança permite a criação de novas classes que podem ser adicionadas sem afetar o funcionamento do código existente.