# Crie um vetor que armazene dados de n funcionários de uma empresa. Deverão ser
# considerados os dados: código funcional, nome, salário e data de admissão. Elabore
# um programa que: preencha o vetor com os dados fornecidos pelo usuário e ordene
# de forma crescente os elementos pelo campo de código funcional, usando o
# quickSort.

print("-"*35)
print("           FUNCIONÁRIOS")
print("-"*35)
class Funcionario:
    def __init__(self, codigo, nome, salario, data_admissao):
        self.codigo = codigo
        self.nome = nome
        self.salario = salario
        self.data_admissao = data_admissao

    def __repr__(self):
        return f"FUNCIONÁRIO = codigo: {self.codigo}, nome: '{self.nome}', salario: {self.salario}, data_admissao: '{self.data_admissao}')"

def quicksort(funcionarios):
    if len(funcionarios) <= 1:
        return funcionarios
    else:
        pivo = funcionarios[0].codigo
        menores = [f for f in funcionarios[1:] if f.codigo <= pivo]
        maiores = [f for f in funcionarios[1:] if f.codigo > pivo]
        return quicksort(menores) + [funcionarios[0]] + quicksort(maiores)

def main():
    n = int(input("Digite o número de funcionários: "))
    funcionarios = []

    for _ in range(n):
        codigo = int(input("Código funcional: "))
        nome = input("Nome: ")
        salario = float(input("Salário: "))
        data_admissao = input("Data de admissão (DD/MM/AAAA): ")
        funcionarios.append(Funcionario(codigo, nome, salario, data_admissao))

    funcionarios_ordenados = quicksort(funcionarios)

    print("\nFuncionários ordenados pelo código funcional:")
    for f in funcionarios_ordenados:
        print(f)

main()
