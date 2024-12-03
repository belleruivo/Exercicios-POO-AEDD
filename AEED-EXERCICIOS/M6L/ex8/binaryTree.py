from node import Node
class BinaryTree:
    def __init__(self):
        self.raiz = None

    def inserir(self, estudante):
        novo_no = Node(estudante)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, atual, novo_no):
        if novo_no.estudante.codigo < atual.estudante.codigo:
            if atual.esquerdo is None:
                atual.esquerdo = novo_no
            else:
                self._inserir_recursivo(atual.esquerdo, novo_no)
        else:
            if atual.direito is None:
                atual.direito = novo_no
            else:
                self._inserir_recursivo(atual.direito, novo_no)

    def encontrar_mais_alto(self):
        return self._encontrar_extremo(self.raiz, key=lambda est: est.altura, maior=True)

    def encontrar_mais_velho(self):
        return self._encontrar_extremo(self.raiz, key=lambda est: est.idade, maior=True)

    def encontrar_maior_media(self):
        return self._encontrar_extremo(self.raiz, key=lambda est: est.media, maior=True)

    def encontrar_menor_media(self):
        return self._encontrar_extremo(self.raiz, key=lambda est: est.media, maior=False)

    def listar_maiores_de_idade(self):
        resultado = []
        self._listar_maiores_de_idade_recursivo(self.raiz, resultado)
        return resultado

    def _listar_maiores_de_idade_recursivo(self, no, resultado):
        if no is None:
            return
        if no.estudante.idade >= 18:
            resultado.append(no.estudante)
        self._listar_maiores_de_idade_recursivo(no.esquerdo, resultado)
        self._listar_maiores_de_idade_recursivo(no.direito, resultado)

    def _encontrar_extremo(self, no, key, maior):
        if no is None:
            return None

        melhor = no.estudante
        if maior:
            comparar = lambda a, b: a > b
        else:
            comparar = lambda a, b: a < b

        def procurar(no_atual):
            nonlocal melhor
            if no_atual is None:
                return
            if comparar(key(no_atual.estudante), key(melhor)):
                melhor = no_atual.estudante
            procurar(no_atual.esquerdo)
            procurar(no_atual.direito)

        procurar(no)
        return melhor