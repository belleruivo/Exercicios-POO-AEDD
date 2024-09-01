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
def aum_uniforme(salarios):
    sala_uniforme = []

    for c in salarios:
        nov_sal = c*1.1 
        sala_uniforme.append(nov_sal)

    return sum(sala_uniforme)

def aum_progressivo(salarios):
    sala_progressivo = []

    for c in salarios:
        if c <= 1000:
            nov_sal = c*1.15
        elif c <= 2000 and c > 1000:
            nov_sal = c*1.10
        else:
            nov_sal = c*1.05
        sala_progressivo.append(nov_sal)

    return sum(sala_progressivo)


def main():
    
    print("-="*20, "CÁLCULO DE AUMENTOS", "-="*20,"\n")
    print("Digite os salários dos seus funcionários e insira o número (0) caso queira finalizar o programa")
    salarios = []
    while True:
        valor = float(input("Digite o salário: "))
        if valor == 0:
            break
        salarios.append(valor)
    

    print(f"\nTotal de funcionários: {len(salarios)}")
    print(f"Salário médio dos funcionários: {sum(salarios)/len(salarios):.2f}")
    print(f"Total da folha de pagamento atual: {sum(salarios):.2f}")
    print(f"Total da folha de pagamento com um aumento uniforme: {aum_uniforme(salarios):.2f}")
    print(f"Total da folha de pagamento com um aumento progressivo: {aum_progressivo(salarios):.2f}")

    if aum_uniforme(salarios) > aum_progressivo(salarios):
        print("\nDesssa forma, o aumento progressivo é mais econômico para a empresa")
    elif aum_uniforme(salarios) == aum_progressivo(salarios):
        print("\nDesssa forma, os dois aumentos geram o mesmo gasto para a empresa")
    else:
        print("\nDesssa forma, o aumento uniforme é mais econômico para a empresa")

main()  