from binary_tree_node import BinaryTreeNode  # Importa a classe que representa um nó na árvore binária.

class BinaryTree:
    def __init__(self):
        """
        inicializa uma árvore binária vazia.
        """
        self.root = None  # Define a raiz da árvore como None, já que inicialmente a árvore está vazia.

    def insert(self, value):
        """
        insere um número na árvore binária.
        """
        if not isinstance(value, int):  # Verifica se o valor é um número inteiro.
            raise ValueError("o valor deve ser um número inteiro.")  # Lança um erro se não for.
        if self.root is None:  # Se a raiz da árvore for None (árvore vazia):
            self.root = BinaryTreeNode(value)  # Cria um novo nó como raiz.
        else:
            self._insert_recursive(self.root, value)  # Caso contrário, insere recursivamente.

    def _insert_recursive(self, current_node, value):
        """
        método auxiliar para inserir recursivamente na árvore.
        """
        if value < current_node.value:  # Se o valor for menor que o nó atual:
            if current_node.left is None:  # E o filho à esquerda for vazio:
                current_node.left = BinaryTreeNode(value)  # Adiciona um novo nó à esquerda.
            else:
                self._insert_recursive(current_node.left, value)  # Continua a busca à esquerda.
        elif value > current_node.value:  # Se o valor for maior que o nó atual:
            if current_node.right is None:  # E o filho à direita for vazio:
                current_node.right = BinaryTreeNode(value)  # Adiciona um novo nó à direita.
            else:
                self._insert_recursive(current_node.right, value)  # Continua a busca à direita.

    def get_leaf_nodes(self):
        """
        retorna todos os nós folha da árvore.
        """
        leaf_nodes = []  # Lista para armazenar os nós folha.
        self._collect_leaf_nodes(self.root, leaf_nodes)  # Chama o método auxiliar para preencher a lista.
        return leaf_nodes  # Retorna a lista com os valores dos nós folha.

    def _collect_leaf_nodes(self, node, leaf_nodes):
        """
        método auxiliar para coletar nós folha recursivamente.
        """
        if node:  # Se o nó não for None:
            if node.left is None and node.right is None:  # Verifica se o nó é folha.
                leaf_nodes.append(node.value)  # Adiciona o valor do nó à lista.
            self._collect_leaf_nodes(node.left, leaf_nodes)  # Busca nós folha à esquerda.
            self._collect_leaf_nodes(node.right, leaf_nodes)  # Busca nós folha à direita.

    def find_ancestors(self, target):
        """
        retorna uma lista de ancestrais do nó com o valor 'target'.
        """
        ancestors = []  # Lista para armazenar os ancestrais.
        if not self._find_ancestors_recursive(self.root, target, ancestors):  # Chama o método auxiliar.
            raise ValueError(f"nó com valor {target} não encontrado.")  # Lança um erro se o nó não existir.
        return ancestors  # Retorna a lista de ancestrais.

    def _find_ancestors_recursive(self, node, target, ancestors):
        """
        método auxiliar para encontrar ancestrais de forma recursiva.
        """
        if node is None:  # Caso base: se o nó for None, retorna False.
            return False
        if node.value == target:  # Se o nó atual é o alvo:
            return True
        if (self._find_ancestors_recursive(node.left, target, ancestors) or
                self._find_ancestors_recursive(node.right, target, ancestors)):  # Busca recursiva.
            ancestors.append(node.value)  # Adiciona o valor do nó atual à lista de ancestrais.
            return True
        return False  # Retorna False se o valor não for encontrado.

    def find_descendants(self, target):
        """
        retorna todos os descendentes do nó com valor 'target'.
        """
        target_node = self._find_node(self.root, target)  # Encontra o nó alvo.
        if not target_node:  # Se o nó alvo não for encontrado:
            raise ValueError(f"nó com valor {target} não encontrado.")  # Lança um erro.
        descendants = []  # Lista para armazenar os descendentes.
        self._collect_all_nodes(target_node, descendants)  # Preenche a lista de descendentes.
        return descendants  # Retorna a lista.

    def _collect_all_nodes(self, node, nodes):
        """
        método auxiliar para coletar todos os descendentes recursivamente.
        """
        if node:  # Se o nó não for None:
            if node.left or node.right:  # Se o nó tiver pelo menos um filho:
                nodes.append(node.value)  # Adiciona o valor à lista.
            self._collect_all_nodes(node.left, nodes)  # Busca descendentes à esquerda.
            self._collect_all_nodes(node.right, nodes)  # Busca descendentes à direita.

    def find_parent_and_children(self, target):
        """
        retorna o nó pai e os nós filhos de um nó com valor 'target'.
        """
        parent = None  # Inicializa o pai como None.
        current = self.root  # Começa a busca a partir da raiz.
        while current:  # Enquanto não alcançar o final da árvore:
            if target < current.value:  # Se o valor do alvo for menor:
                parent = current  # Atualiza o pai.
                current = current.left  # Move para a subárvore à esquerda.
            elif target > current.value:  # Se o valor do alvo for maior:
                parent = current  # Atualiza o pai.
                current = current.right  # Move para a subárvore à direita.
            else:  # Se encontrar o nó alvo:
                return {
                    "pai": parent.value if parent else None,  # Retorna o valor do pai, se existir.
                    "filho_esquerda": current.left.value if current.left else None,  # Valor do filho à esquerda.
                    "filho_direita": current.right.value if current.right else None  # Valor do filho à direita.
                }
        raise ValueError(f"nó com valor {target} não encontrado.")  # Lança erro se o nó não for encontrado.

    def _find_node(self, node, value):
        """
        encontra um nó pelo valor.
        """
        if node is None or node.value == value:  # Caso base: nó encontrado ou None.
            return node
        if value < node.value:  # Se o valor procurado for menor:
            return self._find_node(node.left, value)  # Busca na subárvore esquerda.
        return self._find_node(node.right, value)  # Caso contrário, busca na subárvore direita.
