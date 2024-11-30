from node import Node

class BinaryTree:
    def __init__(self):
        self.root = None

    # Função para inserir um valor na árvore
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # Verifica se a árvore é estritamente binária
    def is_strictly_binary(self):
        return self._is_strictly_binary(self.root)

    def _is_strictly_binary(self, node):
        if node is None:
            return True
        if (node.left and not node.right) or (not node.left and node.right):
            return False
        return self._is_strictly_binary(node.left) and self._is_strictly_binary(node.right)

    # Verifica se a árvore é completa
    def is_complete(self):
        total_nodes = self.count_nodes(self.root)
        return self._is_complete(self.root, 0, total_nodes)

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def _is_complete(self, node, index, total_nodes):
        if node is None:
            return True
        if index >= total_nodes:
            return False
        return self._is_complete(node.left, 2 * index + 1, total_nodes) and self._is_complete(node.right, 2 * index + 2, total_nodes)

    # Verifica se a árvore é cheia
    def is_full(self):
        return self._is_full(self.root)

    def _is_full(self, node):
        if node is None:
            return True
        if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            return False
        return self._is_full(node.left) and self._is_full(node.right)

    # Função para exibir a árvore em ordem (opcional)
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=' ')
            self._inorder(node.right)

         # Função para imprimir a árvore de forma visual
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root, 0)
        else:
            print("Árvore vazia.")
    
    def _print_tree(self, node, level):
        if node is not None:
            self._print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self._print_tree(node.left, level + 1)
    
    # Função para rebalancear a árvore
    def rebalance(self):
        if self.root is None:
            print("A árvore está vazia. Não é possível rebalancear.")
            return

        # Passo 1: Percorrer a árvore em in-ordem e armazenar os itens na lista
        items = []
        self._inorder_to_list(self.root, items)

        # AQUI - LIMPA A ARVORE Passo 2: Limpar a árvore
        self.root = None

        # Passo 3: Inserir os itens de volta de maneira balanceada
        self._rebalance_from_list(items, 0, len(items) - 1)

        print("A árvore foi rebalanceada.")

    # AQUI - PERCURSO EM ORDEM - Função auxiliar que percorre a árvore em in-ordem e armazena os itens na lista
    def _inorder_to_list(self, node, items):
        if node is not None:
            self._inorder_to_list(node.left, items)  # Visita a subárvore esquerda
            items.append(node.value)  # Adiciona o valor à lista
            self._inorder_to_list(node.right, items)  # Visita a subárvore direita

    # Função auxiliar para inserir itens de forma balanceada, pegando o meio da lista
#     A função recursiva _rebalance_from_list insere o valor no meio da lista e depois chama recursivamente para as sublistas à esquerda e à direita, garantindo que os valores sejam inseridos de forma balanceada.
# O valor médio de uma lista é o item no meio (índice (start + end) // 2), e este valor é inserido na árvore, com a recursão dividindo as listas em dois e repetindo o processo.
    def _rebalance_from_list(self, items, start, end):
        if start > end:
            return

        mid = (start + end) // 2  # Encontra o índice do meio da lista
        self.insert(items[mid])  # Insere o item no meio da árvore

        # Recursão para inserir os itens da sublista esquerda
        self._rebalance_from_list(items, start, mid - 1)

        # Recursão para inserir os itens da sublista direita
        self._rebalance_from_list(items, mid + 1, end)


# Resumo da Implementação:
# Passo 1: Percorre a árvore em in-ordem com a função _inorder_to_list e armazena os valores em uma lista.
# Passo 2: Limpa a árvore ao redefinir self.root = None.
# Passo 3: Insere os itens de volta na árvore de maneira balanceada, utilizando o índice médio de cada sublista de itens, através da função _rebalance_from_list.
# O que foi feito exatamente:
# "Copia os itens da árvore para uma lista durante um percurso em in-ordem": Isso foi feito pela função _inorder_to_list, que percorre a árvore e armazena os valores em uma lista.
# "Em seguida, limpa a árvore": A árvore foi limpa ao definir self.root = None.
# "Copia os itens da lista de volta para a árvore de tal maneira que a forma da árvore permaneça balanceada": A reinserção foi feita pela função _rebalance_from_list, que usa o índice médio da lista para garantir que a árvore se mantenha balanceada.