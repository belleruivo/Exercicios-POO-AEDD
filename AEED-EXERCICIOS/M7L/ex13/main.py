'''
Execute o algoritmo do caminho mínimo para o grafo abaixo e determine o custo do menor caminho entre os vértices x e t.
'''

from Graph import Graph

def create_graph():
    vertices = 7
    g = Graph(vertices)
    edges = [
        (0, 1, 30), (0, 2, 12),
        (1, 2, 35), (1, 3, 17), (1, 4, 15),
        (2, 3, 25), (2, 5, 20),
        (3, 4, 15), (3, 5, 7),
        (4, 5, 10), (4, 6, 5),
        (5, 6, 12)
    ]
    
    for src, dest, weight in edges:
        g.add_edge(src, dest, weight)
    
    return g

if __name__ == "__main__":
    vertices_mapping = {'x': 0, 'v': 1, 'z': 2, 'r': 3, 'u': 4, 's': 5, 't': 6}
    vertex_names = ['x', 'v', 'z', 'r', 'u', 's', 't']
    g = create_graph()
    source = vertices_mapping['x']
    destination = vertices_mapping['t']
    g.print_shortest_path(source, destination, vertex_names)

'''
Neste código:

Graph.py: contém a classe Graph com a implementação do algoritmo de Dijkstra e a função para imprimir o menor caminho.

main.py: cria o grafo, adiciona as arestas com seus pesos, mapeia os vértices para índices, e calcula o menor caminho entre 𝑥 e 𝑡 usando o algoritmo de Dijkstra.
Ao executar o código, ele imprimirá o custo do menor caminho e o caminho entre os vértices 𝑥 e 𝑡
.
'''