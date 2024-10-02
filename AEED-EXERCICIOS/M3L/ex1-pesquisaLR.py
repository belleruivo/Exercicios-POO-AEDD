'''1. Implemente um programa estruturado e recursivo para pesquisa linear. Faça uma
função de busca chamada pesquisaLR que receba como parâmetro o valor a ser
encontrado e a referência do vetor onde a busca será efetuada. A função retornará -1,
caso não encontre o item, ou retornará o índice, caso o encontre.'''

def pesquisaLR(valor, lista):
    for i in range(len(lista)):
        if valor == lista[i]:
            return i
    return -1

def main():
    while True:
        try: 
            valor = int(input("Insira o valor a ser procurado: "))
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    lista = [1, 5, 2, 8, 7, 9, 10]

    resultado = pesquisaLR(valor, lista)
    if resultado != -1:
        print(f"O valor {valor} foi encontrado no índice: {resultado}")
    else:
        print("Valor não encontrado.")


main()