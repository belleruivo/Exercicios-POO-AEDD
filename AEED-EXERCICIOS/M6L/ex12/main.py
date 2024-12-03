# Adicione um método rangeFind a uma Árvore Binária de Busca. Esse método espera
# dois itens como argumentos que especificam os limites de um intervalo dos itens a
# serem encontrados na árvore. O método percorre a árvore e constrói e retorna uma
# lista ordenada dos itens encontrados dentro do intervalo especificado.

from binarySearchTree import BinarySearchTree

def main():
    bst = BinarySearchTree()
    valores = [15, 10, 20, 8, 12, 17, 25, 6, 11, 16]

    for valor in valores:
        bst.inserir(valor)

    minimo = int(input("Digite o valor mínimo do intervalo: "))
    maximo = int(input("Digite o valor máximo do intervalo: "))

    resultados = bst.rangeFind(minimo, maximo)
    print(f"Valores no intervalo [{minimo}, {maximo}]: {resultados}")

main()
