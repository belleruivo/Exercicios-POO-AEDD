'''9. Faça um programa que cadastre o nome e o salário de n funcionários em uma lista
duplamente encadeada e ordenada pelo salário de forma crescente. A seguir, o
programa deve mostrar o nome, o valor do imposto e o valor a receber, ou seja, o
salário menos o imposto de todos os funcionários cadastrados. Posteriormente, o
programa deve mostrar os nomes e os salários dos funcionários cujos nomes
comecem por uma letra digitada pelo usuário (considera a possibilidade de letras
maiúsculas e minúsculas). Se nenhum funcionário tem o nome começado com a letra
digitada pelo usuário, mostrar mensagem. Finalmente, o programa deve apresentar
duas listagens:

    a. Dos nomes e salários dos funcionários por ordem crescente de salário;
    b. Dos nomes e salários dos funcionários por ordem decrescente de salário.

Observação: os percentuais de imposto seguem a tabela abaixo:

    Valor do salário        Percentual do imposto
        Até 850                     Isento
    Entre 850 e 1200            10% do salário
    De 1200 para cima           20% do salário
'''
from listaDuplamenteEncadeada import ListaDuplamenteEncadeada
from funcionario import Funcionario

def main():
    lista_funcionarios = ListaDuplamenteEncadeada()
    print("-="*30)
    while True:
            try:
                n = int(input("Digite o número de funcionários a cadastrar: "))
                if n < 0:
                    print("O valor não pode ser negativo.")
                break
            except ValueError:
                print(f"Entrada inválida. Certifique-se de inserir um número inteiro\n")

    for i in range(n):
        while True:
            nome = input(f"\nDigite o nome do {i+1}º funcionário: ")
            if nome.isalpha():  
                break
            else:
                print("O nome deve conter apenas letras. Tente novamente.")
        while True:
            try:
                salario = float(input("Digite o salário do funcionário: ").replace(',', '.'))
                if salario < 0:
                    print("O valor não pode ser negativo.")
                break
            except ValueError:
                print(f"Entrada inválida. Certifique-se de inserir um número válido")

        funcionario = Funcionario(nome, salario)
        lista_funcionarios.inserir_ordenado(funcionario)

    print("\nInformações dos funcionários:")
    for nome, imposto, valor_a_receber in lista_funcionarios.calcular_imposto():
        print(f"Nome: {nome}, Imposto: R${imposto:.2f}, Valor a Receber: R${valor_a_receber:.2f}")

    while True:
            letra = input("\nDigite uma letra para filtrar funcionários: ")
            if letra.isalpha():  
                break
            else:
                print("O nome deve conter apenas letras. Tente novamente.")

    funcionarios_filtrados = lista_funcionarios.listar_por_letra(letra)
    if funcionarios_filtrados:
        print("\nFuncionários cujos nomes começam com a letra:", letra)
        for nome, salario in funcionarios_filtrados:
            print(f"Nome: {nome}, Salário: R${salario:.2f}")
    else:
        print("Nenhum funcionário encontrado com essa letra.")

    print("\nFuncionários por ordem crescente de salário:")
    for nome, salario in lista_funcionarios.listar_funcionarios(ordem='crescente'):
        print(f"Nome: {nome}, Salário: R${salario:.2f}")

    print("\nFuncionários por ordem decrescente de salário:")
    for nome, salario in lista_funcionarios.listar_funcionarios(ordem='decrescente'):
        print(f"Nome: {nome}, Salário: R${salario:.2f}")
    print("-="*30)

main()