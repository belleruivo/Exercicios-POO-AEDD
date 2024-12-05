'''3. Crie um programa capaz de realizar as seguintes operações:
a. Instanciar um novo grafo.
b. Adicionar N vértices ao grafo.
c. Conectar dois vértices.
d. Imprimir o grafo em forma de Lista de Adjacências (dinâmica).
e. Obter todos os nós adjacentes (vizinhos) a um nó do grafo (usando a LA).'''

class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []
        else:
            print(f"Vértice {vertice} já existe no grafo.")

    def adicionar_vertices(self, vertices):
        for vertice in vertices:
            self.adicionar_vertice(vertice)

    def conectar_vertices(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            if vertice2 not in self.lista_adjacencia[vertice1]:
                self.lista_adjacencia[vertice1].append(vertice2)
            if vertice1 not in self.lista_adjacencia[vertice2]:
                self.lista_adjacencia[vertice2].append(vertice1)  # Grafo não-direcionado
        else:
            print("Um ou ambos os vértices não existem no grafo.")

    def imprimir_lista_adjacencia(self):
        for vertice, vizinhos in self.lista_adjacencia.items():
            print(f"{vertice}: {', '.join(vizinhos)}")

    def obter_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            return self.lista_adjacencia[vertice]
        else:
            print(f"Vértice {vertice} não encontrado no grafo.")
            return []

# Teste do programa
if __name__ == "__main__":
    grafo = Grafo()

    # a. Instanciar um novo grafo
    print("Novo grafo instanciado.")

    # b. Adicionar N vértices
    vertices = ["A", "B", "C", "D"]
    grafo.adicionar_vertices(vertices)

    # c. Conectar dois vértices
    grafo.conectar_vertices("A", "B")
    grafo.conectar_vertices("A", "C")
    grafo.conectar_vertices("B", "D")

    # d. Imprimir a lista de adjacências
    print("\nLista de Adjacências:")
    grafo.imprimir_lista_adjacencia()

    # e. Obter os vizinhos de um nó
    vertice = "A"
    print(f"\nVizinhos de {vertice}: {grafo.obter_vizinhos(vertice)}")
