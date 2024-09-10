''' 
1. Elabore um programa que:
• Mostre um menu de opções de conversão entre moedas 
(1 – dólar americano, 2 – euro, 3 – libra esterlina e 4 – yuan;
• Leia a escolha do usuário;
• Leia o custo em R$ (reais) da operação;
• Imprima o valor da transação na moeda escolhida, de acordo com os fatores
de conversão da tabela abaixo.

Moeda Valor         (R$)
Dólar americano     3,258
Euro                4,095
Libra esterlina     4,529
Yuan                0,515
'''
print("-"*65)
print("Olá, seja bem-vindo(a) ao programa que converte moedas para real!\nPara começar, digite o número equivalente à moeda que deseja converter:")
print("-"*65)

taxas = { #dicionário global com as taxas
    1: 3.258,  # dólar Americano
    2: 4.095,  # euro
    3: 4.529,  # libra esterlina
    4: 0.515   # yuan
}

def menu():
    print("\nMenu de Opções:")
    print("="*20)
    print("1 - Dólar Americano")
    print("2 - Euro")
    print("3 - Libra Esterlina")
    print("4 - Yuan")
    print("5 - Sair")
    print("="*20)

def process_input(input_str):
    # verifica se o valor é válido: apenas números ou números com até duas casas decimais
    try:
        # verifica se há no máximo um ponto e se segue o formato correto
        if input_str.count('.') <= 1:
            return float(input_str)  # converte a string diretamente para float
        else:
            return None
    except ValueError:
        return None

def main():
    while True: # laço de repetição para o menu
        menu()

        try:
            opcao = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("\nOpção inválida. Por favor, digite um número presente no menu! ")
            continue # loop começa de novo, pedindo pro usuário inserir a opção desejada

        if opcao == 5:
            print("\nPrograma encerrado.")
            break  # fecha o loop e termina o programa
        
        taxa = taxas.get(opcao)
        if taxa is None:
            print("Opção inválida. Tente novamente.")
            continue # loop começa de novo, pedindo pro usuário inserir a opção desejada
         
        while True:
            print("\nPor favor, insira o valor no formato '5000' ou '5000.00' para centavos.")
            print("Não use separadores de milhar como '1.000' ou '1.000,00'.")
            custo = input("\nDigite o valor na moeda selecionada: ")
            custo = process_input(custo)
            if custo is not None:
                valor_em_reais = custo * taxa
                print(f"\nO valor da transação é: R$ {valor_em_reais:.2f} Reais")
                break  # sai do loop após a conversão bem-sucedida
            else:
                print("\nValor inválido. Por favor, digite um número válido.")
main()      