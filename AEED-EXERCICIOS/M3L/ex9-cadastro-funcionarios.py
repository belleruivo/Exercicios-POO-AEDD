'''9. Faça um programa que cadastre o nome e o salário de n funcionários. Usando um
método de ordenação diferente para cada item a seguir, liste todos os dados dos
funcionários das seguintes formas:
a. Em ordem crescente de salário;
b. Em ordem decrescente de salário;
c. Em ordem alfabética.'''

def ordenar_salario_crescente(funcionarios):
    return sorted(funcionarios, key=lambda x: x['salario'])

def ordenar_salario_decrescente(funcionarios):
    return sorted(funcionarios, key=lambda x: x['salario'], reverse=True)

def ordenar_nome_alfabetica(funcionarios):
    return sorted(funcionarios, key=lambda x: x['nome'].lower())

def cadastrar_funcionarios(n):
    funcionarios = []
    for i in range(n):
        nome = input(f"\nDigite o nome do funcionário {i + 1}: ")
        salario = float(input(f"Digite o salário do funcionário {i + 1}: "))
        funcionarios.append({'nome': nome, 'salario': salario})
    return funcionarios

def exibir_funcionarios(titulo, funcionarios):
    print(f"\n{titulo}:")
    for func in funcionarios:
        print(f"Nome: {func['nome']}, Salário: {func['salario']}")


def main():
    n = int(input("Quantos funcionários deseja cadastrar? "))
    funcionarios = cadastrar_funcionarios(n)
    
    exibir_funcionarios("Funcionários em ordem crescente de salário", ordenar_salario_crescente(funcionarios))

    exibir_funcionarios("Funcionários em ordem decrescente de salário", ordenar_salario_decrescente(funcionarios))
    
    exibir_funcionarios("Funcionários em ordem alfabética", ordenar_nome_alfabetica(funcionarios))

main()
