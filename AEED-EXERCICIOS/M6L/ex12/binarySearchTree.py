from node import Node 

class BinarySearchTree:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo_no = Node(valor)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, atual, novo_no):
        if novo_no.valor < atual.valor:
            if atual.esquerdo is None:
                atual.esquerdo = novo_no
            else:
                self._inserir_recursivo(atual.esquerdo, novo_no)
        else:
            if atual.direito is None:
                atual.direito = novo_no
            else:
                self._inserir_recursivo(atual.direito, novo_no)

    def rangeFind(self, minimo, maximo):
        resultado = []
        self._rangeFind_recursivo(self.raiz, minimo, maximo, resultado)
        return resultado

    def _rangeFind_recursivo(self, no, minimo, maximo, resultado):
        if no is None:
            return

        if minimo <= no.valor <= maximo:
            resultado.append(no.valor)

        if minimo < no.valor:
            self._rangeFind_recursivo(no.esquerdo, minimo, maximo, resultado)

        if no.valor < maximo:
            self._rangeFind_recursivo(no.direito, minimo, maximo, resultado)