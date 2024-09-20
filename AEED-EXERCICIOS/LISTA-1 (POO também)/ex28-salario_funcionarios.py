'''
28. Em uma loja de eletrodomésticos, os funcionários da seção de TVs recebem,
mensalmente um salário fixo mais comissão. Essa comissão é calculada em relação
ao tipo e número de televisores vendidos, de acordo com a tabela abaixo:

Tipo Quantidade vendida Comissões
8 K 10 ou mais R$ 550 por TV vendida
Menos que 10 R$ 350 por TV vendida
4 K 10 ou mais R$ 420 por TV vendida
Menos que 10 R$ 250 por TV vendida

Sabe-se ainda, que ele tem um desconto de 8% do salário total para pagamento do
INSS e se o seu salário total for superior a R$ 950,00 ele ainda tem um desconto de 5% do salário para fins de imposto de renda. Faça um programa que leia os dados de
vários funcionários e, para cada funcionário, calcule e imprima o salário líquido (já
com os descontos). Além disso, no final, o programa deve:
a. Imprimir o número de funcionários.
b. Imprimir o total de salários pagos.
c. Imprimir a média das comissões.
d. Imprimir o valor da maior e da menor comissão paga pelo departamento.
'''

def calcular_comissao(tipo_tv, quantidade_vendida):
    if tipo_tv == '8K':
        if quantidade_vendida >= 10:
            return 550 * quantidade_vendida
        else:
            return 350 * quantidade_vendida
    elif tipo_tv == '4K':
        if quantidade_vendida >= 10:
            return 420 * quantidade_vendida
        else:
            return 250 * quantidade_vendida
    else:
        raise ValueError("Tipo de TV inválido")

def calcular_salario_liquido(salario_fixo, comissao):
    salario_bruto = salario_fixo + comissao
    desconto_inss = salario_bruto * 0.08
    salario_apos_inss = salario_bruto - desconto_inss
    if salario_apos_inss > 950:
        desconto_ir = salario_apos_inss * 0.05
    else:
        desconto_ir = 0
    salario_liquido = salario_apos_inss - desconto_ir
    return salario_liquido

def ler_dados_funcionarios():
    funcionarios = []
    while True:
        try:
            nome = input("Nome do funcionário (ou 'sair' para terminar): ").strip()
            if nome.lower() == 'sair':
                break
            if not nome:
                raise ValueError("O nome do funcionário não pode ser vazio.")
            if any(char.isdigit() for char in nome):
                raise ValueError("O nome do funcionário não pode conter números.")
            
            while True:
                try:
                    salario_fixo = input("Salário fixo: ").strip()
                    if not salario_fixo:
                        raise ValueError("O salário fixo não pode ser vazio.")
                    if not salario_fixo.replace('.', '', 1).isdigit():
                        raise ValueError("O salário fixo deve ser um número válido.")
                    salario_fixo = float(salario_fixo)
                    if salario_fixo <= 0:
                        raise ValueError("O salário fixo deve ser um número positivo.")
                    break
                except ValueError as e:
                    print(f"Erro de entrada: {e}")
            
            while True:
                try:
                    tipo_tv = input("Tipo de TV vendida (8K/4K): ").strip().upper()
                    if not tipo_tv:
                        raise ValueError("O tipo de TV não pode ser vazio.")
                    if tipo_tv not in ['8K', '4K']:
                        raise ValueError("Tipo de TV inválido. Deve ser '8K' ou '4K'.")
                    break
                except ValueError as e:
                    print(f"Erro de entrada: {e}")
            
            while True:
                try:
                    quantidade_vendida = input("Quantidade de TVs vendidas: ").strip()
                    if not quantidade_vendida:
                        raise ValueError("A quantidade de TVs vendidas não pode ser vazia.")
                    if not quantidade_vendida.isdigit():
                        raise ValueError("A quantidade de TVs vendidas deve ser um número inteiro válido.")
                    quantidade_vendida = int(quantidade_vendida)
                    if quantidade_vendida <= 0:
                        raise ValueError("A quantidade de TVs vendidas deve ser um número inteiro positivo.")
                    break
                except ValueError as e:
                    print(f"Erro de entrada: {e}")
            
            comissao = calcular_comissao(tipo_tv, quantidade_vendida)
            salario_liquido = calcular_salario_liquido(salario_fixo, comissao)
            
            funcionarios.append({
                'nome': nome,
                'salario_fixo': salario_fixo,
                'tipo_tv': tipo_tv,
                'quantidade_vendida': quantidade_vendida,
                'comissao': comissao,
                'salario_liquido': salario_liquido
            })
        except ValueError as e:
            print(f"Erro de entrada: {e}")
    return funcionarios

def imprimir_relatorio(funcionarios):
    total_funcionarios = len(funcionarios)
    total_salarios = sum(f['salario_liquido'] for f in funcionarios)
    total_comissoes = sum(f['comissao'] for f in funcionarios)
    media_comissoes = total_comissoes / total_funcionarios if total_funcionarios > 0 else 0
    maior_comissao = max(f['comissao'] for f in funcionarios) if total_funcionarios > 0 else 0
    menor_comissao = min(f['comissao'] for f in funcionarios) if total_funcionarios > 0 else 0

    print(f"Total de funcionários: {total_funcionarios}")
    print(f"Total de salários pagos: R$ {total_salarios:.2f}")
    print(f"Média das comissões: R$ {media_comissoes:.2f}")
    print(f"Maior comissão paga: R$ {maior_comissao:.2f}")
    print(f"Menor comissão paga: R$ {menor_comissao:.2f}")

def main():
    funcionarios = ler_dados_funcionarios()
    imprimir_relatorio(funcionarios)

if __name__ == "__main__":
    main()