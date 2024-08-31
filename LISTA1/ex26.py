''' 26. Uma empresa está fazendo um estudo de possibilidades de aumento aos seus
funcionários e deseja saber se é mais vantajoso dar um aumento uniforme de 10% à
todos os funcionários ou seguir a seguinte tabela progressiva:

    Salário               |    Percentual de aumento
---------------------------------------------------------
    até R$1000,00         |             15%
    até R$2000,00         |             10%
    acima de R$2000,00    |              5%

Faça um programa que leia o salário de um número qualquer de funcionários,
imprimindo para cada um o novo salário nos dois casos (aumento uniforme ou
aumento progressivo). Ao final, o programa deve fornecer:
a. O total de funcionários
b. O salário médio dos funcionários
c. O total da folha de pagamentos atual
d. O total da folha de pagamentos futura nos dois casos estudados, indicando
qual o caminho mais econômico para a empresa.
'''

def main():
    salarios = []
    while True:
        valor = input("Digite o seu salário (ENTER para sair do programa): ")
        if valor == " ":
            break
        salarios.append(valor)
        
        total_funcio += 1

    total_sala = sum(salarios)
    quant_sala = len(salarios)
        
        