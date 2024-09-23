'''
22. Calcule e mostre o imposto de renda de um grupo de contribuintes considerando que
os dados de cada contribuinte (número do CPF, número de dependentes e renda
mensal) são valores fornecidos pelo usuário. Para cada contribuinte será feito um
desconto no imposto de 5% do salário mínimo (R$136,00) para cada dependente (o
salário mínimo e o desconto são designados por constantes simbólicas). Os valores
da alíquota para cálculo do imposto são:

Renda Líquida (R$) Alíquota
até 900,00 isento
900,01 até 1500,00 5%
1500,01 até 1900,00 10%
1900,01 até 2200,00 15%
acima de 2200,01 20%

O último valor, que não será considerado, terá o número do CPF igual a zero. Ao final,
devem ser impressos:
a. Para cada contribuinte, o total a pagar.
b. O número de contribuintes.

10

c. O total de contribuintes isentos e não isentos.
d. O total de impostos que serão arrecadados desse grupo de contribuintes.
e. O número do CPF e o valor da contribuição daquele contribuinte que for pagar
o maior imposto.
'''

SALARIO_MINIMO = 136.00
DESCONTO_DEPENDENTE = 0.05 * SALARIO_MINIMO

def formatar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) > 11:
        cpf = cpf[:11]
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def obter_dados_contribuinte():
    while True:
        try:
            cpf = input("Digite o CPF (0 para terminar): ").replace(".", "").replace("-", "")
            if cpf == "0":
                return None
            if len(cpf) != 11:
                print("CPF inválido. O CPF deve ter exatamente 11 dígitos.")
                continue
            cpf_formatado = formatar_cpf(cpf)
            dependentes = int(input("Digite o número de dependentes: "))
            if dependentes < 0:
                print("Número de dependentes inválido. Deve ser um número não negativo.")
                continue
            renda_mensal = float(input("Digite a renda mensal: "))
            if renda_mensal < 0:
                print("Renda mensal inválida. Deve ser um valor não negativo.")
                continue
            return cpf_formatado, dependentes, renda_mensal
        except ValueError:
            print("Entrada inválida. Por favor, insira os dados corretamente.")

def calcular_imposto(renda_liquida):
    if renda_liquida <= 900.00:
        return 0.00
    elif renda_liquida <= 1500.00:
        return 0.05 * renda_liquida
    elif renda_liquida <= 1900.00:
        return 0.10 * renda_liquida
    elif renda_liquida <= 2200.00:
        return 0.15 * renda_liquida
    else:
        return 0.20 * renda_liquida

def processar_contribuinte(cpf, dependentes, renda_mensal):
    desconto = dependentes * DESCONTO_DEPENDENTE
    renda_liquida = renda_mensal - desconto
    imposto = calcular_imposto(renda_liquida)
    return imposto

def processar_contribuintes():
    contribuintes = []
    total_impostos = 0.0
    total_isentos = 0
    total_nao_isentos = 0
    maior_imposto = 0.0
    cpf_maior_imposto = None

    while True:
        dados = obter_dados_contribuinte()
        if dados is None:
            break

        cpf, dependentes, renda_mensal = dados
        imposto = processar_contribuinte(cpf, dependentes, renda_mensal)

        contribuintes.append((cpf, imposto))
        total_impostos += imposto

        if imposto == 0.0:
            total_isentos += 1
        else:
            total_nao_isentos += 1

        if imposto > maior_imposto:
            maior_imposto = imposto
            cpf_maior_imposto = cpf

    return contribuintes, total_impostos, total_isentos, total_nao_isentos, cpf_maior_imposto, maior_imposto

def imprimir_resultados(contribuintes, total_impostos, total_isentos, total_nao_isentos, cpf_maior_imposto, maior_imposto):
    print("\nResultados:")
    for cpf, imposto in contribuintes:
        print(f"CPF: {cpf}, Total a pagar: R${imposto:.2f}")
    print(f"Total de contribuintes: {len(contribuintes)}")
    print(f"Total de contribuintes isentos: {total_isentos}")
    print(f"Total de contribuintes não isentos: {total_nao_isentos}")
    print(f"Total de impostos arrecadados: R${total_impostos:.2f}")
    if cpf_maior_imposto is not None:
        print(f"CPF do contribuinte que pagou o maior imposto: {cpf_maior_imposto}")
        print(f"Maior valor de imposto pago: R${maior_imposto:.2f}")

def main():
    contribuintes, total_impostos, total_isentos, total_nao_isentos, cpf_maior_imposto, maior_imposto = processar_contribuintes()
    imprimir_resultados(contribuintes, total_impostos, total_isentos, total_nao_isentos, cpf_maior_imposto, maior_imposto)

if __name__ == "__main__":
    main()