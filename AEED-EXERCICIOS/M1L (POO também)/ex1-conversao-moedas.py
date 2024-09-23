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

# Constantes para as taxas de conversão
TAXAS = {
    1: 3.258,  # Dólar Americano
    2: 4.095,  # Euro
    3: 4.529,  # Libra Esterlina
    4: 0.515   # Yuan
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
        if input_str.count('.') <= 1 and ',' not in input_str and '.' not in input_str[:-3]:
            return float(input_str)  # converte a string diretamente para float
        else:
            return None
    except ValueError:
        return None

def get_opcao():
    while True:
        try:
            opcao = int(input("\nDigite a opção desejada: "))
            return opcao
        except ValueError:
            print("\nOpção inválida. Por favor, digite um número presente no menu!")

def get_valor():
    while True:
        print("\nPor favor, insira o valor no formato '5000' ou '5000.00' para centavos.")
        print("Não use separadores de milhar como '1.000' ou '1.000,00'.")
        custo = input("Digite o valor na moeda selecionada: ")
        custo = process_input(custo)
        if custo is not None:
            return custo
        else:
            print("\nValor inválido. Por favor, digite um número válido.")

def main():
    print("-"*65)
    print("Olá, seja bem-vindo(a) ao programa que converte moedas para real!\nPara começar, digite o número equivalente à moeda que deseja converter:")
    print("-"*65)

    while True: # laço de repetição para o menu
        menu()

        opcao = get_opcao()

        if opcao == 5:
            print("\nPrograma encerrado.")
            break  # fecha o loop e termina o programa
        
        taxa = TAXAS.get(opcao)
        if taxa is None:
            print("Opção inválida. Tente novamente.")
            continue # loop começa de novo, pedindo pro usuário inserir a opção desejada
         
        custo = get_valor()
        valor_em_reais = custo * taxa
        print(f"\nO valor da transação é: R$ {valor_em_reais:.2f} Reais")

if __name__ == "__main__":
    main()