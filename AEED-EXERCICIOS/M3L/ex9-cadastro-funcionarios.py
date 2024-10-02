'''9. Faça um programa que cadastre o nome e o salário de n funcionários. Usando um
método de ordenação diferente para cada item a seguir, liste todos os dados dos
funcionários das seguintes formas:
a. Em ordem crescente de salário;
b. Em ordem decrescente de salário;
c. Em ordem alfabética.'''

def main():
    funcionarios = []

    n = int(input("Insira o número de funcionários: "))
    for c in range(n):
        nome = input("Insira o nome do funcionário: ")
        salario = input("Insira o salário do funcionário: ")
        funcionarios.append({"nome": nome, "salario": salario})

