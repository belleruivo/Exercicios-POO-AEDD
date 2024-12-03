# Apenas imprimindo linearmente os elementos da árvore não é possível reproduzir
# sua estrutura. Faça um método imprimeRelacoes que percorra a árvore imprimindo
# as relações entre os nós, de forma que se possa através dessa descrição reproduzir a
# estrutura de uma árvore. Exemplos de descrições impressas são:
# - o nó de valor XXX é filho esquerdo de YYY
# - o nó de valor ZZZ é filho direito de YYY
# - o nó de valor XXX não tem filho esquerdo
# - o nó de valor ZZZ não tem filho direito

from node import Node 
from binaryTree import BinaryTree

if __name__ == "__main__":
    arvore = BinaryTree()
    arvore.raiz = Node(1)
    arvore.raiz.esquerdo = Node(2)
    arvore.raiz.direito = Node(3)
    arvore.raiz.esquerdo.esquerdo = Node(4)
    arvore.raiz.esquerdo.direito = Node(5)

    arvore.imprimeRelacoes()
