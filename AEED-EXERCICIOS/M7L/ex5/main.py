'''5. Escreva uma versão não recursiva do algoritmo de busca em profundidade.'''

# Grafo: Um grafo é uma estrutura de dados que consiste em um conjunto de vértices (ou nós) e arestas (ou conexões) que ligam esses vértices. No seu exemplo, o grafo é representado como um dicionário, onde as chaves são os vértices e os valores são listas de vértices adjacentes.
# Vértices: As letras 'A', 'B', 'C', 'D', 'E' e 'F' são os vértices do grafo. Cada letra representa um nó no grafo. Por exemplo:
# O vértice 'A' está conectado aos vértices 'B' e 'C'.
# O vértice 'B' está conectado a 'A', 'D' e 'E'.
# E assim por diante.

class Grafo:
    def __init__(self, grafo):
        self.grafo = grafo  # Inicializa o grafo

    def busca_em_profundidade(self, inicio):
        visitados = set()  # Conjunto para rastrear vértices visitados
        pilha = [inicio]   # Pilha para armazenar os vértices a serem explorados

        while pilha:
            vertice = pilha.pop()  # Remove o último vértice adicionado à pilha
            if vertice not in visitados:
                visitados.add(vertice)  # Marca o vértice como visitado
                # Adiciona os vizinhos não visitados à pilha
                pilha.extend(vizinho for vizinho in self.grafo[vertice] if vizinho not in visitados)

        return visitados  # Retorna o conjunto de vértices visitados

# Exemplo de uso
if __name__ == "__main__":
    grafo_dict = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    grafo = Grafo(grafo_dict)  # Cria uma instância da classe Grafo
    resultado = grafo.busca_em_profundidade('A')  # Chama o método da classe
    print("Vértices visitados:", resultado)