'''1. Implemente um programa estruturado e recursivo para pesquisa linear. Faça uma
função de busca chamada pesquisaLR que receba como parâmetro o valor a ser
encontrado e a referência do vetor onde a busca será efetuada. A função retornará -1,
caso não encontre o item, ou retornará o índice, caso o encontre.'''

import random 

def pesquisaLR(valor, lista):
    for i in range(len(lista)):
        if valor == lista[i]:
            return i
    return -1

def gerarLista():
    lista_n = []
    for c in range(10):
        n = random.randint(0, 30)
        lista_n.append(n)
    return lista_n

def main():
    while True:
        try: 
            valor = int(input("Insira o valor a ser procurado: "))
            break
        except ValueError:
            print("\nPor favor, insira um número inteiro válido.")

    lista = gerarLista()

    print(f"\nA lista é: {lista}")

    resultado = pesquisaLR(valor, lista)

    if resultado != -1:
        print(f"\nO valor {valor} foi encontrado no índice: {resultado}")
    else:
        print("\nValor não encontrado.")


main()