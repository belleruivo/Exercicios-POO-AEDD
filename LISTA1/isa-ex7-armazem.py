''' 
7. Para fazer o balanço mensal de um armazém, faça um programa que leia para um
número qualquer de mercadorias diferentes o preço de custo, o preço de venda e a
quantidade vendida. A partir desses dados imprima: o número total de mercadorias
diferentes lidas, o faturamento total e o lucro total do armazém. 
'''

print("------------------------------------------------------------------------------------------------")
print("Olá, seja bem-vindo(a)! Seja bem vindo ao programa que calcula o balanço mensal!")
print("------------------------------------------------------------------------------------------------")

total_faturamento = 0
total_lucro = 0
numero_mercadorias = 0

while True:
    try:
        preco_custo = float(input("Digite o preço de custo da mercadoria (ou 0 para encerrar): "))
        if preco_custo == 0:
            break
        
        preco_venda = float(input("Digite o preço de venda da mercadoria: "))
        quantidade_vendida = int(input("Digite a quantidade vendida da mercadoria: "))
        
        if preco_custo < 0 or preco_venda < 0 or quantidade_vendida < 0:
            print("Os valores devem ser positivos. Por favor, insira valores válidos.")
            continue
        
        faturamento = preco_venda * quantidade_vendida
        lucro = (preco_venda - preco_custo) * quantidade_vendida
        
        total_faturamento += faturamento
        total_lucro += lucro
        numero_mercadorias += 1
    
    except ValueError:
        print("Entrada inválida. Por favor, insira valores numéricos válidos.")
        
print("\nRelatório do Balanço Mensal:")
print(f"Número total de mercadorias diferentes lidas: {numero_mercadorias}")
print(f"Faturamento total: R$ {total_faturamento:.2f}")
print(f"Lucro total: R$ {total_lucro:.2f}")