''' 
7. Para fazer o balanço mensal de um armazém, faça um programa que leia para um
número qualquer de mercadorias diferentes o preço de custo, o preço de venda e a
quantidade vendida. A partir desses dados imprima: o número total de mercadorias
diferentes lidas, o faturamento total e o lucro total do armazém. 
'''

print("------------------------------------------------------------------------------------------------")
print("Olá, seja bem-vindo(a)! Seja bem vindo ao programa que calcula o balanço mensal!")
print("------------------------------------------------------------------------------------------------")

def ler_dados_mercadoria():
    while True:
        try:
            preco_custo = float(input("Digite o preço de custo da mercadoria (ou 0 para encerrar): "))
            if preco_custo == 0:
                return None
            elif preco_custo < 0:
                print("O preço de custo deve ser positivo. Por favor, insira um valor válido.")
                continue
            
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico válido.")
    
    while True:
        try:
            preco_venda = float(input("Digite o preço de venda da mercadoria: "))
            if preco_venda < 0:
                print("O preço de venda deve ser positivo. Por favor, insira um valor válido.")
                continue
            
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico válido.")
    
    while True:
        try:
            quantidade_vendida = int(input("Digite a quantidade vendida da mercadoria: "))
            if quantidade_vendida < 0:
                print("A quantidade vendida deve ser positiva. Por favor, insira um valor válido.")
                continue
            
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico válido.")
    
    return preco_custo, preco_venda, quantidade_vendida

def calcular_faturamento_e_lucro(preco_custo, preco_venda, quantidade_vendida):
    faturamento = preco_venda * quantidade_vendida
    lucro = (preco_venda - preco_custo) * quantidade_vendida
    return faturamento, lucro

def main():
    total_faturamento = 0
    total_lucro = 0
    numero_mercadorias = 0

    while True:
        dados_mercadoria = ler_dados_mercadoria()
        if dados_mercadoria is None:
            break
        
        preco_custo, preco_venda, quantidade_vendida = dados_mercadoria
        faturamento, lucro = calcular_faturamento_e_lucro(preco_custo, preco_venda, quantidade_vendida)
        
        total_faturamento += faturamento
        total_lucro += lucro
        numero_mercadorias += 1
    
    print("\nRelatório do Balanço Mensal:")
    print(f"Número total de mercadorias diferentes lidas: {numero_mercadorias}")
    print(f"Faturamento total: R$ {total_faturamento:.2f}")
    print(f"Lucro total: R$ {total_lucro:.2f}")

if __name__ == "__main__":
    main()