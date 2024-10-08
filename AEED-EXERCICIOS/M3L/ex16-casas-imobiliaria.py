'''
16. Crie um vetor que armazene dados de n casas numa imobiliária. Deverão ser
considerados os dados: código, bairro, tamanho em m2, valor de venda e valor de
aluguel. 

Elabore um programa que: preencha o vetor com os dados fornecidos pelo
usuário e ordene de forma decrescente os elementos pelo campo de venda, usando o
bubbleSort.
'''

class Casa:
    def __init__(self, codigo, bairro, tamanho, valor_venda, valor_aluguel):
        self.codigo = codigo
        self.bairro = bairro
        self.tamanho = tamanho
        self.valor_venda = valor_venda
        self.valor_aluguel = valor_aluguel

    def __repr__(self):
        return (f"Casa(codigo={self.codigo}, bairro='{self.bairro}', tamanho={self.tamanho}m², "
                f"valor_venda={self.valor_venda}, valor_aluguel={self.valor_aluguel})")

def bubble_sort_decrescente(casas):
    n = len(casas)
    for i in range(n):
        for j in range(0, n-i-1):
            if casas[j].valor_venda < casas[j+1].valor_venda:
                casas[j], casas[j+1] = casas[j+1], casas[j]
    return casas

def main():
    casas = []
    codigos_existentes = set()
    
    while True:
        try:
            n = int(input("Quantas casas deseja cadastrar? "))
            if n <= 0:
                raise ValueError("O número de casas deve ser maior que zero.")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro maior que zero.")

    for _ in range(n):
        while True:
            try:
                codigo = input("Digite o código da casa (número inteiro): ").strip()
                if not codigo.isdigit():
                    raise ValueError("O código deve ser um número inteiro.")
                if codigo in codigos_existentes:
                    raise ValueError("Código já cadastrado. Digite um código único.")
                
                bairro = input("Digite o bairro da casa: ").strip()
                if not bairro:
                    raise ValueError("O bairro não pode ser vazio.")
                
                tamanho = input("Digite o tamanho da casa em m²: ").strip()
                if not tamanho:
                    raise ValueError("O tamanho não pode ser vazio.")
                try:
                    tamanho = float(tamanho)
                except ValueError:
                    raise ValueError("O tamanho deve ser um número válido.")
                
                valor_venda = input("Digite o valor de venda da casa: ").strip()
                if not valor_venda:
                    raise ValueError("O valor de venda não pode ser vazio.")
                try:
                    valor_venda = float(valor_venda)
                except ValueError:
                    raise ValueError("O valor de venda deve ser um número válido.")
                
                valor_aluguel = input("Digite o valor de aluguel da casa: ").strip()
                if not valor_aluguel:
                    raise ValueError("O valor de aluguel não pode ser vazio.")
                try:
                    valor_aluguel = float(valor_aluguel)
                except ValueError:
                    raise ValueError("O valor de aluguel deve ser um número válido.")
                
                casas.append(Casa(codigo, bairro, tamanho, valor_venda, valor_aluguel))
                codigos_existentes.add(codigo)
                break
            except ValueError as e:
                print(f"Erro: {e}")

    print("\nCasas antes da ordenação:")
    for casa in casas:
        print(casa)

    casas_ordenadas = bubble_sort_decrescente(casas)

    print("\nCasas após a ordenação decrescente pelo valor de venda:")
    for casa in casas_ordenadas:
        print(casa)

main()