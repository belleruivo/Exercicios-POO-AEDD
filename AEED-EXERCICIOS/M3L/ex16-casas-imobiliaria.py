'''
16. Crie um vetor que armazene dados de n casas numa imobiliária. Deverão ser
considerados os dados: código, bairro, tamanho em m2, valor de venda e valor de
aluguel. 

Elabore um programa que: preencha o vetor com os dados fornecidos pelo
usuário e ordene de forma decrescente os elementos pelo campo de venda, usando o
bubbleSort.
'''

# classe que representa uma casa com atributos de código, bairro, tamanho, valor de venda e valor de aluguel
class Casa:
    def __init__(self, codigo, bairro, tamanho, valor_venda, valor_aluguel):
        self.codigo = codigo
        self.bairro = bairro
        self.tamanho = tamanho
        self.valor_venda = valor_venda
        self.valor_aluguel = valor_aluguel

    # método especial para representar a casa como uma string de forma clara e organizada
    def __repr__(self):
        return (f"Casa(codigo={self.codigo}, bairro='{self.bairro}', tamanho={self.tamanho}m², "
                f"valor_venda={self.valor_venda}, valor_aluguel={self.valor_aluguel})")

# função que implementa o algoritmo bubble sort para ordenar as casas em ordem decrescente pelo valor de venda
def bubble_sort_decrescente(casas):
    # obtém o número total de casas no vetor
    n = len(casas)
    # loop externo que percorre cada elemento do vetor
    for i in range(n):
        # loop interno para comparar e trocar elementos adjacentes, se necessário
        for j in range(0, n-i-1):
            # se o valor de venda da casa atual for menor que o da próxima, realiza a troca
            if casas[j].valor_venda < casas[j+1].valor_venda:
                casas[j], casas[j+1] = casas[j+1], casas[j]  # troca as casas de posição
    # retorna o vetor de casas ordenado
    return casas

def main():
    casas = []  # lista para armazenar os dados das casas
    codigos_existentes = set()  # conjunto para garantir que os códigos das casas sejam únicos
    
    # loop para garantir que o usuário forneça um número válido de casas para cadastrar
    while True:
        try:
            n = int(input("Quantas casas deseja cadastrar? "))
            if n <= 0:  # verifica se o número é maior que zero
                raise ValueError("O número de casas deve ser maior que zero.")
            break  # sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro maior que zero.")

    # loop para coletar os dados de cada casa
    for _ in range(n):
        while True:
            try:
                # coleta o código da casa e verifica se é único e numérico
                codigo = input("Digite o código da casa (número inteiro): ").strip()
                if not codigo.isdigit():
                    raise ValueError("O código deve ser um número inteiro.")
                if codigo in codigos_existentes:
                    raise ValueError("Código já cadastrado. Digite um código único.")
                
                # coleta o bairro e verifica se não está vazio
                bairro = input("Digite o bairro da casa: ").strip()
                if not bairro:
                    raise ValueError("O bairro não pode ser vazio.")
                
                # coleta o tamanho da casa e verifica se é um número válido
                tamanho = input("Digite o tamanho da casa em m²: ").strip()
                if not tamanho:
                    raise ValueError("O tamanho não pode ser vazio.")
                try:
                    tamanho = float(tamanho)
                except ValueError:
                    raise ValueError("O tamanho deve ser um número válido.")
                
                # coleta o valor de venda e verifica se é um número válido
                valor_venda = input("Digite o valor de venda da casa: ").strip()
                if not valor_venda:
                    raise ValueError("O valor de venda não pode ser vazio.")
                try:
                    valor_venda = float(valor_venda)
                except ValueError:
                    raise ValueError("O valor de venda deve ser um número válido.")
                
                # coleta o valor de aluguel e verifica se é um número válido
                valor_aluguel = input("Digite o valor de aluguel da casa: ").strip()
                if not valor_aluguel:
                    raise ValueError("O valor de aluguel não pode ser vazio.")
                try:
                    valor_aluguel = float(valor_aluguel)
                except ValueError:
                    raise ValueError("O valor de aluguel deve ser um número válido.")
                
                # adiciona a casa à lista e o código ao conjunto de códigos existentes
                casas.append(Casa(codigo, bairro, tamanho, valor_venda, valor_aluguel))
                codigos_existentes.add(codigo)
                break  # sai do loop se todos os dados forem válidos
            except ValueError as e:
                print(f"Erro: {e}")

    # exibe as casas antes da ordenação
    print("\nCasas antes da ordenação:")
    for casa in casas:
        print(casa)

    # ordena as casas em ordem decrescente pelo valor de venda usando bubble sort
    casas_ordenadas = bubble_sort_decrescente(casas)

    # exibe as casas após a ordenação
    print("\nCasas após a ordenação decrescente pelo valor de venda:")
    for casa in casas_ordenadas:
        print(casa)

main()

# Explicação do Bubble Sort:
# O que é Bubble Sort?: É um algoritmo de ordenação simples que percorre a lista repetidamente, comparando elementos adjacentes e trocando-os se estiverem na ordem errada. O processo é repetido até que a lista esteja ordenada.
# Para que serve o Bubble Sort neste caso?: Aqui, ele é usado para ordenar as casas em ordem decrescente com base no valor_venda. Como o Bubble Sort não é o algoritmo de ordenação mais eficiente, ele é adequado para listas pequenas ou em contextos educacionais para ilustrar conceitos de ordenação.