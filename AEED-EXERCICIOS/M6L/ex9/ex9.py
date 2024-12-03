'''9. Crie uma árvore binária ordenada para implementar um dicionário da língua inglesa.
Cada nó precisa ter a palavra e o seu significado. Implemente as funções básicas
para inserção, remoção, pesquisa e impressão do dicionário.'''

class Node:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None


class BinarySearchTreeDictionary:
    def __init__(self):
        self.root = None

    def insert(self, word, meaning):
        def _insert_recursive(node, word, meaning):
            if node is None:
                return Node(word, meaning)
            if word < node.word:
                node.left = _insert_recursive(node.left, word, meaning)
            elif word > node.word:
                node.right = _insert_recursive(node.right, word, meaning)
            else:
                print(f"A palavra '{word}' já está no dicionário.")
            return node

        self.root = _insert_recursive(self.root, word, meaning)

    def search(self, word):
        def _search_recursive(node, word):
            if node is None:
                return None
            if word == node.word:
                return node.meaning
            elif word < node.word:
                return _search_recursive(node.left, word)
            else:
                return _search_recursive(node.right, word)

        result = _search_recursive(self.root, word)
        if result:
            print(f"Significado de '{word}': {result}")
        else:
            print(f"A palavra '{word}' não foi encontrada no dicionário.")
        return result

    def remove(self, word):
        def _remove_recursive(node, word):
            if node is None:
                return None
            if word < node.word:
                node.left = _remove_recursive(node.left, word)
            elif word > node.word:
                node.right = _remove_recursive(node.right, word)
            else:
                # Nó com um único filho ou nenhum
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Nó com dois filhos: encontre o sucessor (menor na subárvore direita)
                temp = self._find_min(node.right)
                node.word, node.meaning = temp.word, temp.meaning
                node.right = _remove_recursive(node.right, temp.word)

            return node

        self.root = _remove_recursive(self.root, word)

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def print_dictionary(self):
        def _in_order_traversal(node):
            if node is not None:
                _in_order_traversal(node.left)
                print(f"{node.word}: {node.meaning}")
                _in_order_traversal(node.right)

        print("Dicionário:")
        _in_order_traversal(self.root)


# Exemplo de uso
dictionary = BinarySearchTreeDictionary()
dictionary.insert("apple", "A sweet fruit")
dictionary.insert("banana", "A yellow fruit")
dictionary.insert("cherry", "A small red fruit")

dictionary.print_dictionary()

dictionary.search("banana")
dictionary.search("grape")

dictionary.remove("banana")
dictionary.print_dictionary()
