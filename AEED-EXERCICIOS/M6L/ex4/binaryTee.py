class BinaryTree:
    def __init__(self):
        self.raiz = None

    def imprimeRelacoes(self):
        def percorreEImprime(no):
            if no is None:
                return

            if no.esquerdo:
                print(f"O nó de valor {no.esquerdo.valor} é filho esquerdo de {no.valor}")
            else:
                print(f"O nó de valor {no.valor} não tem filho esquerdo")

            if no.direito:
                print(f"O nó de valor {no.direito.valor} é filho direito de {no.valor}")
            else:
                print(f"O nó de valor {no.valor} não tem filho direito")

            percorreEImprime(no.esquerdo)
            percorreEImprime(no.direito)

        if self.raiz is None:
            print("A árvore está vazia.")
        else:
            percorreEImprime(self.raiz)