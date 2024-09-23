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


def coletar_salarios():
    salarios = []
    print("Digite os salários dos seus funcionários e insira o número (0) caso queira finalizar o programa")
    
    while True:
        try:
            valor = float(input("Digite o salário: "))
            if valor < 0:
                print("Por favor, insira um salário válido!\n")
            elif valor == 0:
                break
            else:
                salarios.append(valor)
        except ValueError:
            print("Por favor, insira um valor numérico válido.\n")

    return salarios

def calcular_estatisticas(salarios):
    if not salarios:
        return None, None, None
    
    total_salarios = sum(salarios)
    media_salarios = total_salarios / len(salarios)
    
    return total_salarios, media_salarios, len(salarios)

def exibir_resultados(salarios):
    total_uniforme = aum_uniforme(salarios)
    total_progressivo = aum_progressivo(salarios)
    total_salarios, media_salarios, num_funcionarios = calcular_estatisticas(salarios)

    if num_funcionarios is None:
        print("Nenhum salário foi inserido. Programa finalizado.")
        return

    print(f"\nTotal de funcionários: {num_funcionarios}")
    print(f"Salário médio dos funcionários: {media_salarios:.2f}")
    print(f"Total da folha de pagamento atual: {total_salarios:.2f}")
    print(f"Total da folha de pagamento com um aumento uniforme: {total_uniforme:.2f}")
    print(f"Total da folha de pagamento com um aumento progressivo: {total_progressivo:.2f}")

    comparar_aumentos(total_uniforme, total_progressivo)

def comparar_aumentos(total_uniforme, total_progressivo):
    if total_uniforme > total_progressivo:
        print("\nO aumento progressivo é mais econômico para a empresa.")
    elif total_uniforme == total_progressivo:
        print("\nOs dois aumentos geram o mesmo gasto para a empresa.")
    else:
        print("\nO aumento uniforme é mais econômico para a empresa.")

def main():
    print("-="*20, "CÁLCULO DE AUMENTOS", "-="*20, "\n")
    salarios = coletar_salarios()
    exibir_resultados(salarios)
    print("-="*51)
main()