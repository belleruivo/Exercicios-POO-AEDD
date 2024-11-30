from node import Node  # importa a classe Node de outro arquivo, presumivelmente para representar os nós da árvore

class BinaryTree:
    def __init__(self):  # inicializa a árvore binária
        self.root = None  # a árvore começa sem nenhum nó, ou seja, a raiz é None

    # Função para inserir um valor na árvore
    def insert(self, value):  # define o método para inserir um valor na árvore
        if self.root is None:  # verifica se a árvore está vazia (sem raiz)
            self.root = Node(value)  # cria a raiz da árvore com o valor fornecido
        else:
            self._insert(self.root, value)  # se a árvore não estiver vazia, chama o método _insert para inserir o valor

    def _insert(self, node, value):  # método auxiliar para inserir um valor recursivamente
        if value < node.value:  # verifica se o valor a ser inserido é menor que o valor do nó atual
            if node.left is None:  # se o nó esquerdo do nó atual estiver vazio
                node.left = Node(value)  # cria um nó à esquerda com o valor fornecido
            else:
                self._insert(node.left, value)  # se já houver um nó à esquerda, recursivamente tenta inserir no nó esquerdo
        elif value > node.value:  # se o valor for maior que o nó atual
            if node.right is None:  # se o nó direito estiver vazio
                node.right = Node(value)  # cria um nó à direita com o valor fornecido
            else:
                self._insert(node.right, value)  # se já houver um nó à direita, recursivamente tenta inserir no nó direito

    # Verifica se a árvore é estritamente binária
    def is_strictly_binary(self):  # método para verificar se a árvore é estritamente binária
        return self._is_strictly_binary(self.root)  # chama a função recursiva para verificar a árvore a partir da raiz

    def _is_strictly_binary(self, node):  # método auxiliar recursivo para verificar se a árvore é estritamente binária
        if node is None:  # se o nó atual for None (ou seja, chegou ao final de uma ramificação)
            return True  # uma árvore vazia (sem nó) é considerada estritamente binária
        if (node.left and not node.right) or (not node.left and node.right):  # se um nó tem um filho e não o outro
            return False  # a árvore não é estritamente binária se um nó tiver apenas um filho
        return self._is_strictly_binary(node.left) and self._is_strictly_binary(node.right)  # recursivamente verifica ambos os filhos

    # Verifica se a árvore é completa
    def is_complete(self):  # método para verificar se a árvore é completa
        total_nodes = self.count_nodes(self.root)  # conta o total de nós na árvore
        return self._is_complete(self.root, 0, total_nodes)  # chama o método auxiliar para verificar se a árvore é completa

    def count_nodes(self, node):  # conta o número de nós na árvore recursivamente
        if node is None:  # se o nó atual for None
            return 0  # retorna 0 porque não há nós aqui
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)  # conta o nó atual e os nós dos filhos esquerdo e direito

    def _is_complete(self, node, index, total_nodes):  # método auxiliar recursivo para verificar se a árvore é completa
        if node is None:  # se o nó atual for None
            return True  # uma árvore vazia em um nível é considerada completa
        if index >= total_nodes:  # se o índice do nó for maior ou igual ao total de nós
            return False  # a árvore não é completa se o índice for maior que o total de nós
        # verifica recursivamente os filhos esquerdo e direito para garantir que todos os nós estão preenchendo a árvore de maneira completa
        return self._is_complete(node.left, 2 * index + 1, total_nodes) and self._is_complete(node.right, 2 * index + 2, total_nodes)

    # Verifica se a árvore é cheia
    def is_full(self):  # método para verificar se a árvore é cheia
        return self._is_full(self.root)  # chama o método auxiliar para verificar a árvore a partir da raiz

    def _is_full(self, node):  # método auxiliar recursivo para verificar se a árvore é cheia
        if node is None:  # se o nó atual for None
            return True  # uma árvore vazia é considerada cheia
        if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):  # se um nó tiver apenas um filho
            return False  # a árvore não é cheia se algum nó tiver um filho e o outro não
        # recursivamente verifica se ambos os filhos de cada nó também são cheios
        return self._is_full(node.left) and self._is_full(node.right)

    # Função para exibir a árvore em ordem (opcional)
    def inorder(self):  # método para exibir a árvore em ordem
        self._inorder(self.root)  # chama o método auxiliar para percorrer a árvore

    def _inorder(self, node):  # método auxiliar recursivo para percorrer a árvore em ordem
        if node:  # se o nó atual não for None
            self._inorder(node.left)  # recursivamente percorre o filho esquerdo
            print(node.value, end=' ')  # imprime o valor do nó atual
            self._inorder(node.right)  # recursivamente percorre o filho direito
