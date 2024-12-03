# Faça um programa para executar as operações abaixo em uma árvore binária
# ordenada pelo código, onde o dado não seja um inteiro, mas uma estrutura contendo
# dados de um estudante: código, nome, idade, altura e média acadêmica.
# Menu
# 1 – Inserir estudante
# 2 – Mostrar o estudante mais alto
# 3 – Mostrar o estudante mais velho
# 4 – Mostrar os estudantes maiores de idade
# 5 – Mostrar o estudante com maior média acadêmica
# 6 – Mostrar o estudante com menor média acadêmica
# 7 – Sair

from binaryTree import BinaryTree
from estudante import Estudante


if __name__ == "__main__":
    arvore = BinaryTree()

    while True:
        print("\nMenu")
        print("1 – Inserir estudante")
        print("2 – Mostrar o estudante mais alto")
        print("3 – Mostrar o estudante mais velho")
        print("4 – Mostrar os estudantes maiores de idade")
        print("5 – Mostrar o estudante com maior média acadêmica")
        print("6 – Mostrar o estudante com menor média acadêmica")
        print("7 – Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            codigo = int(input("Digite o código: "))
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            altura = float(input("Digite a altura: "))
            media = float(input("Digite a média acadêmica: "))
            estudante = Estudante(codigo, nome, idade, altura, media)
            arvore.inserir(estudante)

        elif opcao == 2:
            mais_alto = arvore.encontrar_mais_alto()
            print("Estudante mais alto:")
            print(mais_alto if mais_alto else "Árvore vazia")

        elif opcao == 3:
            mais_velho = arvore.encontrar_mais_velho()
            print("Estudante mais velho:")
            print(mais_velho if mais_velho else "Árvore vazia")

        elif opcao == 4:
            maiores_de_idade = arvore.listar_maiores_de_idade()
            print("Estudantes maiores de idade:")
            for estudante in maiores_de_idade:
                print(estudante)

        elif opcao == 5:
            maior_media = arvore.encontrar_maior_media()
            print("Estudante com maior média acadêmica:")
            print(maior_media if maior_media else "Árvore vazia")

        elif opcao == 6:
            menor_media = arvore.encontrar_menor_media()
            print("Estudante com menor média acadêmica:")
            print(menor_media if menor_media else "Árvore vazia")

        elif opcao == 7:
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")
