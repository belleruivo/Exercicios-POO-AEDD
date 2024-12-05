'''2. Crie um programa capaz de:
a. Instanciar um novo grafo.
b. Adicionar um vértice ao grafo.
c. Conectar dois vértices.
d. Imprimir o grafo em forma de Matriz de Adjacências.
e. Obter todos os nós adjacentes (vizinhos) a um nó do grafo (usando a MA).'''

class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz_adjacencia = []

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            # Adiciona uma nova linha e coluna na matriz de adjacência
            for linha in self.matriz_adjacencia:
                linha.append(0)
            self.matriz_adjacencia.append([0] * len(self.vertices))
        else:
            print(f"Vértice {vertice} já existe no grafo.")

    def conectar_vertices(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            indice1 = self.vertices.index(vertice1)
            indice2 = self.vertices.index(vertice2)
            self.matriz_adjacencia[indice1][indice2] = 1
            self.matriz_adjacencia[indice2][indice1] = 1  # Grafo não-direcionado
        else:
            print("Um ou ambos os vértices não existem no grafo.")

    def imprimir_matriz_adjacencia(self):
        print("  ", " ".join(self.vertices))
        for vertice, linha in zip(self.vertices, self.matriz_adjacencia):
            print(vertice, " ".join(map(str, linha)))

    def obter_vizinhos(self, vertice):
        if vertice in self.vertices:
            indice = self.vertices.index(vertice)
            vizinhos = [
                self.vertices[i]
                for i, adjacente in enumerate(self.matriz_adjacencia[indice])
                if adjacente == 1
            ]
            return vizinhos
        else:
            print(f"Vértice {vertice} não encontrado no grafo.")
            return []


def main():
    grafo = Grafo()

    # a. Instanciar um novo grafo
    print("Novo grafo instanciado.")

    # b. Adicionar vértices
    grafo.adicionar_vertice("A")
    grafo.adicionar_vertice("B")
    grafo.adicionar_vertice("C")

    # c. Conectar dois vértices
    grafo.conectar_vertices("A", "B")
    grafo.conectar_vertices("B", "C")

    # d. Imprimir a matriz de adjacências
    print("\nMatriz de Adjacências:")
    grafo.imprimir_matriz_adjacencia()

    # e. Obter os vizinhos de um nó
    vertice = "B"
    print(f"\nVizinhos de {vertice}: {grafo.obter_vizinhos(vertice)}")

main()
