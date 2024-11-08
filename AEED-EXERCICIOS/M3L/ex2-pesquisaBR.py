"""
Implemente um programa estruturado e recursivo para pesquisa binária. Faça uma função de busca chamada pesquisaBR que receba como parâmetro o valor a ser encontrado e a referência do vetor onde a busca será efetuada. A função retornará -1, caso não encontre o item, ou retornará o índice, caso o encontre.
"""

def pesquisaBR(vetor, valor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor) - 1
    
    if inicio > fim:
        return -1  # Elemento não encontrado
    
    meio = (inicio + fim) // 2
    
    if vetor[meio] == valor:
        return meio
    elif vetor[meio] < valor:
        return pesquisaBR(vetor, valor, meio + 1, fim)
    else:
        return pesquisaBR(vetor, valor, inicio, meio - 1)

def main():
    # Recebe a lista do usuário e converte para uma lista de inteiros
    vetor = list(map(int, input("Digite uma lista de números inteiros ordenados, separados por espaço: ").split()))
    valor = int(input("Digite o valor a ser encontrado: "))
    
    resultado = pesquisaBR(vetor, valor)
    
    if resultado != -1:
        print(f"Valor encontrado no índice: {resultado}")
    else:
        print("Valor não encontrado no vetor.")

# Executa a função principal
if __name__ == "__main__":
    main()
