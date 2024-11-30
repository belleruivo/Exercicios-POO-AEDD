'''2. Faça um programa para executar as operações abaixo em uma árvore binária.
Menu
1 – Inserir número
2 – Mostrar nós folha
3 – Mostrar os nós ancestrais de um nó
4 – Mostrar os descendentes de um nó
5 – Mostrar o nó pai e os nós filhos de um nó
6 – Sair'''

# esta classe representa um nó na árvore binária
class BinaryTreeNode:
    def __init__(self, value):
        """
        inicializa o nó com um valor. cada nó pode ter no máximo dois filhos:
        um à esquerda e outro à direita.
        """
        self.value = value  # valor armazenado no nó
        self.left = None  # referência para o filho à esquerda
        self.right = None  # referência para o filho à direita
