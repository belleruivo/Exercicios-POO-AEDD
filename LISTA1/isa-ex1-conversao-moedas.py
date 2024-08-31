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
    '''Função que converte a string de entrada para float'''
    input_str = input_str.replace('.', '')  # remove separador de milhares
    input_str = input_str.replace(',', '.')  # substitui separador decimal por ponto
    try:
        return float(input_str)
    except ValueError:
        return None

def main():
    while True: # laço de repetição para o menu
        menu()

        try:
            opcao = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("\nOpção inválida. Por favor, digite um número presente no menu!")
            continue

        if opcao == 1:
            print("\n--> Conversão de Dólar Americano para Real")
            custo = input("Digite o valor em Dólares Americanos: ")
            custo = process_input(custo)
            if custo is not None:
                print(f"\nO valor da transação é: R$ {custo * 3.258:.2f} Reais")
            else:
                print("\nValor inválido. Por favor, digite um número válido.")
        elif opcao == 2:
            print("\n--> Conversão de Euro para Real")
            custo = input("Digite o valor em Euros: ")
            custo = process_input(custo)
            if custo is not None:
                print(f"\nO valor da transação é: R$ {custo * 4.095:.2f} Reais")
            else:
                print("\nValor inválido. Por favor, digite um número válido.")
        elif opcao == 3:
            print("\n--> Conversão de Libra Esterlina para Real")
            custo = input("Digite o valor em Libras Esterlinas: ")
            custo = process_input(custo)
            if custo is not None:
                print(f"\nO valor da transação é: R$ {custo * 4.529:.2f} Reais")
            else:
                print("\nValor inválido. Por favor, digite um número válido.")
        elif opcao == 4:
            print("\n--> Conversão de Yuan para Real")
            custo = input("Digite o valor em Yuan: ")
            custo = process_input(custo)
            if custo is not None:
                print(f"\nO valor da transação é: R$ {custo * 0.515:.2f} Reais")
            else:
                print("\nValor inválido. Por favor, digite um número válido.")
        elif opcao == 5:
            print("\nPrograma encerrado.")
            break  # fecha o loop e termina o programa
        else:
            print("\nOpção inválida. Tente novamente.")

main()