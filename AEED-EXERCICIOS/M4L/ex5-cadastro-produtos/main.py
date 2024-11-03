'''5. Faça um programa que cadastre n produtos. Para cada produto devem ser
cadastrados código do produto, preço e quantidade estocada. Os dados devem ser
armazenados em uma lista simplesmente encadeada e não ordenada. Posteriormente,
receber do usuário a taxa de desconto (ex.: digitar 10 para taxa de desconto de 10%).
Aplicar a taxa digitada ao preço de todos os produtos cadastrados e finalmente
mostrar um relatório com o código e o novo preço. O final desse relatório deve
apresentar também a quantidade de produtos com quantidade estocada superior a
500.'''

from listaEncadeada import UnorderedLinkedList


def main():
    produtos = UnorderedLinkedList()
    
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
        produtos.add({'codigo': codigo, 'preco': preco, 'quantidade': quantidade})

    while True:
            try:
                taxa_desconto = float(input("\nDigite a taxa de desconto (%): "))
                if taxa_desconto < 0:
                    print("O valor não pode ser negativo.")
                break
            except ValueError:
                print(f"Entrada inválida. Certifique-se de inserir um número Inteiro")

    produtos.apply_discount(taxa_desconto)
    produtos.report()

main()