'''5. Faça um programa que cadastre n produtos. Para cada produto devem ser
cadastrados código do produto, preço e quantidade estocada. Os dados devem ser
armazenados em uma lista simplesmente encadeada e não ordenada. Posteriormente,
receber do usuário a taxa de desconto (ex.: digitar 10 para taxa de desconto de 10%).
Aplicar a taxa digitada ao preço de todos os produtos cadastrados e finalmente
mostrar um relatório com o código e o novo preço. O final desse relatório deve
apresentar também a quantidade de produtos com quantidade estocada superior a
500.'''

from listaEncadeada import ListaEncadeada
from produto import Produto

def main():
    lista_produtos = ListaEncadeada()
    
    print("-="*30)
    while True:
        try:
            n = int(input("Digite o número de produtos a serem cadastrados: "))
            if n < 0:
                print("O valor não pode ser negativo.")
            break
        except ValueError:
            print(f"Entrada inválida. Certifique-se de inserir um número Inteiro\n")

    for i in range(n):
        while True:
            try:
                codigo = int(input(f"\nDigite o código do {i+1}º produto: "))
                if codigo < 0:
                    print("O valor não pode ser negativo.")
                break
            except ValueError:
                print(f"Entrada inválida. Certifique-se de inserir um número Inteiro")
        while True:
            try:
                preco = float(input("Digite o preço do produto: "))
                if preco < 0:
                    print("O valor não pode ser negativo.")
                break
            except ValueError:
                print(f"Entrada inválida. Certifique-se de inserir um número Inteiro\n")
        while True:
            try:
                quantidade = int(input("Digite a quantidade estocada do produto: "))
                if quantidade < 0:
                    print("O valor não pode ser negativo.")
                break
            except ValueError:
                print(f"Entrada inválida. Certifique-se de inserir um número Inteiro\n")

        produto = Produto(codigo, preco, quantidade)
        lista_produtos.adicionar_produto(produto)

    while True:
            try:
                taxa_desconto = float(input("\nDigite a taxa de desconto (%): "))
                if taxa_desconto < 0:
                    print("O valor não pode ser negativo.")
                break
            except ValueError:
                print(f"Entrada inválida. Certifique-se de inserir um número Inteiro")

    lista_produtos.aplicar_desconto(taxa_desconto)

    relatorio_produtos, quantidade_acima_500 = lista_produtos.relatorio()

    print("\nRelatório de Produtos:")
    for codigo, preco in relatorio_produtos:
        print(f"Código: {codigo}, Novo Preço: R${preco:.2f}")
    
    print(f"\nQuantidade de produtos com estoque superior a 500: {quantidade_acima_500}")
    print("-="*30)

main()